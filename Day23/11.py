'''
*Unir listas*
Generar primero una lista con los números entre 0 y 10, 
luego generar otra lista con los números del 11 al 20. 
Unir ambas lista e imprimir el resultado.
'''

lista1 = [i for i in range(0,11)]
lista2 = [i for i in range(11, 21)]

# Dos formas de unir una lista
lista1.extend(lista2)

print(lista1)

