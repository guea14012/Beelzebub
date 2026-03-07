from web3 import Web3
from cryptography.fernet import Fernet
import json

with open("key.key","rb") as f:
    key = f.read()

cipher = Fernet(key)

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

with open("abi.json") as f:
    abi = json.load(f)

contract_address = "0x0C12Fd4606cb8485b1a3EC363d2E432D570F9d69"

contract = w3.eth.contract(address=contract_address, abi=abi)

account = w3.eth.accounts[0]

cmd = input("Command: ")
target = input("Target: ")

payload = f"{cmd}:{target}"

encrypted = cipher.encrypt(payload.encode())

tx = contract.functions.setCommand(encrypted.decode()).transact({
    "from": account
})
