import os
from file_ops.splitter import split_file
from crypto.hashing import hash_file
from crypto.encrypt import generate_key, encrypt_data


chunks_dir = "storage/chunks"

key = generate_key()

print("[*] Encryption Key Generated")

for chunk in os.listdir(chunks_dir):

    path = os.path.join(chunks_dir, chunk)

    with open(path, "rb") as f:
        data = f.read()

    nonce, ciphertext, tag = encrypt_data(data, key)

    print(f"[+] {chunk}")
    print("    hash:", hash_file(path))
    print("    encrypted size:", len(ciphertext))
