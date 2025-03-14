import bcrypt
from jinja2.compiler import has_safe_repr


def hash_password(password:str):
    salt = bcrypt.gensalt()
    print(salt)
    hashed = bcrypt.hashpw(password.encode(), salt)
    print(hashed)
    return hashed


def check_password(password:str, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)
hashed_password = hash_password("AlexHome2010")
print(check_password("AlexHome2010", hashed_password))