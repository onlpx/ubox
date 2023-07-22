import base64
import hashlib

# base64
def b64enc(data: bytes) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')

    return base64.b64encode(data).decode('utf-8')

def b64dec(data: str) -> bytes:
    return base64.b64decode(data).decode('utf-8')

def b64encb(data: bytes) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')

    return base64.b64encode(data)

def b64decb(data: str) -> bytes:
    return base64.b64decode(data)

#sha

def sha256(data: bytes) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    return hashlib.sha256(data).hexdigest()

def sha256b(data: str) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')
        
    return hashlib.sha256(data).digest()

def sha512(data: bytes) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    return hashlib.sha512(data).hexdigest()

def sha512b(data: str) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')
        
    return hashlib.sha512(data).digest()

def sha1(data: bytes) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    return hashlib.sha1(data).hexdigest()

def sha1b(data: str) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')
        
    return hashlib.sha1(data).digest()

def md5(data: bytes) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    return hashlib.md5(data).hexdigest()

def md5b(data: str) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')
        
    return hashlib.md5(data).digest()