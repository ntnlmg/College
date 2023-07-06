import ast
import random
import PySimpleGUI as psg


def is_prime(x):  # fungsi untuk mengecek bilangan prima. x disini adalah variable prime
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def find_alpha(plaintext, p, q):  # fungsi untuk mencari alpha
    alfa = []
    rule1 = []
    rule2 = []

    for _ in range(len(plaintext)*2):
        alfa.append(_+1)
        for i in range(len(alfa)):
            a2 = (alfa[i]**2) % p  # α2 mod p
            aq = (alfa[i]**q) % p  # αq mod p
            if (aq != 1):  # dicek apakah hasil dari αq mod p = 1, jika = 1 maka akan dihapus/remove dari array
                rule1.append(a2)
                rule2.append(aq)
            else:
                alfa.remove(alfa[i])
    return alfa


def alpha(x, y):  # fungsi untuk memilih alfa mana yang ingin kita gunakan
    print(x, y)
    for _ in range(len(x)):
        if y == x[_]:
            print(x[_])
            return x[_]
    return 0


def find_beta(alfa, p, a):  # fungsi untuk mencari beta
    return alfa ** a % p


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


def decrypt(ciphertext, p, a):  # fungsi untuk mendekripsi
    plaintext = ""
    for item in ciphertext:
        # nilai r dan t diambil dari item menggunakan unpacking. Contohnya item = [2, 101], maka r = 2 & t = 101
        r, t = item
        ra = r ** (p-1-a) % p
        M = t * ra % p
        plaintext += chr(M)
        # char() menukar dari angka ascii ke string alfabet
    return plaintext


def open_txt_file():
    file_path = psg.popup_get_file(
        'Select a .txt file', file_types=(("Text Files", "*.txt"),))
    if file_path:
        try:
            with open(file_path, 'r') as file:
                file_contents = file.read()
            return file_contents
        except Exception as e:
            psg.popup_error(f"Error while opening the file: {str(e)}")
    return None


def save_txt_file(contents):
    file_path = psg.popup_get_file(
        'Save as .txt file', save_as=True, file_types=(("Text Files", "*.txt"),))
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(contents)
            psg.popup(f"File saved successfully at: {file_path}")
        except Exception as e:
            psg.popup_error(f"Error while saving the file: {str(e)}")


psg.set_options(font=('Arial Bold', 20))
psg.theme('DarkBlack1')

layout = [
    [psg.Text('Please enter the Plaintext, Prime number and any number you want!')],
    [psg.Button('Open .txt File'), psg.Input(key='-file-', readonly=True)],
    [psg.Button('Encrypt', button_color=('yellow', 'black')),
     psg.Button('Decrypt', button_color=('yellow', 'black')), psg.Exit(button_color=('yellow', 'black'))]
]

window = psg.Window('Elgamal', layout, size=(1000, 250),
                    enable_close_attempted_event=True)

while True:
    event, values = window.read()

    if event == psg.WINDOW_CLOSE_ATTEMPTED_EVENT and psg.popup_yes_no('Do you really want to exit?', title='Elgamal') == 'Yes':
        break
    if event == psg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Open .txt File':
        file_contents = open_txt_file()
        if file_contents:
            window['-file-'].update(values=file_contents)

    if event == 'Encrypt':
        plaintext = values['-file-']

        if plaintext == '':
            psg.popup('Please select a .txt file.', title='Error')
            continue

        p = int(p)
        a = int(a)
        q = int((p-1) / 2)

        while not is_prime(q):  # mengecek apakah P = bil.prima atau bukan
            p = int(psg.popup_get_text(
                str(p) + ' is not prime, please input another big prime number!', title="ERROR"))
            q = int((p-1) / 2)

        if p == '':
            psg.popup('Please fill in all the required fields.',
                      title='Error')
            continue

        fa = find_alpha(plaintext, p, q)
        ca = psg.popup_get_text(
            fa, title="Choose the alfa you desire!")

        while ca == '' or alpha(fa, int(ca)) == 0:
            if ca == '':
                psg.popup('Please fill in all the required fields.',
                          title='Error')
            else:
                psg.popup('Invalid alpha selected!', title='Error')

            ca = psg.popup_get_text(fa, title="Choose the alfa you desire!")

        alfa = alpha(fa, int(ca))
        beta = find_beta(alfa, p, a)
        result = encrypt(plaintext, alfa, beta, p)
        print(result)
        window['-plain-'].update(str(result))
        # Simpan hasil enkripsi ke dalam file .txt baru
        encrypted_text = str(result)
        save_txt_file(encrypted_text)

    if event == 'Decrypt':
        p = int(values['-p-'])
        a = int(values['-a-'])
        rt = values['-plain-']
        rt = ast.literal_eval(rt)
        result = decrypt(rt, p, a)
        window['-plain-'].update(result)
    if event == psg.WINDOW_CLOSE_ATTEMPTED_EVENT and psg.popup_yes_no('Do you really want to exit?', title='Elgamal') == 'Yes':
        break
    if event == psg.WIN_CLOSED or event == 'Exit':
        break

window.close()
