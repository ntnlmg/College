import random

class AlgoritmaGenetika:
    def __init__(self, jumlah_generasi, jumlah_kromosom, panjang_individu, prob_crossover, prob_mutasi):
        self.jumlah_generasi = jumlah_generasi
        self.jumlah_kromosom = jumlah_kromosom
        self.panjang_individu = panjang_individu
        self.prob_crossover = prob_crossover
        self.prob_mutasi = prob_mutasi
        self.d = [3475, 1223, 2260, 2700, 2950]
        self.m = [1, 0.53, 0.5, 0.6, 0.7]
        self.s = [4000, 1600, 1000, 990, 2800]
        self.t = [0.85, 0.9, 0.85, 0.85, 0.9]
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
                    n+=1
            bit += 1

    def inisialisasiGen(self):
        self.cariBatasAtasBatasBawah()
        self.cariBit()
        for _ in range(self.jumlah_kromosom):
            biner = []
            for j in range(len(self.d)):
                biner.append(format(random.randint(2 ** (self.bit[j] - 1), 2 ** self.bit[j]), '0b'))
            self.gen.append(''.join(ind for ind in biner))

    def cariBatasAtasBatasBawah(self):
        for j in range(len(self.d)):
            # maksimasi daur ulang
            # self.ub.append(self.s[j] * self.t[j] if self.d[j] * self.m[j] >= self.s[j] * self.t[j] else self.d[j] * self.m[j])
            # self.lb.append(0)

            # minimasi kayu segar
            self.ub.append(self.d[j])
            self.lb.append(self.d[j] - round(self.d[j] * self.m[j] if self.s[j] * self.t[j] >= self.d[j] * self.m[j]
                                            else self.s[j] * self.t[j]))

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
            sum = 0
            bit = 0
            for j in range(len(self.d)):
                ba = self.ub[j]
                bb = self.lb[j]
                variabelJ = self.desimalKeVariabel(desimal=int(kromosom[bit:bit+self.bit[j]], 2),
                                                          batas_atas=ba,
                                                          batas_bawah=bb,
                                                          bit=self.bit[j])
                sum += round(variabelJ)
                bit += self.bit[j]
            self.fitness.append(sum)

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

    print("Jumlah kayu segar yang dipakai : ", min(GA.fitness))
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