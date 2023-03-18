from web3 import Web3
from abi import ABI
import time



ganach_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganach_url))
web3.eth.defaultAccount = web3.eth.accounts[0]
contract = web3.eth.contract(
    address="0x83E938501aAfBeAf2797f05085aC13b44Ea9073b", abi=ABI)

signer_account = web3.eth.accounts[0]

timeStamp = str(time.time())



def create_product(timeStamp, itemName, mfgDate, expiryDate, batchNo, numberUnits):
    nonce = web3.eth.get_transaction_count(signer_account)
    tx = contract.functions.createProduct(
        itemName,
        timeStamp,
        mfgDate,
        expiryDate,
        batchNo,
        numberUnits
    ).buildTransaction({'from': signer_account, 'nonce': nonce})

    signed_tx = web3.eth.account.signTransaction(
        tx, '0x6727e3c0a0187676c78ff449e9ce460ae1b3479b10e71e59a94414865c8033bc')
    hash_txn = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

def last():
    return contract.functions.getLastIndex().call()



def get_product(productId):
    productData = contract.functions.getProductDetails(productId).call()
    return productData


