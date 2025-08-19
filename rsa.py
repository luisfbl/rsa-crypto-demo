from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keys(bits=2048):
    key = RSA.generate(bits)
    private_key = key.export_key()
    public_key = key.public_key().export_key()

    return private_key, public_key

def encode(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(message)

def decode(message, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(message).decode()