import ipfsapi

def ipfsFileFunction(filename): 
    api = ipfsapi.connect('127.0.0.1', 5001) 
    ipfsLoadedFile = api.add(filename)
    ipfsHash = (ipfsLoadedFile['Hash'])
    return ipfsHash