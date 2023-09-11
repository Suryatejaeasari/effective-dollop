import math
import random
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
def gdc(a,b):
    while b:
        a,b = b, a%b
    return a
def extended_gcd(a,b):
    if b==0:
        return a,1,0
    else:
        g,x,y = extended_gcd(b,a%b)
        return g,y,x-(a//b)*y
def mod_inverse(a,m):
    g,x,y = extended_gcd(a,m)
    if g!=1:
        return None
    return x%m
def gen_key():
    while True:
        p = random.randrange(2**10, 2**12)
        q = random.randrange(2**10, 2**12)
        if is_prime(p) and is_prime(q):
            break
    n = p*q
    phi = (p-1)*(q-1)
    e = random.randrange(2,phi)
    while gdc(e,phi) !=1:
        e = random.randrange(2,phi)
    d = mod_inverse(e,phi)
    return (e,n), (d,n)

def encrypt(pub_key,plain):
    e,n = pub_key
    return [pow(ord(char),e,n) for char in plain]
def decrypt(priv_key,plain):
    d, n = priv_key
    return ''.join([chr(pow(char, d,n)) for char in plain])

pu, pv = gen_key()
e_msq = encrypt(pu, input())
d_msq = decrypt(pv, e_msq)
print("Encrypted Message:",e_msq)
print("Decrypted Message:",d_msq)
