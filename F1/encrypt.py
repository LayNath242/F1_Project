import argparse, sys, os, hashlib, optparse
from cryptography.fernet import Fernet

def get_arguments1():
    parser = optparse.OptionParser()
    parser.add_option("-f", "--filename", dest="filename", 
                      help="Enter your file name to encypt , Ex: myfile.ex")
    (options, _ )= parser.parse_args()
    if not options.filename:
        parser.error("[-] Please spacify an filename, use --help for more info.")
    return options


def created_folder():
    dirName = "./files/"
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        print("Directory " , dirName ,  " Created ")


def encryptFs(filename):
    key = Fernet.generate_key()
    fer = Fernet(key)
    created_folder()
    with open(os.path.join("./files/",("key-"+filename+".pem")), 'wb') as f:
        f.write(key)
    f = open(filename, 'rb')
    data = f.read()
    f.close()

    bytes = len(data)
    if (bytes < 650):
        bytes = 650
    x = int(bytes * 0.034)

    if sys.version_info.major == 3:
        noOfChunks = int(bytes / x)
    elif sys.version_info.major == 2:
        noOfChunks = bytes / x
    if(bytes % x):
        noOfChunks += 1

    j = 0
    for i in range(0, bytes + 1, x):
        j += 1
        fn1 = "-%s" % (j)
        encrypted_file = fer.encrypt(data[i:i + x])
        fen = filename + fn1
        f = open(fen, 'wb')
        f.write(encrypted_file)
        f.close()
   

def usecmd():
    options = get_arguments1()
    filename = options.filename
    return filename
    


