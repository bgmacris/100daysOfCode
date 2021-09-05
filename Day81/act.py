"""
Escribir una clase en python que obtenga todos los posibles subconjuntos únicos de un conjunto de números enteros distintos.
Entrada: [4, 5, 6]
Salida: [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
"""

class Mat:
    def __init__(self, conjunto):
        self.obj = conjunto
    
    def combinaciones(self):
        return self.recursive_comb([], self.obj)
    
    def recursive_comb(self, lista, conjunto):
        if conjunto:
            return self.recursive_comb(lista, conjunto[1:]) + self.recursive_comb(lista + [conjunto[0]], conjunto[1:])
        return [lista]
    

entrada = Mat([4, 5, 6])
print('Subconjuntos:', entrada.combinaciones())