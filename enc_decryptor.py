import os
from cryptography.fernet import Fernet
import time
                

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

z = input("Enter folder path to encrypt all txt and docx files:-")
w = input("Enter choice (1.Encrypt 2.Decrypt):-")

if w=="1":
    write_key()
    key = load_key()
    f = Fernet(key)
    for subdir, dirs, files in os.walk(z):
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(".txt") or filepath.endswith(".JPG"):
                if filepath.endswith(".JPG"):
                    os.rename(filepath,filepath.strip(".JGP")+"(JPG).txt")
                    filepath = filepath.strip(".JGP")+"(JPG).txt"
                elif filepath.endswith(".txt"):
                    os.rename(filepath,filepath.strip(".txt")+"(txt).txt")
                    filepath = filepath.strip(".txt")+"(txt).txt"
                c = open(filepath,'rb')
                z = c.read()
                c.close()
                os.remove(filepath)
                encrypted = f.encrypt(z)
                n = open(filepath.strip('.txt')+'.encrypted', 'xb')
                n.write(encrypted)
                n.close()
            
                    
if w=="2":
    key = load_key()
    f = Fernet(key)
    for subdir, dirs, files in os.walk(z):
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(".encrypted") :
                c = open(filepath,'rb')
                zi = c.read()
                c.close()
                os.remove(filepath)
                decrypted = f.decrypt(zi)
                if filepath.endswith("(JPG).encrypted"):
                    n = open(filepath.strip('(JPG).encrypted')+'.JPG', 'wb')
                elif filepath.endswith("(txt).encrypted"):
                    n = open(filepath.strip('(txt).encrypted')+'.txt', 'wb')
                n.write(decrypted)
                n.close()
                
