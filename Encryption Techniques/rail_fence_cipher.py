def encrypt(plaintext, key):
    ciphertext = ''
    matrix = [[''for cols in range(len(plaintext))]for rows in range(key)]
    row = 0
    col = 0
    i = 1
    
    while col < len(plaintext):
        if row + i < 0 or row + i >= key:
            i = i*-1
        matrix[row][col] = plaintext[col]
        row += i
        col += 1

    
    for j in matrix:
        ciphertext += ''.join(j)
        print(j)
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ''
    matrix = [['' for cols in range(len(ciphertext))] for rows in range(key)]
    row = 0
    col = 0
    i = 1
    
    for char in range(len(ciphertext)):
        if row + i < 0 or row + i >= key:
            i = i * -1
        matrix[row][col] = '*'
        row += i
        col += 1
    
    index = 0
    for row in range(key):
        for col in range(len(ciphertext)):
            if matrix[row][col] == '*' and index < len(ciphertext):
                matrix[row][col] = ciphertext[index]
                index += 1

    row = 0
    col = 0
    i = 1

    for char in range(len(ciphertext)):
        if row + i < 0 or row + i >= key:
            i = i * -1
        plaintext += matrix[row][col]
        row += i
        col += 1
    
    return plaintext


print()
print('*** RAIL FENCE CIPHER PROGRAM ***')
print()

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key: '))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt(text, key)
    print(f'CHIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key: '))
    text = input('Enter the text to decrypt: ')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')