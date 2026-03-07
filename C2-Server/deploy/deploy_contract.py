from solcx import compile_source
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

with open("soli.sol","r") as f:
    source = f.read()

compiled = compile_source(source)

contract_id, contract_interface = compiled.popitem()

bytecode = contract_interface["bin"]
abi = contract_interface["abi"]

account = w3.eth.accounts[0]

Contract = w3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Contract.constructor().transact({"from": account})

receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Contract deployed at:", receipt.contractAddress)