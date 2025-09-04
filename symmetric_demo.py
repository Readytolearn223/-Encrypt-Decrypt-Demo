# symmetric_demo.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Generate a random 16-byte AES key
key = get_random_bytes(16)
print("Symmetric Key (AES):", key.hex())

# Message to encrypt
message = b"Hello, symmetric encryption!"
print("Original Message:", message.decode())

# AES encryption requires a random IV
cipher = AES.new(key, AES.MODE_CFB)
iv = cipher.iv

# Encrypt message
ciphertext = cipher.encrypt(message)
print("Ciphertext (Base64):", base64.b64encode(ciphertext).decode())

# Decrypt message
decipher = AES.new(key, AES.MODE_CFB, iv=iv)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted Message:", decrypted.decode())
