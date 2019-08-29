import sys, os
sys.path.append("./F1/")
from F1.decrypt import usecmd, decryptFs
from F1.ipfsApi import ipfsFileget

try:
    filename, key = usecmd()
    fn1 = filename + "-hash.txt"
    hash = [line.rstrip('\n') for line in open(os.path.join('./files/',fn1))]
    for i in hash:
        ipfsFileget(i)
    decryptFs(filename,hash, key)
    print("Download successes")
except:
    print("Download fail")

