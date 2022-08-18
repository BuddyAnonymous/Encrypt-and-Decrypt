import os
from cryptography.fernet import Fernet
import hashlib
import time

list = []
for file in os.listdir('..\\..\\'):
    if file == 'Encrypt.py' or file == 'thekey.key' or file == 'Decrypt.py' or file == 'NotPassword.txt' or file == 'build' or file == 'dist' or file == 'Decrypt.spec':
        continue
    list.append(file)


input = input('What\'s the password?')
textplain = input.encode()
d = hashlib.sha256(textplain)
hashed = d.digest()
with open('..\\..\\dist\\Encrypt\\NotPassword.txt','rb') as password:
    thePassword = password.read()
if hashed == thePassword:

    with open('..\\..\\dist\\Encrypt\\thekey.key','rb') as thekey:
        secretkey = thekey.read()

    for file in list:
        try:
            with open('..\\..\\' + file,'rb') as thefile:
                contents = thefile.read()
                contents_encrypted = Fernet(secretkey).decrypt(contents)
            with open('..\\..\\' + file,'wb') as thefile:
                thefile.write(contents_encrypted)
        except:
            None
    print("Files decrypted!")
else:
    print("Incorrect password!")

time.sleep(5)