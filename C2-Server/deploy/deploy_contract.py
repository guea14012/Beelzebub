from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version

# install และ set version
install_solc('0.8.0')
set_solc_version('0.8.0')

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

with open("c2_contract.sol") as f:
    source = f.read()

compiled = compile_source(source)

contract_id, contract_interface = compiled.popitem()

bytecode = contract_interface['bin']
abi = contract_interface['abi']

account = w3.eth.accounts[0]

C2 = w3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = C2.constructor().transact({
    'from': account
})

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Contract address:", tx_receipt.contractAddress)

import json
with open("abi.json","w") as f:
    json.dump(abi,f)
