import sys
from map import draw_map

def dijkstra(grafo, nodo_inicial):
    etiquetas = {}
    visitados = []
    pendientes = [nodo_inicial]
    nodo_actual = nodo_inicial

    # Nodo inicial
    etiquetas[nodo_actual] = [0, '']

    # Seleccionar el siguiente nodo de menor peso acumulado
    while len(pendientes) > 0:
        nodo_actual = nodo_menor_peso(etiquetas, visitados)
        visitados.append(nodo_actual)

        # Obtener conexiones
        for conexion, peso in grafo[nodo_actual].items():
            if conexion not in pendientes and conexion not in visitados:
                print(conexion)
                pendientes.append(conexion)
            nuevo_peso = etiquetas[nodo_actual][0] + peso

            # Etiquetar
            if conexion not in visitados:
                if conexion not in etiquetas:
                    etiquetas[conexion] = [nuevo_peso, nodo_actual]
                else:
                    if etiquetas[conexion][0] > nuevo_peso:
                        etiquetas[conexion] = [nuevo_peso, nodo_actual]


        pendientes.remove(nodo_actual)
    return etiquetas
    

def nodo_menor_peso(etiquetas, visitados):
    valor = sys.maxsize
    for nodo, etiqueta in etiquetas.items():
        if etiqueta[0] < valor and nodo not in visitados:
            valor = etiqueta[0]
            nodo_menor = nodo
    return nodo_menor

if __name__ == '__main__':
    mapa = draw_map()
    print(mapa)
    estado_inicial = (20,20)
    objetivo = (50, 50)
    
    buscar = dijkstra(mapa, estado_inicial)
    print(buscar)
