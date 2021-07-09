'''
*Bucles*
Listar los números del 1 al 10.
'''

# Creamos una lista utilizando range
print("Lista uno")
lista = list(range(1,11))
print(lista)

# Creando una lista utilizando el bucle for
print("\nLista dos")
lista = []
for i in range(10):
    lista.append(i + 1)
print(lista)

# Creando una lista utilizando el bucle for pero a la hora de definir la lista.
print("\nLista tres")
lista = [i + 1 for i in range(10)]
print(lista)
