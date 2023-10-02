import math
import csv

# Erlang
with open('Erlang.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)

    def lcg(x, a, c, m, i):
        List = []
        List.append(round(x/m, 5))
        for iterasi in range(i-1):
            x = (a*x+c) % m
            r = round(x / m, 5)
            List.append(r)
        return List

    def randErlang(b, m):
        tocsv = []
        listExp = []
        uniform = lcg(15, 75, 74, 2**16 + 1, 10000+m)
        for i in range(0, len(uniform), m):
            u = 1
            for j in range(m):
                u *= 1-uniform[i+j]
                # print(i, " : " ,j+i)
                # print(u)
            x = round(-(b/m) * math.log(u, math.e), 5)
            strX = str(x)
            listExp.append(strX)
            # writer.writerow(x)
            tocsv.append(x)
            # print(x, end=' ')
        writer.writerow(tocsv)

    randErlang(1, 2)
