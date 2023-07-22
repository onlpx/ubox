import os
import string
import random

def ranhex(length) -> str:
    return os.urandom(length).hex()

def ranstr(length, charset = (string.ascii_letters + string.digits)) -> str:
    return ''.join(random.choices(charset, k=length))

def ranint(minimum: int, maximum: int) -> int:
    return random.randint(minimum, maximum)

def rhex(length: int) -> str:
    return ranhex(length)

def rstr(length: int, charset: str = (string.ascii_letters + string.digits)) -> str:
    return ranstr(length, charset)

def rint(minimum: int, maximum: int) -> int:
    return random.randint(minimum, maximum)

def rbytes(length: int) -> bytes:
    return os.urandom(length)

def ranbytes(length: int) -> bytes:
    return rbytes(length)