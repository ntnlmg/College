# Tsukamoto #

# Marvin Adinata - 312110009
# Natanael Missionday Gloryant - 312110010

# Mode Input manual
# in_persediaan = input("Persediaan")
# in_permintaan = input("Permintaan")
# in_harga_produksi = input("Harga Produksi")
# persediaan = int(in_persediaan)
# permintaan = int(in_permintaan)
# harga_produksi = int(in_harga_produksi)

persediaan = 125
permintaan = 380
harga_produksi = 700

rules = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1]
]

myu_persediaan = [0, 0]
myu_permintaan = [0, 0]
myu_harga_produksi = [0, 0]
arr_min = [2, 2, 2, 2, 2, 2, 2, 2]
arr_z = [0, 0, 0, 0, 0, 0, 0, 0]
z_up = 0
z_bot = 0
harga_jual = 0

if (persediaan > 100 and persediaan < 300):
    myu_persediaan[0] = (300 - persediaan) / (300 - 100)
    myu_persediaan[1] = (persediaan - 100) / (300 - 100)
elif (persediaan <= 100):
    myu_persediaan[0] = 1
    myu_persediaan[1] = 0
elif (persediaan >= 300):
    myu_persediaan[0] = 0
    myu_persediaan[1] = 1

if (permintaan > 100 and permintaan < 500):
    myu_permintaan[0] = (500 - permintaan) / (500 - 100)
    myu_permintaan[1] = (permintaan - 100) / (500 - 100)
elif (permintaan <= 100):
    myu_permintaan[0] = 1
    myu_permintaan[1] = 0
elif (permintaan >= 500):
    myu_permintaan[0] = 0
    myu_permintaan[1] = 1

if (harga_produksi > 600 and harga_produksi < 1000):
    myu_harga_produksi[0] = (1000 - harga_produksi) / (1000 - 600)
    myu_harga_produksi[1] = (harga_produksi - 600) / (1000 - 600)
elif (harga_produksi <= 600):
    myu_harga_produksi[0] = 1
    myu_harga_produksi[1] = 0
elif (harga_produksi >= 1000):
    myu_harga_produksi[0] = 0
    myu_harga_produksi[1] = 1

print("myu persediaan sedikit = ", myu_persediaan[0])
print("myu persediaan banyak = ", myu_persediaan[1])
print("myu permintaan sedikit = ", myu_permintaan[0])
print("myu permintaan banyak = ", myu_permintaan[1])
print("myu harga_produksi murah = ", myu_harga_produksi[0])
print("myu harga_produksi mahal = ", myu_harga_produksi[1])

print("Rulesnya : ")
print("Persediaan ", "Permintaan ", "Harga Produksi", "Harga Jual")
for i in range(len(rules)):
    for j in range(len(rules[i])):
        print(rules[i][j], end="\t\t")
    print()

for i in range(len(rules)):
    arr_min[i] = min(myu_persediaan[rules[i][0]], myu_permintaan[rules[i][1]], myu_harga_produksi[rules[i][2]])
    print(arr_min[i], end=" ")
    if (rules[i][3]):
        arr_z[i] = arr_min[i] * 1000 + 1000
    else:
        arr_z[i] = 2000 - arr_min[i] * 1000
    
    z_up += arr_min[i] * arr_z[i]
    z_bot += arr_min[i]
    print("Z", i+1, " = ", arr_z[i])

z = z_up / z_bot
print("Z Total = ", z)