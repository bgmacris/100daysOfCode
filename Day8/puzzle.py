"""
    Esta aplicacion es para ejecutar el puzzle manualmente y ver la salida en la linea de comandos
"""
from arbol import Nodo

def busqueda_amplietud(estado_inicial, solucion):
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)
    
    while len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)
        
        if nodo.get_datos() == solucion:
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            
            # Operadores logicos(Para realizar movimientos)
            # Movimiento izquierda(Intercambiar las dos piezas de la derecha)
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izq = Nodo(hijo)
            if not hijo_izq.en_lista(nodos_frontera) and not hijo_izq.en_lista(nodos_visitados):
                nodos_frontera.append(hijo_izq)
                
            # Movimientos central(Intercambiar las dos piezas del centro)
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_centro = Nodo(hijo)
            if not hijo_centro.en_lista(nodos_frontera) and not hijo_centro.en_lista(nodos_visitados):
                nodos_frontera.append(hijo_centro)
                
            # Movimientos derecha(Intercambiar las dos piezas de la derecha)
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_der = Nodo(hijo)
            if not hijo_der.en_lista(nodos_frontera) and not hijo_der.en_lista(nodos_visitados):
                nodos_frontera.append(hijo_der)
            
        nodo.set_hijos([hijo_izq, hijo_centro, hijo_der])
        
if __name__ == '__main__':
    estado_inicial = [4,3,2,1]
    solucion = [1,2,3,4]
    nodo_solucion = busqueda_amplietud(estado_inicial, solucion)
    resultado = []
    
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    
    resultado.append(estado_inicial)
    print(resultado[::-1])