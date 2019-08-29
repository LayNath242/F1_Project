import ipfshttpclient

api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

def ipfsFileFunction(filename): 
    ipfsLoadedFile = api.add(filename)
    ipfsHash = (ipfsLoadedFile['Hash'])
    return ipfsHash

def ipfsFileget(hash):
    api.get(hash)