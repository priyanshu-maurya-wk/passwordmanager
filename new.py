from cryptography.fernet import Fernet
key = Fernet.generate_key()
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