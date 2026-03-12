import json
import os
import base64
import random
import string
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from getpass import getpass
from colorama import Fore, Style, init

# ---------- COLOR INIT ----------
init(autoreset=True)

TITLE = Fore.MAGENTA + Style.BRIGHT
MENU = Fore.BLUE + Style.BRIGHT
INFO = Fore.CYAN + Style.BRIGHT
SUCCESS = Fore.GREEN + Style.BRIGHT
WARN = Fore.YELLOW + Style.BRIGHT
ERROR = Fore.RED + Style.BRIGHT

SALT_FILE = "salt.bin"
EMAIL_VAULT = "email_vault.enc"
WEBSITE_VAULT = "website_vault.enc"

# ---------- UTILITY ----------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input(INFO + "\nPress Enter to continue...")

def choose_vault():
    while True:
        clear_screen()
        print(TITLE + """
Select vault:
""" + MENU + """1. Email Vault (high security)
2. Website Vault (normal accounts)
3. Exit
""")
        choice = input("Choose (1-3): ").strip()

        if choice == "1":
            return EMAIL_VAULT, "EMAIL VAULT"
        elif choice == "2":
            return WEBSITE_VAULT, "WEBSITE VAULT"
        elif choice == "3":
            print(INFO + "👋 Exiting program. Goodbye.")
            exit()
        else:
            print(ERROR + "Invalid choice.")
            pause()

# ---------- SECURITY ----------
def get_salt():
    if not os.path.exists(SALT_FILE):
        with open(SALT_FILE, "wb") as f:
            f.write(os.urandom(16))
    return open(SALT_FILE, "rb").read()

def derive_key(master_password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=get_salt(),
        iterations=200000,
    )
    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))

def get_fernet():
    master_password = getpass(INFO + "Enter master password: ")
    return Fernet(derive_key(master_password))

# ---------- VAULT ----------
def load_vault(fernet, vault_file):
    if not os.path.exists(vault_file):
        return []
    with open(vault_file, "rb") as f:
        return json.loads(fernet.decrypt(f.read()).decode())

def save_vault(data, fernet, vault_file):
    with open(vault_file, "wb") as f:
        f.write(fernet.encrypt(json.dumps(data).encode()))

# ---------- PASSWORD GENERATOR ----------
def generate_password(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return ''.join(random.choice(chars) for _ in range(length))

def choose_password():
    p1 = generate_password()
    p2 = generate_password()

    print(INFO + "\nAuto-generated passwords:")
    print("1)", p1)
    print("2)", p2)
    print("3) Enter my own password")

    choice = input("Choose (1/2/3): ").strip()

    if choice == "1":
        return p1
    elif choice == "2":
        return p2
    else:
        return input("Enter your password: ").strip()

# ---------- DUPLICATE CHECK ----------
def find_duplicate(vault, website, username, email):
    for i, e in enumerate(vault):
        if e["website"] == website and e["username"] == username and e["email"] == email:
            return i
    return None

# ---------- MASK PASSWORD ----------
def show_masked_password(password):
    print(" Password:", "*" * 12)
    choice = input(" Press 'v' to view or Enter to continue: ").strip().lower()
    if choice == "v":
        print(INFO + f" Password: {password}")

# ---------- FEATURES ----------
def add_entry(vault, fernet, vault_file):
    clear_screen()
    print(TITLE + "--- Add New Credential ---")

    website = input("Website: ").strip()
    username = input("Username (optional): ").strip()
    email = input("Email (optional): ").strip()
    password = choose_password()
    notes = input("Notes (optional): ").strip()

    entry = {
        "website": website,
        "username": username,
        "email": email,
        "password": password,
        "notes": notes
    }

    idx = find_duplicate(vault, website, username, email)
    if idx is not None:
        vault[idx] = entry
        print(WARN + "\n♻ Duplicate found → entry updated.")
    else:
        vault.append(entry)
        print(SUCCESS + "\n✅ New entry added.")

    save_vault(vault, fernet, vault_file)
    pause()

def search_entry(vault):
    clear_screen()
    key = input("Search keyword: ").lower()
    found = False

    for i, e in enumerate(vault, 1):
        if key in str(e).lower():
            print(INFO + f"\n{i}. {e['website']}")
            print(" Username:", e["username"] or "N/A")
            print(" Email   :", e["email"] or "N/A")
            show_masked_password(e["password"])
            print(" Notes   :", e["notes"] or "N/A")
            found = True

    if not found:
        print(ERROR + "\n❌ No match found.")
    pause()

def list_all(vault):
    clear_screen()
    if not vault:
        print(WARN + "No credentials saved.")
        pause()
        return

    sorted_vault = sorted(vault, key=lambda e: e["website"].lower())
    for i, e in enumerate(sorted_vault, 1):
        print(INFO + f"\n{i}. {e['website']} | {e['email'] or e['username']}")
    pause()

# ---------- UPDATE / DELETE (UNCHANGED LOGIC) ----------
def update_entry(vault, fernet, vault_file):
    clear_screen()
    if not vault:
        print(WARN + "No credentials saved.")
        pause()
        return

    for i, e in enumerate(vault, 1):
        print(f"{i}. {e['website']}")

    try:
        idx = int(input("\nEnter entry number: ")) - 1
        entry = vault[idx]
    except:
        print(ERROR + "❌ Invalid selection.")
        pause()
        return

    clear_screen()
    print(TITLE + "--- Update Credential ---")

    website = input(f"Website [{entry['website']}]: ").strip()
    if website:
        entry["website"] = website

    username = input(f"Username [{entry['username']}]: ").strip()
    if username:
        entry["username"] = username

    email = input(f"Email [{entry['email']}]: ").strip()
    if email:
        entry["email"] = email

    print("\n1) Keep password\n2) Change password")
    if input("Choose: ") == "2":
        entry["password"] = choose_password()

    notes = input(f"Notes [{entry['notes']}]: ").strip()
    if notes:
        entry["notes"] = notes

    save_vault(vault, fernet, vault_file)
    print(SUCCESS + "\n✅ Entry updated.")
    pause()

def delete_entry(vault, fernet, vault_file):
    list_all(vault)
    try:
        idx = int(input("\nEnter entry number to delete: ")) - 1
        del vault[idx]
        save_vault(vault, fernet, vault_file)
        print(WARN + "🗑 Entry deleted.")
    except:
        print(ERROR + "❌ Invalid selection.")
    pause()

# ---------- MAIN ----------
def main():
    try:
        clear_screen()
        fernet = get_fernet()
        vault_file, vault_name = choose_vault()
        vault = load_vault(fernet, vault_file)
    except Exception:
        print(ERROR + "❌ Wrong master password or corrupted vault.")
        return

    while True:
        clear_screen()
        print(TITLE + f"""
==== SECURE PASSWORD ORGANIZER ====
""" + INFO + f"Active vault: {vault_name}\n" + MENU + """
1. Add new credential
2. Search credential
3. List all accounts
4. Update entry
5. Delete entry
6. Clear screen
7. Switch vault
8. Exit
""")

        choice = input("Choose (1-8): ").strip()

        if choice == "1":
            add_entry(vault, fernet, vault_file)
        elif choice == "2":
            search_entry(vault)
        elif choice == "3":
            list_all(vault)
        elif choice == "4":
            update_entry(vault, fernet, vault_file)
        elif choice == "5":
            delete_entry(vault, fernet, vault_file)
        elif choice == "6":
            clear_screen()
        elif choice == "7":
            vault_file, vault_name = choose_vault()
            vault = load_vault(fernet, vault_file)
        elif choice == "8":
            print(INFO + "👋 Vault locked. Goodbye.")
            break
        else:
            print(ERROR + "Invalid choice.")
            pause()

if __name__ == "__main__":
    main()

