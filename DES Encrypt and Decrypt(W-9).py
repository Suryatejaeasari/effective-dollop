from Crypto.Cipher import DES
from secrets import token_bytes
key = token_bytes(8)
def encrypt(msg):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext,tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext,tag
nonce, ciphertext,tag = encrypt(input())
def decrypt(nonce,  ciphert, tag):
    cipher = DES.new(key,DES.MODE_EAX, nonce = nonce)
    pain = cipher.decrypt(ciphert)
    try:
        cipher.verify(tag)
        return pain.decode('ascii')
    except:
        return False
print("Encrypted Message:",ciphertext)
plain = decrypt(nonce, ciphertext, tag)
print("Decrypted Message:",plain)
