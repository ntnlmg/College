import copy

nbits = 128
# Plaintext = input("Please enter the Plaintext: ")
Plaintext = "3243F6A8885A308D313198A2E0370734"
# Key = input("Please enter the Key (max = %d): " % nbits)
Key = "2B7E151628AED2A6ABF7158809CF4F3C"
Round = 2


def fill_array_by_column(n_rows, n_columns, value):
    matrix = []
    x = 0
    for i in range(0, n_rows):
        l = []
        for j in range(0, n_columns):
            l.append(value[x:x + 2])
            x = x + 2
        matrix.append(l)
    return matrix


def AES(Plaintext, Key, nbits, Round):

    matrix_Plaintext = fill_array_by_column(4, 4, Plaintext)
    matrix_Key = fill_array_by_column(4, 4, Key)
    print('\nPlaintext\t', matrix_Plaintext, '\nKey\t\t', matrix_Key, '\nNº bits\t\t', nbits,
          '\nNº round\t', Round, '\n')

    def SubBytes(A):  # replace bits by S-box

        # Table 1. S-box used in AES | 0 1 2 3 4 5 6 7 8 9 a b c d e f
        Sbox = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],  # 0
                ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad',
                    'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],  # 1
                ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34',
                    'a5', 'e5', 'f1', '71', 'd8', '31', '15'],  # 2
                ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07',
                    '12', '80', 'e2', 'eb', '27', 'b2', '75'],  # 3
                ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52',
                    '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],  # 4
                ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a',
                    'cb', 'be', '39', '4a', '4c', '58', 'cf'],  # 5
                ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45',
                    'f9', '02', '7f', '50', '3c', '9f', 'a8'],  # 6
                ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc',
                    'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],  # 7
                ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4',
                    'a7', '7e', '3d', '64', '5d', '19', '73'],  # 8
                ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46',
                    'ee', 'b8', '14', 'de', '5e', '0b', 'db'],  # 9
                ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2',
                    'd3', 'ac', '62', '91', '95', 'e4', '79'],  # a
                ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c',
                    '56', 'f4', 'ea', '65', '7a', 'ae', '08'],  # b
                ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8',
                    'dd', '74', '1f', '4b', 'bd', '8b', '8a'],  # c
                ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61',
                    '35', '57', 'b9', '86', 'c1', '1d', '9e'],  # d
                ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b',
                    '1e', '87', 'e9', 'ce', '55', '28', 'df'],  # e
                ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]  # f

        result = Sbox[int(A[0], 16)][int(A[1], 16)]
        return result

    def RotWordTop(Vector):  # move up lines of a Vector from bottom to top
        aux = Vector[0]
        for i in range(0, len(Vector)-1):
            Vector[i] = Vector[i+1]
        Vector[len(Vector)-1] = aux
        print(Vector)
        return Vector

    def ShiftRows(matrix):  # from right to left
        aux = 0
        for i in range(0, 4):           # column
            for num in range(0, i):      # number of indents to the left of the line
                aux = matrix[0][i]
                for j in range(0, 4-1):  # line
                    matrix[j][i] = matrix[j+1][i]
                matrix[4-1][i] = aux
        return matrix

    def MixColumns(matrix):

        # copy element by element, safe for matrixes and vectors
        R = copy.deepcopy(matrix_Plaintext)
        MatrixMixColumns = [[2, 1, 1, 3],
                            [3, 2, 1, 1],
                            [1, 3, 2, 1],
                            [1, 1, 3, 2]]
        # 3 = (x+1) *(matrix) # polynomial multiplication by Galois field
        # 2 = x *(matrix)
        # 1 = 1 *(matrix)
        for i in range(0, 4):  # line
            k = 0
            for k in range(0, 4):  # repeat multiplication for each column
                result = 0          # decimal result l*c
                for j in range(0, 4):      # column

                    if MatrixMixColumns[j][i] == 3:
                        temp1 = (int(matrix[k][j], 16) << 1) ^ int(
                            matrix[k][j], 16)  # SHIFTLEFT(num,1) XOR num
                    else:
                        temp1 = MatrixMixColumns[j][i] * int(matrix[k][j], 16)
                    if temp1 >= 256:
                        temp1 = (temp1 % 256) ^ 283  # () XOR 1 0001 1011
                    result = result ^ temp1
                    # print('\n', MatrixMixColumns[j][i], matrix[k][j], temp1, '= ', result, '| ')
                result = result % 256
                R[k][i] = format(hex(result)[2:], '0>2')
                # print('==',result,'| ',format(hex(result)[2:], '0>2'))
        return R

    def AddRoundKey(matrix, Key):

        # copy element by element, safe for matrixes and vectors
        R = copy.deepcopy(matrix_Plaintext)
        for i in range(0, 4):
            for j in range(0, 4):
                R[i][j] = format(hex(int(matrix[i][j], 16) ^ int(Key[i][j], 16))[
                                 2:], '0>2')  # XOR
        return R

    def KeySchedule(Key, RoundNum):
       # compose the Rcon[0][0]=RC[Round] of the Round round
        RC = ['01', '01', '02', '04', '08', '10', '20', '40', '80', '1B', '36']

        # copy element by element, safe for matrixes and vectors
        W = copy.deepcopy(Key)
        for i in range(4-1, -1, -1):  # descending
            RotWordTop(W[i])

        # print(W,'\nSubBytes')
        for i in range(0, 4):
            for j in range(0, 4):
                # print('ij ',i,j,'value ',W[i][j][0], W[i][j][1],a,b)
                W[i][j] = SubBytes(W[i][j])
        # print(W, '\Roundcon ultima coluna')

        for i in range(0, 4):  # last column
            if i == 0:
                W[0][i] = format(hex(int(
                    W[len(W) - 1][i], 16) ^ int(Key[0][i], 16) ^ int(RC[RoundNum], 16))[2:], '0>2')
            else:
                W[0][i] = format(hex(int(W[len(W) - 1][i], 16)
                                 ^ int(Key[0][i], 16) ^ 0)[2:], '0>2')
                # print(W[len(W)-1][i], Key[0][i] )

        for i in range(1, 4):  # 1:end
            for j in range(0, 4):
                W[i][j] = format(
                    hex(int(W[i - 1][j], 16) ^ int(Key[i][j], 16))[2:], '0>2')

        print('Key %2d ' % RoundNum, W)
        return W

    # At each round of the encryption algorithm, we perform 4 steps:
    # AddRoundKey, SubBytes, ShiftRows and MixColumns. The first round 0, starts with an AddRoundKey only.
    # In the last round, the MixColumns operation is suppressed.

    # copy element by element, safe for matrixes and vectors
    A = copy.deepcopy(matrix_Plaintext)
    # Round 0 : AddRoundKey step
    key = matrix_Key
    print('Key  0 \t ', key)

    A = AddRoundKey(A, matrix_Key)
    print('AddRoundKey\t', A, '\n')

    for k in range(1, Round + 1):

        # Sub Key Generation
        key = KeySchedule(key, k)

        # encryption: SubBytes step
        for i in range(0, 4):
            for j in range(0, 4):
                A[i][j] = SubBytes(A[i][j])
        print('SubBytes\t', A)

        # encryption : ShiftRows step
        A = ShiftRows(A)
        print('ShiftRows\t', A)

        # encryption: MixColumns step
        if k != Round:
            A = MixColumns(A)
            print('MixColumns\t', A)

        # encryption : AddRoundKey step
        A = AddRoundKey(A, key)
        print('AddRoundKey\t', A, '\n')

    Ciphertext = A
    print('Ciphertext\t', A)
    return A


# Main code
while len(Plaintext) % (nbits//4) != 0:     # fill 32-bit block with '0'
    Plaintext += '0'

for i in range(round(len(Plaintext) / (nbits//4))):
    AES(Plaintext[i * (nbits//4):(i + 1)
        * (nbits//4)], Key, nbits, Round)
    print('--------------------------------------------------------------')
