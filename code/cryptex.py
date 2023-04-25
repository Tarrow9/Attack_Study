import base64
from Crypto import Random
from Crypto.Cipher import AES

key = b"TESTTESTTESTTEST"
print(key)

def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertxt, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertxt, tag

