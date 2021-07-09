'''
*Media de n valores*
Calcular la media de n números.
'''

import random

num_media = int(input("De cuantos numeros se tiene que calcular la media: "))

numeros = [random.randint(0,100) for i in range(num_media)]
print(numeros)
media = sum(numeros) / num_media
print(media)