from cryptography.fernet import Fernet

while True:
    
    user = input("Do you want to decrypt passowrd or store a passowrd (1/2): ")
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    
    if user == "1":
        decoded_text = cipher_suite.decrypt(user).decode()
        print(decoded_text)
        
    elif user == "2":
        textfile = open("text.txt", "a")
        textfile.write(input())
        
    else:
        print("Invalid choice!")