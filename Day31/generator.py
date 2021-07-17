class Pass:
    def __init__(self, password=None, hijos=None):
        self.datos = None
        
        self.lower = 'abcdefghijklmnopqrstuvwxyz'
        self.upper = self.lower.upper()
        self.special = {
            'A': 4,
            'B': 8,
            'O': 0,
            'S': 5,
            'E': 3,
            'T': 7,
            'Z': 2,
            'I': 1
        }
        self.num = '1234567890'
        self.signos = '?-,.=!"·$%&/)('
        self.char = self.upper + self.lower + self.num + self.signos

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def generate_variantes(self, list_words):
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
                    if letter.upper() in self.special:
                        word = word.replace(letter, str(self.special[letter.upper()]))
                lista.append(word)
            variantes[key] += lista
        
        return variantes

    def movimientos(self, values):
        print(values)
        if type(values) != list:
            return {'ERROR-01': 'Error type valu, is necessary list'}
        for keys in values:
            print(keys)

    def comb_simple(self, key, data, visitados=[]):
        variantes = []
        new_pass = key
        for key_data, item in data.items():
            for it in item:
                if it not in visitados:
                    # list_move = self.movimientos(data)
                    print(it)
                    break
            
            

