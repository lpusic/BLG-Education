import web3
from web3.auto import w3
from eth_account.messages import encode_defunct

msg = "biologyPublicKey"
private_key = "0x58ed59957b0dee44ba2e0a2709f20c2a4b6667442c8e149636537dc98e0e5970"
message = encode_defunct(text=msg)
signed_message = w3.eth.account.sign_message(message, private_key=private_key)
print(signed_message)


#a1 = web3.Account.from_key(0x58ed59957b0dee44ba2e0a2709f20c2a4b6667442c8e149636537dc98e0e5970)
