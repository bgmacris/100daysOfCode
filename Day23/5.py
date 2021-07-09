'''
*Aleatorios*
Generar un número aleatorio.
'''

import random

length = int(input("Introduce la longitud del numero: "))
num = ''.join([str(random.randint(0, 9)) for i in range(length)])
print(num)
