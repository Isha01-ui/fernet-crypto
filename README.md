# fernet-crypto

A simple Python project using `cryptography.fernet` to encrypt and decrypt text manually.

## Setup

1. Create and activate virtual environment:
python3 -m venv venv
source venv/bin/activate

2. Install dependencies:
pip install -r requirements.txt

## Generate a key (one-time)

Option A (recommended — run once from terminal):
python -c "from cryptography.fernet import Fernet; open('secret.key','wb').write(Fernet.generate_key())"

Option B:
Uncomment `generate_key()` in `crypto_app.py`, run it once, then comment it back.

## Run the app

python crypto_app.py

You will be prompted to choose:
- `e` to encrypt a message
- `d` to decrypt an encrypted token

Example usage:

Encrypt:
Do you want to encrypt or decrypt? (e/d): e
Enter message to encrypt: Hello World
Encrypted: gAAAAABl...   # copy this exact string

Decrypt:
Do you want to encrypt or decrypt? (e/d): d
Enter encrypted text to decrypt: gAAAAABl...
Decrypted: Hello World

⚠️ Do not commit `secret.key` to GitHub.
