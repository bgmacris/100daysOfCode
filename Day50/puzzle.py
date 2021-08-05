from copy import deepcopy, copy

class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = None
        self.padre = None

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_hijos(self, hijos):
        self.hijos = hijos
        for hijo in hijos:
            hijo.padre = self

    def get_hijos(self):
        return self.hijos

    def get_padre(self):
        return self.padre

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

direcciones = {"U": (-1, 0),
               "D": (1, 0),
               "L": (0, -1),
               "R": (0, 1)}


def get_index(nodo, valor):
    for i in nodo:
        if valor in i:
            return (nodo.index(i), i.index(valor))


def get_move_0(nodo):
    lista_hijos = []
    pos_0 = get_index(nodo, 0)

    for move in direcciones.keys():
        new_pos = (pos_0[0] + direcciones[move][0],
                pos_0[1] + direcciones[move][1])
        if 0 <= new_pos[0] <= len(nodo) and 0 <= new_pos[1] <= len(nodo[0]):
            try:
                hijo = deepcopy(nodo)
                hijo[pos_0[0]][pos_0[1]] = hijo[new_pos[0]][new_pos[1]]
                hijo[new_pos[0]][new_pos[1]] = 0
                lista_hijos.append(Nodo(hijo))
            except:
                pass
    return lista_hijos


if __name__ == "__main__":
	estado_inicial = [
        [0, 13, 3, 1],
        [5, 2, 6, 4],
        [15, 8, 12, 9],
        [7, 10, 11, 14]
	]

	solucion = [
        [1, 2, 3, 0],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ]

	for i in get_move_0(solucion):
		print(i.get_datos())
