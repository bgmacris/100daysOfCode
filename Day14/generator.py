class Pass:
    def __init__(self, password, hijos=None):
        self.datos = password
        self.hijos = None
        self.padre = None
        self.set_hijos(hijos)

    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos != None:
            for i in self.hijos:
                i.padre = self
                
    def get_hijos(self):
        return self.hijos
    
    def get_padre(self):
        return self.padre
    
    def set_padre(self, padre):
        self.padre = padre
        
    def get_datos(self):
        return self.datos

    def igual(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista
    
    def get_index_char(self, char):
        lst = []
        for i in range(len(self.datos)):
            if (self.datos[i] == char):
                lst.append(i)
        
        return lst
    
    def replace_index(self, index, text):
        self.datos = self.datos[:index] + text.get_datos() + self.datos[1+index:]
        print(self.datos)
