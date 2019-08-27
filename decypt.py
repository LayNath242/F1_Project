from cryptography.fernet import Fernet
import os
import sys
import optparse
sys.path.append("./myModules/")
from myModules.joiner import JoinFiles
from myModules.transposition_ipher import DecryptName, EncryptName


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-f", "--filename", dest="filename", 
                    help="Enter your file name than you encypt to decypt, Ex: myfile.ex")

    parser.add_option("-k", "--key", dest="key", 
                    help="Enter Key that you get, Ex: LzYXMHHpKD35eoI0zBwR5XxcMOBi3_fghqnW7AI3Ft0")
    
    (options, _ )= parser.parse_args()
    if not options.filename:
        parser.error("[-] Please spacify file name, use --help for more info.")
    elif not options.key:
        parser.error("[-] Please spacify key , use --help for more info")
    return options


options = get_arguments()
filename1 = options.filename.replace(" ", "-")
outputname = filename1.lower()
filename2 = EncryptName(6, filename1)
key = options.key

JoinFiles(filename2, 34)
with open(filename2, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)
os.remove(filename2)
with open(outputname + "_decypt", 'wb') as f:
    f.write(encrypted)

