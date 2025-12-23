from cryptography.fernet import Fernet
import os

def key_file():
    
    file_name = "secret.key"
    if os.path.exists(file_name):
        with open("secret.key", "rb") as key_sec:
            return key_sec.read()
    else:
        key = Fernet.generate_key()
        with open("secret.key", "a") as key_sec:
            key_sec.write(key)
            print(f"Key is saved to {file_name}")
            return key_sec
        
key = key_file()
cipher_suite = Fernet(key)

while True:
    
    user = input("Do you want to decrypt passowrd or store a passowrd (1/2): ")
    
    if user == "2":
        textfile = open("text.txt", "a")
        password = input("Enter the password: ")
        encoded_text = cipher_suite.encrypt(password.encode())
        textfile.write(password)
        print(encoded_text)
        
    elif user == "1":
        decryptkey = input("Enter the key to decrypt it: ")
        decoded_text = cipher_suite.decrypt(decryptkey).decode()
        print(decoded_text)
         
    else:
        print("Invalid choice!")