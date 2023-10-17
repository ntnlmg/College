d = [3475, 1223, 2260, 2700, 2950]
m = [1, 0.53, 0.5, 0.6, 0.7]
s = [4000, 1600, 1000, 990, 2800]
t = [0.85, 0.9, 0.85, 0.85, 0.9]

# Inisialisasi daftar ub dan lb
ub = []
lb = []

# Menghitung ub dan lb untuk setiap elemen dalam daftar d
for j in range(len(d)):
    # Menghitung ub
    ub.append(d[j])

    # Menghitung lb
    lb.append(d[j] - round(d[j] * m[j] if s[j] *
              t[j] >= d[j] * m[j] else s[j] * t[j]))
    print()
    print("a", d[j] * m[j])
    print("b", s[j] * t[j])
    print("c", d[j] - (d[j] * m[j]))
    print("d", d[j] - (s[j] * t[j]))
# Menampilkan hasil ub dan lb
print("Batas Atas (ub):", ub)
print("Batas Bawah (lb):", lb)
