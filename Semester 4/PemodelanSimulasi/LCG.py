import numpy as np
import csv
# LCG
with open('LCG.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)

    def lcg(x, a, c, m, i):
        List = []
        List.append(round(x/m, 5))
        for iterasi in range(i-1):
            x = (a*x+c) % m
            r = round(x / m, 1)
            # rr = str(r)
            List.append(r)

            # writer.writerow(rr)

        # print(r)
        cycle = 0
        for check1 in range(i):
            for check2 in range(i):
                if (check1 != check2):
                    if (List[check1] == List[check2]):
                        cycle += 1
        print(List)
        writer.writerow(List)
        print("The numbers are saved into LCG.csv")
        print("n:", len(List), " Cycle:", cycle)

    lcg(15, 75, 74, 2**8 + 1, 31)
