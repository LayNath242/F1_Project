import argparse
import sys
import os
import hashlib
from cryptography.fernet import Fernet


def SplitFile(inputFile):
    f = open(inputFile, 'rb')
    data = f.read()
    f.close()

    bytes = len(data)
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
        fn1 = "%s-chunk-%s-Of-%s" % (inputFile, j, noOfChunks)
        f = open(os.path.join("/home/msi/Desktop/Project/Split_FIle",fn1), 'wb')
        f.write(data[i:i + x])
        f.close()
    os.remove(inputFile)
    
