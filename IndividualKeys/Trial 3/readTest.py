privKey = ""

with open ('test.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
    for myline in myfile:                 # For each line, read it to a string 
    	print(myline)
    	if myline == "Your ETH privkey derived from seed:":
    		print(myline)					#Doesnt do anything, just holds that line
    	else:
    		privKey = myline


print(privKey)								#creates new doc with private key
f = open("privKey.txt", "w")
f.write(privKey)
f.close()