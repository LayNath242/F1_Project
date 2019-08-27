import base64
import os, sys
import optparse
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
sys.path.append("./myModules/")
from myModules import spliter
from myModules.transposition_ipher import EncryptName

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-f", "--filename", dest="filename", 
                      help="Enter your file name to encypt , Ex: myfile.ex")
    (options, _ )= parser.parse_args()
    if not options.filename:
        parser.error("[-] Please spacify an filename, use --help for more info.")
    return options


def Encrypt_File(file, new_name, delete=False):
    password = b"LzYXMHHpKD35eoI0zBwR5XxcMOBi3_fghqnW7AI3Ft0"
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



options = get_arguments()
filename = options.filename
lowecasename = filename.lower()
os.rename(filename, lowecasename.replace(" ", "-"))
file = lowecasename.replace(" ", "-")
new_name = EncryptName(6, file)
Encrypt_File(file, new_name)
spliter.SplitFile(new_name)


