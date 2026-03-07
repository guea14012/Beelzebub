from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

contract_address = "PUT_CONTRACT_ADDRESS"

abi = json.load(open("abi.json"))

contract = w3.eth.contract(address=contract_address, abi=abi)

account = w3.eth.accounts[0]

def send_command(cmd, target):

    tx = contract.functions.addCommand(
        cmd,
        target
    ).transact({'from':account})

    print("Command stored on blockchain")

send_command("scan","agent1")