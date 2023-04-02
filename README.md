# RsaEncryptionAndDecryption  
  
    To run
    
    
    python3 -e file_to_save_ecnrypted_message file_with_plain_text_message  

    python3 -d file_with_ecnrypted_message file_to_save_plain_text_message  
    
    -e or -d to indicate whether to encrypt or decrypt the file  

 This project helps in encrypting data with a public key and decrypting with private key

 It uses the Crypto library to generate RSA keys, encrypt data with AES, and encrypt the AES key with RSA. The resulting encrypted data and keys are then saved to files.

When the script is run, it expects three command-line arguments:



The path to the input file  

The path to the output file  

If the operation argument is -e, the script generates RSA keys, encrypts the input file with AES, and then encrypts the AES key with RSA. The encrypted data is saved to the output file.

If the operation argument is -d, the script decrypts the AES key using the private RSA key, then uses the decrypted key to decrypt the input file with AES. The decrypted data is saved to the output file.
  
  
If the operation argument is not recognized, the script prints an error message.

Note that the script uses a fixed AES key (b'Sixteen byte key'), which is not secure. In a real application, you would want to generate a random key for each encryption operation.


The Crypto library is a Python library that provides various cryptographic functions and algorithms, including symmetric and asymmetric encryption, digital signatures, and hashing. In this code, we use it to generate RSA keys, encrypt data with AES, and encrypt the AES key with RSA.

The AESEncryption class is the main class that performs the encryption and decryption operations. When an instance of this class is created, it reads the three command-line arguments (operation, file1, and file2) and stores them as instance variables. The operation argument indicates whether to encrypt or decrypt the file, and file1 and file2 are the paths to the input and output files, respectively.

The createKeys method generates an RSA key pair with a length of 2048 bits. It then exports the public and private keys to two separate files (publicKey.pem and privateKey.pem).

The encrypt method reads the contents of the input file (file2) and pads the data with a block size of 16 bytes (the AES block size). It then encrypts the padded data with AES using the AES key (self.aes_key). After that, it imports the public RSA key from publicKey.pem and uses it to encrypt the AES key with RSA. The resulting encrypted data and key are then saved to the output file (file1).

The decrypt method reads the encrypted data from the input file (file1) and imports the private RSA key from privateKey.pem. It then uses the private key to decrypt the AES key, which was encrypted with RSA. The decrypted AES key is used to decrypt the data with AES. The decrypted data is then saved to the output file (file2).

Finally, the AESEncryption() statement at the end of the code creates an instance of the AESEncryption class, which triggers the encryption or decryption operation based on the operation argument. If the operation argument is not recognized, the script prints an error message.

I hope this provides a more detailed explanation of the code! Let me know if you have any other questions.
And feel free to raise any issues or forking the project
