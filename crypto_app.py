from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to secret.key")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message.encode()).decode()
    return decrypted

if __name__ == "__main__":
    # generate_key()   # keep commented unless you want a new key
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

    if choice == "e":
        msg = input("Enter message to encrypt: ")
        encrypted = encrypt_message(msg)
        print("Encrypted:", encrypted.decode())

    elif choice == "d":
        encrypted_input = input("Enter encrypted text to decrypt: ")
        try:
            decrypted = decrypt_message(encrypted_input)
            print("Decrypted:", decrypted)
        except Exception:
            print("Error: Invalid encrypted text or wrong key.")

    else:
        print("Invalid choice. Type 'e' to encrypt or 'd' to decrypt.")

