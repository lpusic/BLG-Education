
from web3.auto import w3
from eth_account.messages import encode_defunct

message_hash = '0x45325791ca46a560220cda4141baa4c178be6a1b1deeca5233100c46c697468a'
signature = '0xfdccaf1ada79d69d09af0ad7e90dfddf6128b5d89f77b74080b66d9e3dca9ea32762ac53ba271a4464d401363ee56a0dfa768499a8dbc8867e0cb74210b5e56a1c'
print(w3.eth.account.recoverHash(message_hash, signature=signature))

#Output: 0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E


# Message Hash 0x45325791ca46a560220cda4141baa4c178be6a1b1deeca5233100c46c697468a

# Signature 0xfdccaf1ada79d69d09af0ad7e90dfddf6128b5d89f77b74080b66d9e3dca9ea32762ac53ba271a4464d401363ee56a0dfa768499a8dbc8867e0cb74210b5e56a1c