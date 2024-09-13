from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import secrets


ph = PasswordHasher()


def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)
    hashed_password = ph.hash(
        password=password, 
        salt=salt
    )
    return hashed_password


def verify_password(hash: str, password: str):
    try:
        return ph.verify(hash, password)
    except VerifyMismatchError:
        return False

