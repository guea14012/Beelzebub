from web3 import Web3
import json
import time

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

contract_address = "PUT_CONTRACT_ADDRESS"
abi = json.load(open("abi.json"))

contract = w3.eth.contract(address=contract_address, abi=abi)

last = 0

while True:

    count = contract.functions.commandCount().call()

    if count > last:

        cmd,target = contract.functions.getCommand(last).call()

        print("New command:",cmd)

        if cmd == "scan":
            print("Simulated network scan")

        last +=1

    time.sleep(5)