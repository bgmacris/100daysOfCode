import math


lista = [1, 5, 10, 15, 20, 25, 30, 35]


def search_interpolation(lista, key):
    length = len(lista)
    left = 0
    right = len(lista) - 1
    position = -1
    
    pasos = 0
    while left <= right:
        pasos = pasos + 1
        pos = math.floor(left + ((key-lista[left])*(right-left) / (lista[right]-lista[left]) ))
        if lista[pos] == key:
            print(pasos)
            return key, pos
        elif lista[pos] < key:
            left = pos + 1
        else:
            right = pos - 1
    
    print(pasos)
    return -1
    
print(search_interpolation(lista, 30))