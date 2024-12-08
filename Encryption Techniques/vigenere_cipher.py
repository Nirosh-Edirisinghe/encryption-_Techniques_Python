letters = 'abcdefghijklmnopqrstuvwxyz'

letter_to_index = dict(zip(letters, range(len(letters))))
index_to_letter = dict(zip(range(len(letters)), letters))

def encrypt(plaintext, key):
    ciphertext = ''
    plaintext = plaintext.replace(' ', '').lower()
    split_message = [plaintext[i:i + len(key)] for i in range(0, len(plaintext), len(key))]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(letters)
            ciphertext += index_to_letter[number]
            i += 1
    return ciphertext



def decrypt(ciphertext, key):
    plaintext = ''
    ciphertext = ciphertext.replace(' ', '').lower()
    split_cipher = [ciphertext[i:i + len(key)] for i in range(0, len(ciphertext), len(key))]

    for each_split in split_cipher:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(letters)
            plaintext += index_to_letter[number]
            i += 1
    return plaintext

    
    


print()
print('*** VIGENERE CIPHER PROGRAM ***')
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

