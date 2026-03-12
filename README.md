# password-manager-cli
A secure command-line password manager written in Python that stores website and email credentials in encrypted vault files using a master password.

# Secure Password Organizer CLI

A local encrypted password manager built with Python.

## Features
- Master password protection
- Encrypted vault storage
- Email vault and website vault
- Password generator
- Duplicate detection
- Search credentials
- Update and delete credentials

## Installation

Clone the repository

git clone https://github.com/yourusername/password-manager-cli.git

Install dependencies

pip install -r requirements.txt

Run the program

python password_manager.py

## Security

Encryption uses:
- PBKDF2 key derivation
- SHA256 hashing
- Fernet encryption

## License

MIT
