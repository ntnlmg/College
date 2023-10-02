import ast
import random
import PySimpleGUI as psg


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def find_alfa(plaintext, x, y):
    alfa = []
    rule1 = []
    rule2 = []
    for h in range(len(plaintext)*2):
        alfa.append(h+1)
        for i in range(len(alfa)):
            newrule1 = (alfa[i]**2) % x
            newrule2 = (alfa[i]**y) % x
            if (newrule2 != 1):
                rule1.append(newrule1)
                rule2.append(newrule2)
            else:
                alfa.remove(alfa[i])
    return alfa


def newalfa(x, y):
    y = y
    print(x, y)
    for _ in range(len(x)):
        if (y == x[_]):
            newalfa = x[_]
    return newalfa


def find_beta(alfa, x, y):
    return alfa ** x % y


def encrypt(plaintext, alfa, beta, x):
    res = []
    for _ in range(len(plaintext)):
        k = random.randint(1, len(plaintext)*2)
        r = alfa ** k % x
        t = beta ** k * ord(plaintext[_]) % x
        inner_res = [r, t]
        res.append(inner_res)
    return res


def decrypt(data, x, y):
    plaintext = ""
    for item in data:
        r, t = item
        print(r, ", ", t)
        ra = r ** (p-1-y) % x
        M = t * ra % x
        plaintext += chr(M)
    return plaintext

# Programmm


plaintext = str(input('Input plaintext: ')).upper()
p = int(input("Big prime number: "))
a = int(input("Any Number you want: "))
q = int((p-1) / 2)

while not is_prime(q):  # mengecek apakah P = bil.prima atau bukan
    p = int(psg.popup_get_text(
        str(p) + ' is not prime, please input another big prime number!', title="ERROR"))
    q = int((p-1) / 2)

alfa = find_alfa(plaintext, p, q)
print("Choose the alfa you desire!", alfa)

ca = int(input("Any the alpha you want: "))
nwalfa = newalfa(alfa, ca)
beta = find_beta(nwalfa, a, p)
result = encrypt(plaintext, nwalfa, beta, p)
print(result)

p = int(input("Big prime number: "))
a = int(input("Any Number you want: "))
result = ast.literal_eval(input("Ciphertext: "))
ciphertext = decrypt(result, p, a)
print(ciphertext)
