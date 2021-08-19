'''
*Bucles animados*
Generar la tabla de multiplicar.
'''

def tabla(num):
    for i in range(1,11):
        print(f'{num} * {i} = {num*i}')

tabla(int(input('Tabla de multiplicar del numero: ')))
