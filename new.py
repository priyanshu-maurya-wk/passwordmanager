from cryptography.fernet import fernet

while True:
    user = input("Do you want to decrypt passowrd or store a passowrd (1/2): ")

    if user == "1":
        pass
    elif user == "2":
        textfile = open("text.txt", "a")
        textfile.write(input())
    else:
        print("Invalid choice! Your passowrd is now leaked to internet with all of your information if you stored password before you dumb bitch")