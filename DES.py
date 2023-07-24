from Crypto.Cipher import DES
from secrets import token_bytes
key = token_bytes(8)
def encrypt(msg):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag
nonce,ciphertext, tag = encrypt(input())
print(f'Cipher Text : {ciphertext}')
