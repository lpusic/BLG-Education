import web3
privKey = ''
pubKey = ''

file = open('../PrivateKeyFromRetina/privKey.txt','r')
privKey = file.readlines()[0]
privKey.replace('\n', '')
print(privKey)
file.close()

pubKey = web3.Account.from_key(privKey)

file = open('pubKey.txt','w')
file.write(pubKey)
file.close()