import sys, os
sys.path.append("./F1/")
from F1.encrypt import usecmd, encryptFs
from F1.ipfsApi import ipfsFileFunction
try:
    hash = []
    filename = usecmd()
    encryptFs(filename)
    for i in range(1,31):
        fn1 = filename + "-%s" % (i)
        ipfsFileFunction(fn1)
        h = ipfsFileFunction(fn1)
        hash.append(h)
        os.remove(fn1)
    with open(os.path.join("./files/",(filename + '-hash.txt')), 'w') as f:
        for item in hash:
            f.write("%s\n" % item)
    print("Upload successes")
except:
    print("Fail to Upload")