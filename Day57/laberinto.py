class Nodo:
	def __init__(self, datos, hijos=None):
		self.datos = datos
		self.hijos = None
		self.padre = None
		self.coste = None
		self.set_hijos(hijos)

	def set_hijos(self, hijos):
		self.hijos = hijos
		if hijos != None:
			for i in self.hijos:
				i.padre = self
	def get_padre(self):
		return self.padre

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
		en_lista = False
		for nodo in lista_nodos:
			if self.igual(nodo):
				en_lista = True
		return en_lista

def movimientos(laberinto, nodo):
	movimientos = []
	nx = nodo[0]
	ny = nodo[1]
	if nx != 0:
		movimientos.append((nx-1, ny) if laberinto[nx-1][ny] != 'X' else None)
	if nx != 4:
		movimientos.append((nx+1, ny) if laberinto[nx+1][ny] != 'X' else None)
	if ny != 0:
		movimientos.append((nx, ny-1) if laberinto[nx][ny-1] != 'X' else None)
	if ny != 4:
		movimientos.append((nx, ny+1) if laberinto[nx][ny+1] != 'X' else None)
	movimientos = [i for i in movimientos if i]
	return movimientos

def ordenar(x):
	return x.get_coste()

def a_star(laberinto, inicio, solucion):
	solucionado = False
	nodos_visitados = []
	nodos_frontera = []
	nodo_inicial = Nodo(inicio)
	nodo_inicial.set_coste(0)
	nodos_frontera.append(nodo_inicial)
	while (not solucionado) and len(nodos_frontera) != 0:
		nodos_frontera = sorted(nodos_frontera, key=ordenar)
		nodo = nodos_frontera.pop(0)
		nodos_visitados.append(nodo)
		if nodo.get_datos() == solucion:
			solucionado = True
			return nodo
		else:
			dato_nodo = nodo.get_datos()
			hijos = [Nodo(i) for i in movimientos(laberinto, dato_nodo)]
			for h in hijos:
				coste = int(nodo.get_coste()) + 1
				h.set_coste(coste)
				if not h.en_lista(nodos_visitados):
					if h.en_lista(nodos_frontera):
						for n in nodos_frontera:
							if n.igual(h) and n.get_coste() > h.get_coste():
								nodos_frontera.remove(n)
								nodos_frontera.append(h)
					else:
						nodos_frontera.append(h)
			nodo.set_hijos(hijos)

if __name__ == '__main__':
	laberinto = [[' ' for i in range(5)] for i in range(5)]

	muros = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
	for muro in muros:
		mx = muro[0]
		my = muro[1]
		laberinto[mx][my] = 'X'

	nodo_inicial = (0, 0)
	nodo_final = (4, 4)


	for i in laberinto:
		print(i)
	print("\n")

	resultado = []
	nodo_solucion = a_star(laberinto, nodo_inicial, nodo_final)
	nodo = nodo_solucion
	while nodo.get_padre() != None:
		resultado.append(nodo.get_datos())
		nodo = nodo.get_padre()
	resultado.append(nodo_inicial)
	print(resultado[::-1])
	print("Coste:", nodo_solucion.get_coste())
