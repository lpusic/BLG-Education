import web3
from web3.auto import w3
from eth_account.messages import encode_defunct

privKey = ''

def sign(privateKey, msg):
	msg = msg
	private_key = privateKey
	message = encode_defunct(text=msg)
	signed_message = w3.eth.account.sign_message(message, private_key=private_key)
	print(signed_message)

def getPrivate():
	file = open('../Keys/PrivateKeyFromRetina/privKey.txt','r') #Opens file that contains just private key
	privKey = file.readlines()[0]						   #reads in the first line of the file, the private key
	privKey.replace('\n', '')							   #cut off the /n at the end of the private key
	file.close()

getPrivate()
print(privKey)
sign(privKey,"test")
#a1 = web3.Account.from_key(0x58ed59957b0dee44ba2e0a2709f20c2a4b6667442c8e149636537dc98e0e5970)
