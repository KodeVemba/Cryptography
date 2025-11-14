import modules.hash
from modules.encryption import aes_ed, rsa_ed
from modules.password import check_stregth, hash_pw, verify_pw


def menu():
    print("\n Select operation")
    print("[1] Hash file")
    print("[2] Check file integrity")
    print("[3] AES Encrypt/Decrypt")
    print("[4] RSA Encrypt/ Decrypt")
    print("[5] Password manager")


print("Welcome to the Cryptography toolkit")


while True:
    menu()
    choice = input()
    if choice == 0:
        break
    elif choice == 1:
        file = input("Enter the file path ")
        print(f" The hash of the file is {modules.hash.hash_file(file)}")
    elif choice == 2:
        file1 = input("Input file 1 ")
        file2 = input("Input file 2 ")
    elif choice == 3:
        message = input("what is your message? ")
        print(f"Here is the encryption of your file {aes_ed(message)}")
    elif choice == 4:
        message = input("what is your message? ")
        print(f"Here is the encryption of your file {rsa_ed(message)}")
    elif choice == 5:
        while True:
            password = input("create a password?")
            response = check_stregth(password)
            if response.startswith("stron"):
                break
        hash_pw(password)
