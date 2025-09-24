from cryptography.fernet import Fernet

# Generate a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to secret.key")

# Load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a message
def encrypt_message(message: str) -> bytes:
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

# Decrypt a message
def decrypt_message(encrypted_message: bytes) -> str:
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message).decode()
    return decrypted

if __name__ == "__main__":
    # First run generate_key() once to create the key file
    #generate_key()

    message = "Cybersecurity is fun!"
    encrypted = encrypt_message(message)
    print("Encrypted:", encrypted)

    decrypted = decrypt_message(encrypted)
    print("Decrypted:", decrypted)

