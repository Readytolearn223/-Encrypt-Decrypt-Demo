# asymmetric_demo.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generate RSA key pair
key_pair = RSA.generate(2048)
private_key = key_pair.export_key()
public_key = key_pair.publickey().export_key()

print("Public Key:\n", public_key.decode())
print("Private Key:\n", private_key.decode())

# Message to encrypt
message = b"Hello, asymmetric encryption!"
print("Original Message:", message.decode())

# Encrypt with public key
cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
ciphertext = cipher.encrypt(message)
print("Ciphertext (Base64):", base64.b64encode(ciphertext).decode())

# Decrypt with private key
decipher = PKCS1_OAEP.new(RSA.import_key(private_key))
decrypted = decipher.decrypt(ciphertext)
print("Decrypted Message:", decrypted.decode())
