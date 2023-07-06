# Sugeno #

# Marvin Adinata - 312110009
# Natanael Missionday Gloryant - 312110010

persediaan = 125
permintaan = 380
harga_produksi = 700

rules = [
    [0, 0, 0, 0],
    [0, 1, 0, 2],
    [1, 0, 0, 0],
    [1, 1, 0, 2],
    [0, 0, 1, 2],
    [0, 1, 1, 3],
    [1, 0, 1, 1],
    [1, 1, 1, 2]
]

myu_persediaan = [0, 0]
myu_permintaan = [0, 0]
myu_harga_produksi = [0, 0]
arr_min = [2, 2, 2, 2, 2, 2, 2, 2]
arr_z = [0, 0, 0, 0, 0, 0, 0, 0]
z_up = 0
z_bot = 0
harga_jual = 0
z = 0

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

print("Rulesnya : ")
print("Persediaan ", "Permintaan ", "Harga Produksi", "Harga Jual")
for i in range(len(rules)):
    for j in range(len(rules[i])):
        print(rules[i][j], end="\t\t")
    print()

print("Nilai Z : ")
for i in range(len(rules)):
    arr_min[i] = min(myu_persediaan[rules[i][0]], myu_permintaan[rules[i][1]], myu_harga_produksi[rules[i][2]])
    # print(arr_min[i])
    if (rules[i][3] == 0): # low profit
        # print(rules[i][3])
        arr_z[i] = harga_produksi
    elif (rules[i][3] == 1): # medium profit
        # print(rules[i][3])
        arr_z[i] = harga_produksi + (permintaan + persediaan) / 2
    elif (rules[i][3] == 2): # high profit
        # print(rules[i][3])
        arr_z[i] = (harga_produksi * 1.5) + permintaan
    elif (rules[i][3] == 3): # ultra profit
        # print(rules[i][3])
        arr_z[i] = harga_produksi * 3
    
    z_up += arr_min[i] * arr_z[i]
    z_bot += arr_min[i]
    print("Z", i+1, " = ", arr_z[i])

z = z_up / z_bot
print("Z Total = ", z)