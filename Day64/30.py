'''
*Encriptación*
Encriptar y desencriptar frases usando la clave MURCIELAGO. Cada letra de la frase que coincida con alguna 
letra de la clave se sustituye por un número siguiendo el orden 0123456789.
'''

key = {0: 'M', 1: 'U', 2: 'R', 3: 'C', 4: 'I',
       5: 'E', 6: 'L', 7: 'A', 8: 'G', 9: 'O'}

def encrypt(text, key):
    text = list(text.upper())
    for i in range(len(text)):
        for x in range(10):
            if text[i].upper() == key.get(x):
                text[i] = str(x)
    return ''.join(text)

def decrypt(text, key):
    text_code = ''
    for i in list(text.upper()):
        try:
            if int(i) in key:
                text_code += str(key[int(i)])
        except:
            text_code += i

    return text_code
    
texto_encriptado = encrypt('Hola mundo', key)
texto_decriptado = decrypt(texto_encriptado, key)

print(texto_encriptado)
print(texto_decriptado)
