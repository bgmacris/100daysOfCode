'''
*Pares*
Listar los números pares del 10 al 20.
'''

# Diferentes maneras de utilizar el bucle for.
print("Forma uno")
numeros = list(range(10,21))
pares = []
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
print(pares)

print("Forma dos")
pares = []
for i in range(10,21,2):
    pares.append(i)
print(pares)

print("Forma tres")
print([i for i in range(10,21,2)])