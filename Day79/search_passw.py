import os
import hashlib

# HolaMundo
hash_pwd = '4960c7d6d1e08730a94c67d18004ac1a47cfe624d267faf06adf024544c7da1d'

dictionari = open(os.path.join(os.path.dirname(__file__),'contraseñas.txt'), 'r')

find = False
for pwd in dictionari:
    hashs = hashlib.sha256(pwd.strip().encode('utf-8')).hexdigest()
    if hashs == hash_pwd:
        print(f"La contraseña es: {pwd}")
        find = True
        break
    
if not find:
    print("La contraseña no ha sido encontrada")
        

