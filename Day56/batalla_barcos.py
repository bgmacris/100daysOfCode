def tablero():
	numeracion = [str(i+1) for i in range(9)]
	tablero = []
	tablero.append(['N'])
	tablero[0] += numeracion
	for i in numeracion:
		fila = [str(i)]
		fila += ['x' for i in range(9)]
		tablero.append(fila)
	for i in tablero:
		print(i)

tablero()
