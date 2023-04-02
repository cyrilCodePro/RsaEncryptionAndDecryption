import datetime
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util import Padding
import sys

class AESEncryption:
    def __init__(self) -> None:
        self.operation=sys.argv[1]
        self.file1 = sys.argv[2]
        self.file2 = sys.argv[3]
        self.aes_key = b'Sixteen byte key'
        self.cipher_aes =cipher_aes = AES.new(key=self.aes_key, mode=AES.MODE_CBC, iv=b'\x00'*16)

        if(self.operation == "-e"):
                try:
                    self.createKeys()
                    self.encrypt()
                except Exception as e:
                    print(e)
        elif(self.operation == "-d"):
            try:
                self.createKeys()
                self.decrypt()
            except Exception as e:
                    print(e)
        else:
            print("Invalid operation trigger \n try -e for encrypting \n try -d for decrypting")

    def createKeys(self):
        key = RSA.generate(2048)
        public_key = key.publickey().export_key("PEM")
        private_key = key.export_key("PEM")
        with open("publicKey.pem", "wb") as f:
            f.write(public_key)
        with open("privateKey.pem", "wb") as f:
            f.write(private_key)


    def encrypt(self):
        # encrypt the data with AES
        with open(self.file2,"rb") as file:
            data =file.read()
        padded_data = Padding.pad(data, AES.block_size)
        encrypted_data = self.cipher_aes.encrypt(padded_data)
        # encrypt the AES key with RSA
        public_key = RSA.import_key(open("publicKey.pem").read())
        cipher_rsa = PKCS1_OAEP.new(public_key)
        encrypted_aes_key = cipher_rsa.encrypt(self.aes_key)
        with open(self.file1,"wb") as file:
            file.write(encrypted_data)

    def decrypt(self):
        # decrypt the AES key with RSA
        private_key = RSA.import_key(open("privateKey.pem").read())
        cipher_rsa = PKCS1_OAEP.new(private_key)
        encrypted_aes_key = cipher_rsa.encrypt(self.aes_key)
        decrypted_aes_key = cipher_rsa.decrypt(encrypted_aes_key)
        # decrypt the data with AES
        cipher_aes = AES.new(key=decrypted_aes_key, mode=AES.MODE_CBC, iv=b'\x00'*16)
        with open(self.file1,"rb") as file:
            data = file.read()
        decrypted_data = Padding.unpad(cipher_aes.decrypt(data), AES.block_size)
        with open(self.file2,"w") as file:
            file.write(decrypted_data.decode())

AESEncryption()
