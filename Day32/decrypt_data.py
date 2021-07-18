from cryptography.fernet import Fernet
from pathlib import Path
import os

def load_key():
    return open('key.key', 'rb').read()

def decript_data(data, fernet):
    decrypted = fernet.decrypt(data)
    return decrypted

key = load_key()
fernet = Fernet(key)

BASE_DIR = Path(__file__).resolve().parent
files = os.listdir(BASE_DIR)


black_list_files = ['key.key', 'ransomware.py', 'decrypt_data.py']
for filename in files:
    if filename not in black_list_files:
        with open(filename, 'rb') as file:
            data = file.read()
        decrypted = decript_data(data, fernet)

        with open(filename, 'wb') as file:
            file.write(decrypted)
