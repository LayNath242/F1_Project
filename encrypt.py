import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from transposition_ipher import EncryptName
import spliter 

def Encrypt_File(file, new_name, delete=False):
    password = b"msipl627rc72677812dhtcdkehgdodh"
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend())

    key = base64.urlsafe_b64encode(kdf.derive(password))
    fer = Fernet(key)
    with open(file, 'rb') as f:
        encrypted_file = fer.encrypt(f.read())
    with open(new_name, 'wb') as f:
        f.write(encrypted_file)
    with open("key.pem", 'wb') as f:
        f.write(key)


file = "myvideo.mp4"
new_name = EncryptName(6, file)
Encrypt_File(file, new_name)
spliter.SplitFile(new_name)
