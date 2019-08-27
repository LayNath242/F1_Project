from cryptography.fernet import Fernet
from transposition_ipher import DecryptName
import os
from joiner import joinFiles

key = b'sEHVm2fH-O7ndw2gzseVC3LJ3cXLoA4ZD2GjQfU8vDk='
input_file = 'moy.vmipd4e'
output_file = DecryptName(6, input_file)

joinFiles(input_file, 30)
with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)
os.remove(input_file)

with open(output_file + "_temp", 'wb') as f:
    f.write(encrypted)