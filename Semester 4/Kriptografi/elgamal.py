import ast
import random
import PySimpleGUI as psg


def is_prime(x):  # fungsi untuk mengecek bilangan prima. x disini adalah variable prime
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def find_alpha(plaintext, x, y):  # fungsi untuk mencari alpha
    alfa = []
    rule1 = []
    rule2 = []

    for _ in range(len(plaintext)*2):
        alfa.append(_+1)
        for i in range(len(alfa)):
            a2 = (alfa[i]**2) % x  # α2 mod p
            aq = (alfa[i]**y) % x  # αq mod p
            if (aq != 1):  # dicek apakah hasil dari αq mod p = 1, jika = 1 maka akan dihapus/remove dari array
                rule1.append(a2)
                rule2.append(aq)
            else:
                alfa.remove(alfa[i])
    return alfa


def alpha(x, y):  # fungsi untuk memilih alfa mana yang ingin kita gunakan
    y = y
    print(x, y)
    for _ in range(len(x)):
        if (y == x[_]):
            newalfa = x[_]
        else:
            alpha
    return newalfa


def find_beta(alfa, x, y):  # fungsi untuk mencari beta
    return alfa ** x % y


def encrypt(plaintext, alfa, beta, x):  # fungsi untuk mengenkripsi
    res = []
    for _ in range(len(plaintext)):
        # k dirandom menggunakan fungsi random.randint dengan range dari 1 - panjanganya plaintext^2
        k = random.randint(1, len(plaintext)*2)
        r = alfa ** k % x
        t = beta ** k * ord(plaintext[_]) % x
        inner_res = [r, t]  # memasukkan hasil enkripsi ke dalam array
        res.append(inner_res)
    return res


def decrypt(data, p, a):  # fungsi untuk mendekripsi
    plaintext = ""
    for item in data:
        # nilai r dan t diambil dari item menggunakan unpacking. Contohnya item = [2, 101], maka r = 2 & t = 101
        r, t = item
        ra = r ** (p-1-a) % p
        M = t * ra % p
        plaintext += chr(M)
        # char() menukar dari angka ascii ke string alfabet
    return plaintext

# Programmm


layout = [
    [psg.Text('Please enter the Plaintext, Prime number and any number you want!')],
    [psg.Text('Plaintext\t\t:'), psg.Input(key='-plain-',)],
    [psg.Text('Big prime numb\t:'), psg.Input(key='-p-')],
    [psg.Text('Any number\t:'), psg.Input(key='-a-')],
    [psg.Button('Encrypt'), psg.Input(key='-DECRYPT-'), psg.Button('Decrypt')],
    [psg.Text('Decrypted\t: '), psg.Text(key='-out-')],
    [psg.Exit()]
]

window = psg.Window('Elgamal', layout,  enable_close_attempted_event=True)

while True:
    event, values = window.read()
    print(event, values)
    if event == "Encrypt":
        plaintext = values['-plain-'].upper()
        # .upper mengubah semua karakter dalam string input/plaintext menjadi huruf besar
        p = values['-p-']
        a = values['-a-']

        if plaintext == '' or p == '' or a == '':
            psg.popup('Please fill in all the required fields.', title='Error')
            continue

        p = int(p)
        a = int(a)
        q = int((p-1) / 2)

        while not is_prime(q):  # mengecek apakah P = bil.prima atau bukan
            p = int(psg.popup_get_text(
                str(p) + ' is not prime, please input another big prime number!', title="ERROR"))
            q = int((p-1) / 2)

        findalfa = find_alpha(plaintext, p, q)
        choosen_alfa = psg.popup_get_text(
            str(findalfa), title="Choose the alfa you desire!")

        while choosen_alfa == '':
            psg.popup('Please fill in all the required fields.', title='Error')
            choosen_alfa = psg.popup_get_text(
                str(findalfa), title="Choose the alfa you desire!")
            continue

        choosen_alfa = int(choosen_alfa)

        alfa = alpha(findalfa, choosen_alfa)
        beta = find_beta(alfa, a, p)
        result = encrypt(plaintext, alfa, beta, p)
        print(result)
        psg.popup_scrolled(
            result, title="Result: [r, t]")

    if event == 'Decrypt':
        p = int(values['-p-'])
        a = int(values['-a-'])
        rt = values['-DECRYPT-']
        rt = ast.literal_eval(rt)
        result = decrypt(rt, p, a)
        window['-out-'].update(result)
        # .title mengembalikan format awal kalimat
    if event == psg.WINDOW_CLOSE_ATTEMPTED_EVENT and psg.popup_yes_no('Do you really want to exit?', title='Elgamal') == 'Yes':
        break
    if event == psg.WIN_CLOSED or event == 'Exit':
        break
window.close()
