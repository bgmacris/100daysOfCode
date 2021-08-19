'''
*Oredenar números*
Imprimir una lista de 10 números aleatorios sin repetición que varíen en el rango 80 a 99.
Volver a imprimir la lista pero ordenada.
'''

from random import sample

# Funcion para ordenar una lista(Funciones inacabadas
def movimientos(central=False, derecha=False, izquierda=False):
	pass

def ordenar(lista):
	list_c = lista.copy()
	ord_list = []
	for i in lista:
		if ord_list == []:
			ord_list.append(i)
		else:
			for x in ord_list:
				if x > i:
					pass

lista = sample(list(range(80,100)),10)
print(lista)
print(sorted(lista))
