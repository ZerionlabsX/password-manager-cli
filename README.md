REPOSITORY SETUP GUIDE FOR YOUR FIRST GITHUB PROJECT
Secure Password Organizer CLI

----------------------------------------------------

1. REPOSITORY NAME

password-manager-cli


----------------------------------------------------

2. REPOSITORY DESCRIPTION

Secure CLI password manager built with Python that stores credentials in encrypted vault files using master password protection.


----------------------------------------------------

3. FILE STRUCTURE FOR YOUR REPOSITORY

password-manager-cli
│
├── password_manager.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE


----------------------------------------------------

4. requirements.txt

cryptography
colorama


----------------------------------------------------

5. .gitignore

__pycache__/
*.pyc
*.pyo
*.pyd
.env
*.enc
*.bin
.DS_Store
Thumbs.db


----------------------------------------------------

6. LICENSE (MIT)

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software.

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.


----------------------------------------------------

7. README.md

# Secure Password Organizer CLI

A secure command-line password manager built with Python that stores credentials in encrypted vaults protected by a master password.

This tool helps you organize and securely store credentials for websites and email accounts locally.

----------------------------------------------------

FEATURES

• Master password protection  
• Encrypted credential storage  
• Separate Email Vault and Website Vault  
• Search credentials quickly  
• Update stored credentials  
• Delete credentials  
• Duplicate credential detection  
• Auto password generator  
• Alphabetical credential listing  
• Simple and lightweight CLI interface

----------------------------------------------------

TECHNOLOGIES USED

Python 3  
cryptography library  
PBKDF2 key derivation  
SHA256 hashing  
Fernet encryption  
Colorama for CLI colors

----------------------------------------------------

INSTALLATION

1. Clone the repository

git clone https://github.com/yourusername/password-manager-cli.git


2. Navigate to the project folder

cd password-manager-cli


3. Install dependencies

pip install -r requirements.txt


----------------------------------------------------

USAGE

Run the program with:

python password_manager.py


The program will ask for a master password and then allow you to manage encrypted credentials.


----------------------------------------------------

VAULT FILES

The program automatically creates these files when needed:

salt.bin
email_vault.enc
website_vault.enc

These files store encrypted credentials locally.

They are ignored by GitHub using .gitignore.


----------------------------------------------------

SECURITY

This project uses:

PBKDF2 key derivation
SHA256 hashing
Fernet symmetric encryption

All credentials are stored locally and encrypted.


----------------------------------------------------

DISCLAIMER

This project is intended for learning and personal use.
It should not be used to store highly sensitive production credentials without additional security improvements.


----------------------------------------------------

AUTHOR

Created as a learning project to explore:

Python encryption
CLI application development
Password management systems


----------------------------------------------------

8. FILES YOU SHOULD NOT UPLOAD TO GITHUB

salt.bin
email_vault.enc
website_vault.enc

These are user-generated encrypted vault files.


----------------------------------------------------

9. HOW USERS WILL RUN YOUR PROJECT

Clone the repo:

git clone https://github.com/yourusername/password-manager-cli.git

Install dependencies:

pip install -r requirements.txt

Run program:

python password_manager.py


----------------------------------------------------

Your repository will look like this:

password-manager-cli
│
├── password_manager.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

----------------------------------------------------
