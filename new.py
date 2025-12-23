from cryptography.fernet import Fernet
import os

def key_file():
    
    file_name = "secret.key"
    if os.path.exists(file_name):
        with open("secret.key", "rb") as key_sec:
            key_data = key_sec.read()
        if not key_data:
                print("Key file was empty. Generating new key...")
                return generate_and_save_key(file_name)
        return key_data
    else:
        return generate_and_save_key(file_name)

def generate_and_save_key(file_name):
    key = Fernet.generate_key()
    # Use "wb" (Write Binary) not "a"
    with open(file_name, "wb") as key_sec:
        key_sec.write(key)
    print(f"Key is saved to {file_name}")
    return key 
        
key = key_file()
cipher_suite = Fernet(key)

print("********* Password Manager *********")

while True:
    
    user = input("\nOptions\n 1. Add Password(Encrypt)\n 2. View Password(Decrypt) \n 3. Exit\n Choose(1/2/3): ")
    
    if user == "1":
        
        app_name = input("For what is Password for like app or site name: ")
        password = input("Enter the password: ")
        
        encoded_text = cipher_suite.encrypt(password.encode())
        
        with open("password.txt", "a") as textfile:
            textfile.write(f"{app_name}|{encoded_text.decode()}\n")

        print("Password encrypted and saved")
        
    elif user == "2":
        
        if not os.path.exists("password.txt"):
            print("No password saved yet")
            continue
        
        with open("password.txt", "r") as f:
            for line in f.readlines():
                try: 
                    data = line.strip().split("|")
                    if len(data) == 2: 
                        app_names, encrypted_password = data
                        decoded_text = cipher_suite.decrypt(encrypted_password.encode()).decode()
                        print(f"App Name: {app_names} | Password: {decoded_text}")
                    
                except Exception as e:
                    print("Error(idk)")
                    

    
    elif user == "3":
        break
    
    else:
        print("Invalid choice!")