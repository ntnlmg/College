import random


class AlgoritmaGenetika:
    def __init__(self, jumlah_generasi, jumlah_kromosom, panjang_individu, prob_crossover, prob_mutasi):
        self.jumlah_generasi = jumlah_generasi
        self.jumlah_kromosom = jumlah_kromosom
        self.panjang_individu = panjang_individu
        self.prob_crossover = prob_crossover
        self.prob_mutasi = prob_mutasi
        self.d = [3475, 1223, 2260, 2700, 2950]  # demand
        self.m = [1, 0.53, 0.5, 0.6, 0.7]  # material
        self.s = [4000, 1600, 1000, 990, 2800]  # supply
        self.t = [0.85, 0.9, 0.85, 0.85, 0.9]
        self.b_du = [297, 334, 432, 226, 258]
        self.b_ks = [300, 300, 300, 300, 300]
        self.ub = []
        self.lb = []
        self.bit = [0, 0, 0, 0, 0]
        self.offspring = []
        self.gen = []
        self.fitness = []
        self.inisialisasiGen()
        self.cariOptimum()

    def cariBit(self):
        n = 0
        bit = 1
        while n < 5:
            for j in range(len(self.d)):
                batas_atas = self.ub[j]
                batas_bawah = self.lb[j]
                if (2 ** (bit - 1)) < (batas_atas - batas_bawah) * (10 ** self.panjang_individu) <= ((2 ** bit) - 1):
                    self.bit[j] = bit
                    n += 1
            bit += 1

    def inisialisasiGen(self):
        self.cariBatasAtasBatasBawah()
        self.cariBit()
        for _ in range(self.jumlah_kromosom):
            biner = []
            for j in range(len(self.d)):
                biner.append(format(random.randint(
                    2 ** (self.bit[j] - 1), 2 ** self.bit[j]), '0b'))
            self.gen.append(''.join(ind for ind in biner))

    def cariBatasAtasBatasBawah(self):
        for j in range(len(self.d)):
            # minimasi kayu segar
            self.ub.append(self.d[j])
            self.lb.append(self.d[j] - round(self.d[j] * self.m[j] if self.s[j]
                           * self.t[j] >= self.d[j] * self.m[j] else self.s[j] * self.t[j]))

            # if s * t >= demand * m
            # true = demand - (demand * m)
            # false = demand - (s * t)

    @staticmethod
    def desimalKeVariabel(desimal, batas_atas, batas_bawah, bit):
        return batas_bawah + desimal * ((batas_atas - batas_bawah) / ((2 ** bit) - 1))

    def cariOptimum(self):
        for _ in range(self.jumlah_generasi):
            self.offspring.clear()

            mutation = self.mutation()
            crossover = self.crossover()
            self.offspring += mutation + crossover

            # enlarge
            self.gen += self.offspring
            self.hitungFitness()
            self.seleksi()

    def hitungFitness(self):
        self.fitness = []

        for kromosom in self.gen:
            total_biaya = 0
            bit = 0
            for j in range(len(self.d)):
                ba = self.ub[j]
                bb = self.lb[j]
                # kayu segar  = (jumlah kayu * cost kayu segar) + ((demand - kayu segar) * cost daur ulang)
                variabelJ = self.desimalKeVariabel(desimal=int(kromosom[bit:bit+self.bit[j]], 2),
                                                   batas_atas=ba,
                                                   batas_bawah=bb,
                                                   bit=self.bit[j])
                kayu_segar = round(variabelJ)
                # daur ulang = (demand - kayu segar)
                daur_ulang = self.d[j] - kayu_segar
                # (kayu segar * biaya produksi) + (daur ulang * biaya daur ulang)
                total_biaya += (kayu_segar *
                                self.b_ks[j]) + (daur_ulang * self.b_du[j])
                print(total_biaya, j)
                bit += self.bit[j]
            self.fitness.append(total_biaya)

    def crossover(self):
        gen_terpilih = []
        hasil_crossover = []
        # Pemilihan Gen
        for i in range(self.jumlah_kromosom - 1):
            if random.random() < self.prob_crossover:
                gen_terpilih.append(self.gen[i])

        if len(gen_terpilih) > 1:
            # crossover untuk gen terpilih
            for i in range(len(gen_terpilih)):
                for j in range(i+1, len(gen_terpilih)):
                    # one cut point
                    cutpoint = random.randint(0, sum(self.bit) - 1)
                    hasil_crossover.append(
                        gen_terpilih[i][0:cutpoint]
                        + gen_terpilih[j][cutpoint:len(gen_terpilih[j])])
        return hasil_crossover

    def mutation(self):
        mutation = []
        for i in range(len(self.gen)):
            if random.random() < self.prob_mutasi:
                kromosom = random.randint(0, len(self.gen)-1)
                pos = random.randint(0, len(self.gen[kromosom]) - 1)
                mutation.append(
                    self.gen[kromosom][0:pos] +
                    ('1' if self.gen[kromosom][pos] == '0' else '0') +
                    self.gen[kromosom][pos+1:len(self.gen[kromosom])+1])
        return mutation

    # natan
    def seleksi(self):
        for i in range(len(self.fitness)):
            for j in range(0, len(self.fitness)-i-1):
                if self.fitness[j] > self.fitness[j + 1]:
                    temp = self.gen[j]
                    self.gen[j] = self.gen[j + 1]
                    self.gen[j + 1] = temp
                    temp = self.fitness[j]
                    self.fitness[j] = self.fitness[j + 1]
                    self.fitness[j + 1] = temp
        self.fitness = self.fitness[:self.jumlah_kromosom]
        self.gen = self.gen[:self.jumlah_kromosom]


def main():
    GA = AlgoritmaGenetika(jumlah_generasi=1000,
                           jumlah_kromosom=20,
                           panjang_individu=5,
                           prob_mutasi=0.2,
                           prob_crossover=0.3)

    print("Total biaya: Rp", min(GA.fitness))
    bit = 0
    kromosom = GA.gen[GA.gen == min(GA.fitness)]
    for j in range(5):
        ba = GA.ub[j]
        bb = GA.lb[j]
        variabelJ = GA.desimalKeVariabel(desimal=int(kromosom[bit:bit + GA.bit[j]], 2),
                                         batas_atas=ba,
                                         batas_bawah=bb,
                                         bit=GA.bit[j])
        bit += GA.bit[j]
        print("Variabel", j+1, ":", round(variabelJ))


if __name__ == "__main__":
    main()


# x = []
# for _ in range(3):
#     x.append(format(random.randint(2 ** 3, 2 ** 4), '0b'))
#
# z = ''.join(h for h in x)
#
# print(x)
# print(z)

# print(GA.gen)
# print(GA.bit_x)
# print(GA.bit_y)
#
# for i in range(GA.ukuran_gen):
#     print(int(GA.gen[i][GA.bit_x:(len(GA.gen)-1)], 2))

# abc = [4,5,6]
# fgh = [7,8,9]
# abc += fgh
# print(abc)


# simulasi mutasi
# bde = ''
# bde = '10010100001'
# bdehasil = []
# a = random.randint(0, len(bde)-1)
# print(a)
# bdehasil.append(bde[0:a] + ('1' if bde[a] == '0' else '0') + bde[a+1:len(bde)+1])
# print(bdehasil)
# jfk = ['000', '001', '010']
#
# for i in range (len(bde)):
#     print(bde[i] + jfk[i])
#     print(bde[i][0:len(bde)])

# abc = list(range(1, 6))
#
# for i in range (len(abc)):
#     for j in range (i+1, len(abc)):
#         print(abc[i], " dengan ", abc[j])
