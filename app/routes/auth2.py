import hashlib
import os

def hash_password(password:str, salt):
    hashed = hashlib.sha512(salt + password.encode()).hexdigest()
    print("hashed", hashed)
    return hashed



def check_password(password: str, hashed_password, salt):
    return hashlib.sha512(salt + password.encode()).hexdigest() == hashed_password

def get_salt():
    return os.urandom(64)

salt = get_salt()
print("salt", salt)
hashed_password = hash_password("AlexHome2010", salt)
print(check_password("AlexHome2010", hashed_password, salt))