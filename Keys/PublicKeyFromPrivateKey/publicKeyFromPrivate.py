
def publicKeyFromPrivate():
	import web3
	privKey = ''
	pubKey = ''

	file = open('../PrivateKeyFromRetina/privKey.txt','r') #Opens file that contains just private key
	privKey = file.readlines()[0]						   #reads in the first line of the file, the private key
	privKey.replace('\n', '')							   #cut off the /n at the end of the private key
	file.close()										   #output a string that equals something like: 
														   # 	"0x900f28ad68709df23c6191617152f0240ecd57760f707ff3bdbd489126db5064"
	pubKey = web3.Account.from_key(privKey)   			   #Spits out 
	print(pubKey)

# file = open('pubKey.','w')
# file.write(pubKey)
# file.close()