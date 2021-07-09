'''
*Adivina el número secreto*
Se genera un número aleatorio entero entre 1 y 100. El usuario debe adivinar el número secreto, diciendo en cada tirada si es mayor o menor.
'''

import random

adivina = random.randint(1,100)
num = int(input('Adivina el numero: '))

comprovar = lambda num: "El numero es mas pequeño" if num > adivina else "El numero es mas grande"
while num != adivina:
    print(comprovar(num))
    num = int(input('Prueba otra vez:' ))

print('El numero secreto era: ' + str(adivina) + ' lo has adivinado.')
