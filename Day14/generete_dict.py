from generator import Pass


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
            new_pass = f'{word[:1]}_{word[1:]}'
            new_pass2 = f'{word[:2]}_{word[2:]}'
            largada = len(word)-2
            new_pass3 = f'{word[:largada]}_{word[largada:]}'
            lista = [new_pass, new_pass2, new_pass3]
            for i in lista:
                if i not in variantes[word]:
                    variantes[word].append(i)
    
    # Crear mas vaiantes separando por guiones
    for key, variable in variantes.items():
        lista = []
        for word in variable:
            separate = word.split("_")
            for i in separate:
                if len(i) > 2 and i not in variantes[key]:
                    lista.append(i)
        variantes[key] += lista

    # Substituir letras por numeros
    for key, variable in variantes.items():
        lista = []
        for word in variable:
            for letter in word:
                if letter.upper() in special:
                    word = word.replace(letter, str(special[letter.upper()]))
            lista.append(word)
        variantes[key] += lista
    
    return variantes  


def generate_new_pass(variantes, password):
    nodo_password = Pass(password)
    nodos_frontera = []
    nodo_visitados = []
    
    for key, items in variantes.items():
        for word in items:
            if word != password:
                nodos_frontera.append(Pass(word))
    
    lst_index_ = nodo_password.get_index_char("_")
    print(lst_index_)
    while len(nodos_frontera) != 0:
        new_pass = nodo_password
        while len(lst_index_) != 0 or len(nodos_frontera) != 0:
            for i in lst_index_:
                variante = nodos_frontera.pop(0)
                print(lst_index_)
                if not variante.get_index_char("_"):
                    new_pass.replace_index(i, variante)
                    lst_index_.remove(i)
        print(new_pass)
        break
              

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
variantes = generate_variantes(key_words)

# print(variantes)

for key, items in variantes.items():
    for word in items:
        generate_new_pass(variantes, word)
        break
    break
