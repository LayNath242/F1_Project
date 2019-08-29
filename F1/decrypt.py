import os, optparse
from cryptography.fernet import Fernet
from transposition_ipher import DecryptName , EncryptName

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


def get_arguments2():
    parser = optparse.OptionParser()
    parser.add_option("-f", "--filename", dest="filename", 
                    help="Enter your file name than you encypt to decypt, Ex: myfile.ex")

    parser.add_option("-k", "--key", dest="key", 
                    help="Enter Key that you get, Ex: LzYXMHHpKD35eoI0zBwR5XxcMOBi3_fghqnW7AI3Ft0")
    
    parser.add_option("-i", "--inputDir", dest="inputDir", 
                    help="Enter directory of you want to input ")

    parser.add_option("-o", "--outputDir", dest="outputDir", 
                    help="Enter directory of you want to output ")
    
    (options, _ )= parser.parse_args()
    if not options.filename:
        parser.error("[-] Please spacify file name, use --help for more info.")
    elif not options.key:
        parser.error("[-] Please spacify key , use --help for more info")
    elif not options.inputDir:
        parser.error("[-] Please spacify Input Dierectory , use --help for more info")
    elif not options.outputDir:
        parser.error("[-] Please spacify Output Dierectory , use --help for more info")
    return options


def decryptFs(filename, key):
    dataList = []
    noOfChunks = 30
    j = 0
    for _ in range(0, noOfChunks, 1):
        j += 1
        chunkName = "%s-chunk-%s-Of-%s" % (filename, j, noOfChunks)
        f = open(os.path.join('./files/encryptFs',chunkName), 'rb')
        data = f.read()
        encrypted = Fernet(key).decrypt(data)
        dataList.append(encrypted) 
        f.close()
    filename = DecryptName(5, filename)
    f2 = open(os.path.join('./files/',("decrypt-"+filename)), 'wb')
    for data in dataList:
        f2.write(data)
    f2.close()


def decryptFsFromDir(filename, key, inputdir, outputDir):
    dataList = []
    noOfChunks = 30
    j = 0
    for _ in range(0, noOfChunks, 1):
        j += 1
        chunkName = "%s-chunk-%s-Of-%s" % (filename, j, noOfChunks)
        f = open(os.path.join(inputdir,chunkName), 'rb')
        data = f.read()
        encrypted = Fernet(key).decrypt(data)
        dataList.append(encrypted) 
        f.close()
    filename = DecryptName(5, filename)
    f2 = open(os.path.join(outputDir,("decrypt-"+filename)), 'wb')
    for data in dataList:
        f2.write(data)
    f2.close()


def usecmd():
    options = get_arguments1()
    filename = options.filename
    filename = EncryptName(5, filename)
    key = options.key
    return filename, key


def usecmdDir():
    options = get_arguments2()
    filename = options.filename
    filename = EncryptName(5, filename)
    key = options.key
    inputdir = options.inputDir
    outputDir = options.outputDir
    return filename, key, inputdir, outputDir

