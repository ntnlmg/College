array = [24, 11, 25, 9, 23, 17, 4, 17, 5, 19, 7, 17, 5, 25]
for i in range(14):
    b = (5 + (i+1))
    c = (array[i]-b)
    r = c % 26
    print(b, '\t', c, '\t', r, "\t i  = ", i)
