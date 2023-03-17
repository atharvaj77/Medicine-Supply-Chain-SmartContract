from datetime import datetime
import json
from web3 import Web3
from datetime import datetime
from hexbytes import HexBytes

abi_edi = '''[
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "item_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "time_stamp",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "mfg_date",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "expiry_date",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "batch_no",
				"type": "string"
			}
		],
		"name": "createHash",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "item_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "time_stamp",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "mfg_date",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "expiry_date",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "batch_no",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "numOfItem",
				"type": "uint256"
			}
		],
		"name": "createProduct",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "_messageHash",
				"type": "bytes32"
			}
		],
		"name": "getEthSignedMessageHash",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "productId",
				"type": "uint256"
			}
		],
		"name": "getProductDetails",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "timestamp",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "itemName",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "mfgDate",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "expiryDate",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "batchNo",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "numberOfItem",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "productId",
						"type": "uint256"
					}
				],
				"internalType": "struct Contract_supplychain.Product",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "products",
		"outputs": [
			{
				"internalType": "string",
				"name": "timestamp",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "itemName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "mfgDate",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "expiryDate",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "batchNo",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "numberOfItem",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "productId",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "runningProductId",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]'''

ganach_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganach_url))
# web3 = Web3(Web3.EthereumTesterProvider)
web3.eth.defaultAccount = web3.eth.accounts[0]
#address = web3.toChecksumAddress("0xd9145CCE52D386f254917e481eB44e9943F39138")
contract = web3.eth.contract(address="0x4087Bb7beB5e3DAFd232A05970d9423aDaF202b2", abi=abi_edi)
# contract = web3.eth.contract(abi = abi, bytecode = bytecode )
# print(web3.eth.get_block('latest'))

# print(msg_hash)
# print(type(msg_hash))

# web3.utils.padLeft(web3.utils.hexToBytes(msg_hash), 32)
# msg_hashbytes = HexBytes(msg_hash)
# print(msg_hash.hex())


signer_account = web3.eth.accounts[0]
signer_private = '0x1f03802300a542709b103fc04b631f20e5ae72792b4aa96a9990b4ee39d09d74'
# nonce = web3.eth.getTransactionCount(signer_account)
# tx = {
#     'nonce': nonce+1,
#     'to': web3.eth.accounts[1],
#     'value': web3.toWei(1, 'ether'),
#     'gas': 2000000,
#     'gasPrice': web3.toWei('50', 'gwei')
# }
# msg_hash = contract.functions.getMessageHash(web3.eth.accounts[1],web3.toWei(1,'ether'),"first transaction",nonce).transact()

#get transaction hash
# print(web3.toHex(tx_hash))


# verifyer_acc = web3.eth.accounts[1]
# print(web3.eth.accounts[0].verify(signed_tx, msg_hash))



def settime():
        now="prateek"
    #  print(now)
        tx_hash = contract.functions.setTimeStamp(now).transact()
        return tx_hash


def gettime():
    time = contract.functions.getTimeStamp().call()
    # time = contract.caller().getTimeStamp()
    return time

def create_product(
            timeStamp, itemName, mfgDate, expiryDate, batchNo, numberUnits
):
      contract.functions.createProduct(
            itemName,
            timeStamp,
            mfgDate,
            expiryDate,
            batchNo,
            numberUnits
	  ).transact()


      productId = contract.functions.createProduct(
            itemName,
            timeStamp,
            mfgDate,
            expiryDate,
            batchNo,
            numberUnits
	  ).call()
      
      return productId
      
def get_product(productId):
      #contract.functions.getProductDetails(productId).transact()
      productData = contract.functions.products(productId).call()
      return productData

      
      
      



# hash = settime()
# time = gettime()
# tx_receipt = web3.eth.wait_for_transaction_receipt(hash)
# print(tx_receipt.contractAddress)
# time = gettime()
#print(hash)
# print(time)






