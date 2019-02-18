from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

def encryptdata(message):
   key_text = open("publicKey.pem", "rb").read()

    # Import key using RSA module
   public_key = RSA.importKey(key_text)

    # Generate a cypher using the PKCS1.5 standard
   cipher = PKCS1_v1_5.new(public_key)

    # Encrypy as bytes
   encrypted_bytes = cipher.encrypt(message)

   return base64.b64encode(encrypted_bytes)

def decryptdata(ciphertext):
    key_text=open("privateKey.pem","rb").read()
    private_key=RSA.importKey(key_text)
    cipher = PKCS1_v1_5.new(private_key)
    text=base64.b64decode(ciphertext)
    return cipher.decrypt(text,"decryption error")


data=encryptdata(b"The cool code")
test=decryptdata(data)
print(test)