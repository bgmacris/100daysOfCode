"""
    Este script es para utilizarlo en la app de tkinter
"""
from puzzle import busqueda_amplietud
        
def search_solution(estado_inicial, solucion):
    nodo_solucion = busqueda_amplietud(estado_inicial, solucion)
    resultado = []
    
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    
    resultado.append(estado_inicial)
    return resultado[::-1]
