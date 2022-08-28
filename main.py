from importlib import import_module
from cryptography.fernet import Fernet as fnet

password = input("enter password: ")

key = fnet.generate_key()

fernet= fnet(key)

encpass= fernet.encrypt(password.encode())

decpass= fernet.decrypt(encpass).decode()

print(encpass)
print("welp")

print(decpass)
