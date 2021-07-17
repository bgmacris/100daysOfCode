from generator import Pass


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
file_ = 'key_words.txt'
with open(file_, 'r') as keys:
    lines = keys.readlines()
    for line in lines:
        if "\n" in line:
            try:
                line = line.replace(" \n", '')
            except:
                line = line.replace("\n", '')
        line = line.split(',')
        key_words += line

generator = Pass()
variantes = generator.generate_variantes(key_words)
for key, item in variantes.items():
    generate_new_pass(variantes, item)
    break

