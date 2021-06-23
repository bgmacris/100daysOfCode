from arbol import Nodo

def busqueda_amplietud(conexiones, estado_inicial, objetivo):
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)

    while len(nodos_frontera):
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)

        if nodo.get_datos() == objetivo:
            return nodo
        else:
            datos_nodo = nodo.get_datos()
            hijos = []
            for hijo in conexiones[datos_nodo]:
                hijo = Nodo(hijo)
                
                hijos.append(hijo)
                if not hijo.en_lista(nodos_frontera) and not hijo.en_lista(nodos_visitados):
                    nodos_frontera.append(hijo)

        nodo.set_hijos(hijos)
                


def search(estado_inicial, objetivo):
    conexiones = {
            'malaga': {'salamanca', 'madrid', 'barcelona'},
            'sevilla': {'santiago', 'madrid'},
            'granada': {'valencia'},
            'valencia': {'barcelona', 'granada'},
            'madrid': {'salamanca', 'sevilla', 'malaga', 'barcelona', 'santander'},
            'barcelona': {'zaragoza', 'santiago', 'madrid', 'malaga', 'valencia'},
            'salamanca': {'malaga', 'madrid'},
            'santiago': {'sevilla', 'santander', 'barcelona'},
            'santander': {'santiago', 'madrid'},
            'zaragoza': {'barcelona'}
        }

    # Para poder cambiarlo y ejeutar el script sin 
    # la necesidad de utilizar la api
    estado_inicial = estado_inicial
    objetivo = objetivo

    resultado = []
    nodo_solucion = busqueda_amplietud(conexiones, estado_inicial, objetivo)
    nodo = nodo_solucion
    print(nodo.get_padre(),"X")
    while nodo.get_padre() != None: 
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    
    resultado.append(estado_inicial)
    print(resultado[::-1])
    return resultado[::-1]