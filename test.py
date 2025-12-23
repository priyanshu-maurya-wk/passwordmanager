from cryptography.fernet import Fernet
user = input("Enter whatever: ")
key = Fernet.generate_key()
cipher_suite = Fernet(key)
encoded_text = cipher_suite.encrypt(user.encode())
print(encoded_text)

user2 = input("Enter the key: ")
decoded_text = cipher_suite.decrypt(user2).decode()
print(decoded_text)