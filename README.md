# fernet-crypto

A simple Python project using cryptography.fernet to encrypt and decrypt text.

## Setup

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Generate a key (one-time)
Option A (recommended):
python -c "from cryptography.fernet import Fernet; open('secret.key','wb').write(Fernet.generate_key())"

Option B:
Uncomment generate_key() in crypto_app.py, run once, then comment it back.

## Run the app
python crypto_app.py

You should see:
Encrypted: b'gAAAAAB...'
Decrypted: Cybersecurity is fun!

Do not commit secret.key to GitHub.
