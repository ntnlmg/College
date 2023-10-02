import csv

with open('D:\Coding\Sem 4\PemodelanSimulasi\ByCGPT\LCG_CGPT.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)

    def lcg(x, a, c, m, i, b):
        list = []
        for _ in range(i):
            n = (a * x + c) % m
            n = round(n / float(m-1), 1)
            print(n)
            while n < b:
                n = (a * n + c) % m
                n = round(n / float(m - 1), 1)
                print(n)
            list.append(n)
            x = n

        cycle = 0
        for check1 in range(i):
            for check2 in range(i):
                if (check1 != check2):
                    if (check1 != check2 and list[check1] == list[check2]):
                        cycle += 1

        print(list)
        writer.writerow(list)
        print("n:", len(list), " Cycle:", cycle)

    lcg(15, 75, 74, 2 ** 8 + 1, 30, 0.1)
