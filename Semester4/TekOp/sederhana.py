dj, mj, sj, tj = [float(x) for x in input().split()]
daur_ulang = int(dj*mj if sj*tj>=dj*mj else sj*tj)
kayu_segar = int(dj-daur_ulang)
print("Kertas daur ulang: ", daur_ulang,"\nKertas dari kayu segar: ", kayu_segar)