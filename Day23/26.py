'''
*Cifras pares e impares*
Generar un número aleatorio entero entre un millón y dos millones. Imprimir ese número en pantalla y decir cuántas cifras pares e impares tiene.
'''

import random

num = random.randint(1000000,2000000)
pares = [i for i in list(str(num)) if int(i) % 2 == 0]
impares = [i for i in list(str(num)) if int(i) % 2 != 0]
print(num)
print('Numeros pares: ' + ','.join(pares))
print('Numeros impares: ' + ','.join(impares))
