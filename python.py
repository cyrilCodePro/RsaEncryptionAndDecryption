from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util import Padding


class AESEncryption:
    def __init__(self) -> None:
        # generate AES key
        self.aes_key = b'Sixteen byte key'
        # create AES cipher in CBC mode with an initialization vector of all zeroes 
        self.cipher_aes =cipher_aes = AES.new(key=self.aes_key, mode=AES.MODE_CBC, iv=b'\x00'*16)
    # generate RSA key pair and write the keys to files
    def createKeys(self):
        key = RSA.generate(2048)
        public_key = key.publickey().export_key("PEM")
        private_key = key.export_key("PEM")
        with open("publicKey.pem", "wb") as f:
            f.write(public_key)
        with open("privateKey.pem", "wb") as f:
            f.write(private_key)
    def utilities(self):
        pass

    def encrypt(self):
        # encrypt the data with AES
        data = b'This is some data to encrypt'
        padded_data = Padding.pad(data, AES.block_size)
        encrypted_data = self.cipher_aes.encrypt(padded_data)
        # encrypt the AES key with RSA
        public_key = RSA.import_key(open("publicKey.pem").read())
        cipher_rsa = PKCS1_OAEP.new(public_key)
        encrypted_aes_key = cipher_rsa.encrypt(self.aes_key)

    
    def decrypt(self):
        # decrypt the AES key with RSA
        private_key = RSA.import_key(open("privateKey.pem").read())
        cipher_rsa = PKCS1_OAEP.new(private_key)
        encrypted_aes_key = cipher_rsa.encrypt(self.aes_key)

        decrypted_aes_key = cipher_rsa.decrypt(encrypted_aes_key)
        # decrypt the data with AES
        cipher_aes = AES.new(key=decrypted_aes_key, mode=AES.MODE_CBC, iv=b'\x00'*16)
        decrypted_data = Padding.unpad(cipher_aes.decrypt(b'\x9e#\x8d\x0c\xd0\xe5.\x7f\xf6\x185\xdc\xc3cX\xfe"\x14\xc7\xddx\r7D\xd2J\x8aW4[K\x01'), AES.block_size)
        print(decrypted_data)

