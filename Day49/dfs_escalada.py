def escalada_nodos(nodo_inicial, solucion):
    etiquetas = {}
    visitados = []
    pendientes = []
    nodo_actual = nodo_inicial
    visitados.append(nodo_actual)
    nivel = 0
    
    #[Nivel de la escalada, coste, padre del nodo]
    etiquetas[nodo_actual] = [nivel, 0, '']
    
    solucionado = False
    while not solucionado:        
        if etiquetas[nodo_actual][1] == solucion:
            solucionado = True
            print("Solucion", nodo_actual, etiquetas[nodo_actual])
            return nodo_actual 
        if nodo_actual != nodo_inicial:
            nodos_conexiones = len(conexiones[nodo_actual])
            cuenta = 0
            for i in conexiones[nodo_actual].keys():
                if i in visitados or i == etiquetas[nodo_actual][2]:
                    cuenta += 1
            if cuenta == nodos_conexiones:
                visitados.append(nodo_actual)
        nivel += 1
        for conexion in conexiones[nodo_actual]:
            if conexion not in pendientes and conexion not in visitados:
                pendientes.append(conexion)
            nuevo_peso = etiquetas[nodo_actual][1] + conexiones[nodo_actual][conexion]
            if conexion not in visitados:
                if conexion not in etiquetas:
                    etiquetas[conexion] = [nivel , nuevo_peso, nodo_actual]
        
        pendientes = sorted([i for i in pendientes if i != etiquetas[nodo_actual][2]], key=lambda x: etiquetas[x][1])
        
        print("Nodo Actual", nodo_actual, etiquetas[nodo_actual])
        print("pendientes", pendientes)
        print("VISITADOS", visitados)
        print("\n")
        
        if len(pendientes) > 0:           
            nodo_actual = pendientes[0]
            pendientes = []
        else:
            nivel = 1
            encontrado = False
            while not encontrado:
                for i in etiquetas:
                    if len(pendientes) > 0:
                        encontrado = True
                    if etiquetas[i][0] == nivel and i not in visitados:
                        pendientes.append(i)
                    
                nivel += 1
            pendientes = sorted(pendientes, key=lambda x: etiquetas[x][1])
            nodo_actual = pendientes[0]
            pendientes = []
         
                
if __name__ == "__main__":
    solucion = float('inf')
    conexiones = {
        'A': {'D': 3, 'F': 2, 'G': 1},
        'D': {'A': 1, 'H': 4, 'J': 3},
        'F': {'A': 1, 'C': 3, 'E': 8},
        'G': {'A': 1},
        'H': {'D': 3, 'B': 0},
        'J': {'D': 3, 'K': 0},
        'C': {'F': 2},
        'E': {'F': 2,'Z': 4,'W': 5},
        'B': {'H': 4},
        'K': {'J': 3,'L': solucion},
        'Z': {'E': 8},
        'W': {'E': 8},
        'L': {'K': 5}
    }
    estado_inicial = 'A'
    meta = escalada_nodos(estado_inicial, solucion)