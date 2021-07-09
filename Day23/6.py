'''
*Intervalos*
Generar un número aleatorio entre 1 y 120. Decir si se encuentra en el intervalo entre 10 y 50, 
o bien si es mayor de 50 hasta 100, o bien si es mayor de 100, o bien si es menor de 10.
'''

import random

def diccionario():
    num = random.randint(1,120)
    print("El numero es: " + str(num))

    posibilidades = {
        0: 'El numero es menor que 10',
        1: 'El numero se encuentra entre el 10 y el 50',
        2: 'El numero se encuentra entre el 50 y el 100',
        3: 'El numero es mayor que 100'
    }
    
    index = len([i for i in [9,51,100,121] if i < num])
    print(posibilidades[index])

diccionario()



