'''
*Máximo y mínimo*
Generar 10 números aleatorios y calcular el máximo y el mínimo.
'''

from random import randint

x = [randint(1,100) for i in range(10)]

# Funciones
def maxmin_comparacion(lista, max=None, min=False):
	num = None
	for i in lista:
		if not num:
			num = i
		else:
			if i > num and max:
				num = i
			if i < num and min:
				num = i
	return num

def maxmin_sort(lista, max=None, min=False):
	if max:
		return sorted(lista)[-1]
	if min:
		return sorted(lista)[0]



print(f'Numeros: {x}')
print(f'Maximo: {max(x)}')
print(f'Minimo: {min(x)}')
print(f'Maximo comparacion: {maxmin_comparacion(x, max=True)}')
print(f'Maximo sort: {maxmin_sort(x, max=True)}\n')
print(f'Minimo: {min(x)}')
print(f'Minimo comparacion: {maxmin_comparacion(x, min=True)}')
print(f'Minimo sort: {maxmin_sort(x, min=True)}')
