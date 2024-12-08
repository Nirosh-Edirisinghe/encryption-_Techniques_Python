import math

def encrypt(plaintext, key):
    ciphertext = ''
    key_index = 0

    plain_len = float(len(plaintext))
    plain_lst = list(plaintext)
    key_lst = sorted(list(key))

    
    col = len(key)
    row = int(math.ceil( plain_len / col))

    fill_null = int((row * col) - plain_len)
    plain_lst.extend('_' * fill_null)

    matrix = [plain_lst[i: i + col]for i in range(0, len(plain_lst), col)]

    
    for _ in range(col):
        current_index  = key.index(key_lst[key_index])
        ciphertext += ''.join([row[current_index]for row in matrix])
        key_index += 1

    return ciphertext



def decrypt(ciphertext, key):
    plaintext = ''
    key_index = 0

    cipher_index = 0
    cipher_len = float(len(ciphertext))
    cipher_lst = list(ciphertext)

    col = len(key)
    row = int(math.ceil(cipher_len / col))

    key_lst = sorted(list(key))
    dec_cipher = []

    for _ in range(row):
        dec_cipher += [[None] * col]

    for _ in range(col):
        current_index = key.index(key_lst[key_index])

        for j in range(row):
            dec_cipher[j][current_index] = cipher_lst[cipher_index]
            cipher_index += 1
        key_index += 1

    try:
        plaintext = ''.join(sum(dec_cipher, []))

    except TypeError:
        raise TypeError("This program cannot","handle repeating words.")

    null_count = plaintext.count('_')

    if null_count > 0:
        return plaintext[: -null_count]  

    return plaintext


print()
print('*** COLUMNAR CIPHER PROGRAM ***')
print()

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = input('Enter the key word: ')
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt(text, key)
    print(f'CHIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = input('Enter the key word: ')
    text = input('Enter the text to decrypt: ')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')
