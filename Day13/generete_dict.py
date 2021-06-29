lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
special = {
    'A': 4,
    'B': 8,
    'O': 0,
    'S': 5,
    'E': 3,
    'T': 7,
    'Z': 2,
    'I': 1
}
num = '1234567890'
signos = '?-,.=!"·$%&/)('
char = upper + lower + num + signos

def generate_variantes(list_words):
    variantes = {}
    for word in list_words:
        variantes[word] = []
        Len = len(word)
        
        # Forma 1
        new_pass = f"_{word}_"
        variantes[word].append(new_pass)
        
        # Comprovar si es par
        if Len % 2 == 0:
            # Partir variable por la mitad
            mitad = Len // 2
            new_pass = f"{word[:mitad]}_{word[mitad:]}"
            variantes[word].append(new_pass)
            
            # Partir la variable en todas las partes que permite
            controll = 0
            new_pass = ''
            for letra in word:
                controll += 1
                if controll < 2:
                    new_pass += letra
                else:
                    controll = 0
                    new_pass += f"{letra}_"
            variantes[word].append(new_pass)
            
        else:
            pass

    # Substituir letras por numeros
    for key, variable in variantes.items():
        lista = []
        for word in variable:
            for letter in word:
                if letter.upper() in special:
                    word = word.replace(letter, str(special[letter.upper()]))
            lista.append(word)
        variantes[key] += lista
    
    for key, item in variantes.items():
        print(key, item)

    

key_words = []
with open('key_words.txt', 'r') as keys:
    lines = keys.readlines()
    for line in lines:
        if "\n" in line:
            try:
                line = line.replace(" \n", '')
            except:
                line = line.replace("\n", '')
        line = line.split(',')
        key_words += line

print(key_words)
generate_variantes(key_words)
