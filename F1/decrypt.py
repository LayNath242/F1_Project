import os, optparse
from cryptography.fernet import Fernet

def get_arguments1():
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

def decryptFs(filename,hash, key):
    dataList = []
    for chunkName in hash:
        f = open(str(chunkName), 'rb')
        data = f.read()
        encrypted = Fernet(key).decrypt(data)
        dataList.append(encrypted) 
        f.close()
        os.remove(chunkName)
    f2 = open(os.path.join('./files/',("decrypt-"+filename)), 'wb')
    for data in dataList:
        f2.write(data)
    f2.close()


def usecmd():
    options = get_arguments1()
    filename = options.filename
    key = options.key
    return filename, key



