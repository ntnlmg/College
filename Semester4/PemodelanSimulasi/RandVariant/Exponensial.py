import math
import csv
# print(-b * math.log(1-u,math.e))
# print(-m/b * math.log(1-u1 * 1-u2,math.e))
# print(-1 * math.log(0.618,math.e))

# Exponential
with open('Exponential.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)

    def lcg(x, a, c, m, i):
        List = []
        List.append(round(x/m, 5))
        for iterasi in range(i-1):
            x = (a*x+c) % m
            r = round(x / m, 5)
            List.append(r)
        return List

    def randExponential(b):
        tocsv = []
        listExp = []
        uniform = lcg(15, 75, 74, 2**16 + 1, 10000)
        for i in range(len(uniform)):
            x = round(- b * math.log(1-uniform[i], math.e), 5)
            strX = str(x)
            listExp.append(strX)
            tocsv.append(x)
            # print(x, end=' ')
        writer.writerow(tocsv)

    randExponential(1.083)
