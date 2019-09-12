import os
import sys
import argparse
import inspect
import ipfshttpclient
from cryptography.fernet import Fernet



def get_argparse():
     parser = argparse.ArgumentParser()

     subparsers = parser.add_subparsers(title="subcommand")

     parser_upload = subparsers.add_parser('upload')
     parser_upload.add_argument("-f","--filename", dest='filename', 
                              help="Enter your file name to encypt , Ex: myfile.ex")
     parser_upload.set_defaults(func=ipfsUpload)

     parser_download = subparsers.add_parser('download')
     parser_download.add_argument("-f", "--filename", dest="filename", 
                              help="Enter your file name than you encypt to decypt, Ex: myfile.ex")
     parser_download.add_argument("-k", "--key", dest="key", 
                              help="Enter Key that you get, Ex: LzYXMHHpKD35eoI0zBwR5XxcMOBi3_fghqnW7AI3Ft0")
     parser_download.set_defaults(func=ipfsDownload)

     args = parser.parse_args()

     arg_spec = inspect.getfullargspec(args.func)
     if arg_spec.varkw:
          args_for_func = vars(args)
     else:
          args_for_func = {k:getattr(args, k) for k in arg_spec.args}
     args.func(**args_for_func)


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
   
def decryptFs(filename,hash, key):
    dataList = []
    for chunkName in hash:
        f = open(str(chunkName), 'rb')
        data = f.read()
        encrypted = Fernet(key).decrypt(data)
        dataList.append(encrypted) 
        f.close()
        os.remove(chunkName)
    f2 = open(os.path.join('./files/',(filename)), 'wb')
    for data in dataList:
        f2.write(data)
    f2.close()

def ipfsFileAdd(filename):
    api = ipfshttpclient.Client()
    ipfsLoadedFile = api.add(filename, recursive=True)
    ipfsHash = (ipfsLoadedFile['Hash'])
    ipfshttpclient.Client.close
    print(ipfsHash)
    return ipfsHash

def ipfsFileget(hash):
    api = ipfshttpclient.Client()
    api.get(hash)

def ipfsDownload(filename, key):
    try:  
        fn1 = filename + "-hash.txt"
        hash = [line.rstrip('\n') for line in open(os.path.join('./files/',fn1))]
        for i in hash:
            ipfsFileget(i)
        decryptFs(filename,hash, key)
        print("Download successes")
    except:
        print("Download fail")

def ipfsUpload(filename):
    try:
        hash = []
        encryptFs(filename)
        for i in range(1,31):
            fn1 = filename + "-%s" % (i)
            # ipfsFileAdd(fn1)
            h = ipfsFileAdd(fn1)
            hash.append(h)
            os.remove(fn1)
        with open(os.path.join("./files/",(filename + '-hash.txt')), 'w') as f:
            for item in hash:
                f.write("%s\n" % item)
        print("Upload successes")
    except:
        for i in range(1,31):
            fn1 = filename + "-%s" % (i)
            os.remove(fn1)
        print("Fail to Upload")

get_argparse()