import math, pyperclip


def EncryptName(key, file):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(file):
            ciphertext[col] += file[pointer]
            pointer += key
    return ''.join(ciphertext)


def DecryptName(key, file):
    numOfColumns = math.ceil(len(file) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(file)
    plaintext = [''] * numOfColumns
    col = 0
    row = 0
    for symbol in file:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)
