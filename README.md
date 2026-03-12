# Secure Password Organizer CLI

REPOSITORY SETUP GUIDE FOR YOUR FIRST GITHUB PROJECT
Secure Password Organizer CLI

----------------------------------------------------

1. REPOSITORY DESCRIPTION

Secure CLI password manager built with Python that stores credentials in encrypted vault files using master password protection.

This project is intended for learning and personal use.

It should not be used to store highly sensitive production credentials without additional security improvements.


----------------------------------------------------


2. requirements.txt

cryptography
colorama


----------------------------------------------------


3. INSTALLATION

1. Clone the repository

git clone https://github.com/yourusername/password-manager-cli.git


2. Navigate to the project folder

cd password-manager-cli


3. Install dependencies

pip install -r requirements.txt


----------------------------------------------------


4. HOW TO RUN THIS PROJECT ON COMMAND PROMPT

Clone the repo:

git clone https://github.com/yourusername/password-manager-cli.git

Install dependencies:

pip install -r requirements.txt

Run program:

python3 password_manager.py


----------------------------------------------------


5. VAULT FILES

The program automatically creates these files when needed:

salt.bin
email_vault.enc
website_vault.enc

These files store encrypted credentials locally.


----------------------------------------------------


6. TECHNOLOGIES USED

Python 3  
cryptography library  
PBKDF2 key derivation  
SHA256 hashing  
Fernet encryption  
Colorama for CLI colors


----------------------------------------------------


7. FEATURES

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


8. USAGE

Run the program with:

python3 password_manager.py


The program will ask for a master password and then allow you to manage encrypted credentials.


----------------------------------------------------


9. LICENSE (MIT)

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


10. README.md

A secure command-line password manager built with Python that stores credentials in encrypted vaults protected by a master password.

This tool helps you organize and securely store credentials for websites and email accounts locally.


----------------------------------------------------


11. SECURITY

This project uses:

PBKDF2 key derivation
SHA256 hashing
Fernet symmetric encryption

All credentials are stored locally and encrypted.


----------------------------------------------------


12. AUTHOR

Created as a learning project to explore:

Python encryption
CLI application development
Password management systems
