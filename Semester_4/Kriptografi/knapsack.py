def generate_superincreasing_knapsack(n):
    knapsack = []
    total = 0
    for i in range(n):
        knapsack.append(total + 1)
        total += knapsack[i]
    return knapsack


def encrypt(plain_text, knapsack):
    encrypted = 0
    for i in range(len(plain_text)):
        if plain_text[i] == '1':
            encrypted += knapsack[i]
    return encrypted


def decrypt(encrypted_text, knapsack):
    decrypted = ""
    for i in range(len(knapsack) - 1, -1, -1):
        if encrypted_text >= knapsack[i]:
            decrypted = '1' + decrypted
            encrypted_text -= knapsack[i]
        else:
            decrypted = '0' + decrypted
    return decrypted


# Contoh penggunaan
text = "Hello, world!"
binary_text = ''.join(format(ord(char), '08b') for char in text)

# Membuat knapsack superincreasing dengan panjang sesuai teks biner
knapsack = generate_superincreasing_knapsack(len(binary_text))

# Enkripsi
encrypted_text = encrypt(binary_text, knapsack)
print("Teks terenkripsi:", encrypted_text)

# Dekripsi
decrypted_text = decrypt(encrypted_text, knapsack)
decrypted_text = ''.join(
    chr(int(decrypted_text[i:i+8], 2)) for i in range(0, len(decrypted_text), 8))
print("Teks terdekripsi:", decrypted_text)
