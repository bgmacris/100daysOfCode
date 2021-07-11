"""
Busqueda A*
Buscar la ruta mas corta de un punto a otro, segun su coste.
"""


class Nodo:
    def __init__(self,datos,hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.cose = None
        self.set_hijos(hijos)

    def set_hijos(self,hijos):
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

    def set_datos(self,datos):
        self.datos = datos

    def set_coste(self, coste):
        self.coste = coste
    
    def get_coste(self):
        return self.coste

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

    def __str__(self):
        return str(self.get_datos())


def comparar(x):
    return x.get_coste()

def busqueda_estrella(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_coste(0)
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera) != None:
        nodos_frontera = sorted(nodos_frontera, key=comparar)
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_coste(nodo.get_coste() + coste)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_coste() > hijo.get_coste():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
            nodo.set_hijos(lista_hijos)


if __name__ == "__main__":
    conexiones = {
        'I': {'A': 1, 'B': 5, 'C': 16, 'D': 5},
        'A': {'I': 1, 'B': 1},
        'B': {'A': 1, 'I': 5, 'C': 10, 'E': 5, 'F': 5},
        'C': {'I': 16, 'B': 10},
        'D': {'I': 5, 'J': 20},
        'E': {'B': 5, 'G': 10},
        'F': {'B': 5, 'D': 3, 'H': 10},
        'J': {'D': 20},
        'G': {'E': 10},
        'H': {'F': 10, 'Z': 3},
        'Z': {'H': 3}
    }

    coste_estimado = {
        'I': 100,
        'A': 27,
        'B': 20,
        'C': 30,
        'D': 22,
        'E': 10,
        'F': 12,
        'J': 20,
        'G': 15,
        'H': 11,
        'Z': 0
    }

    estado_inicial = 'I'
    solucion = 'Z'
    nodo_solucion = busqueda_estrella(conexiones, estado_inicial, solucion)

    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    print(resultado[::-1])
    print(nodo_solucion.get_coste())
