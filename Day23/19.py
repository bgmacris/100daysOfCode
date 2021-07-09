'''
*Capitalización compuesta*
Crear una aplicación que trabaje con la ley de capitalización compuesta.
'''

C = float(input('Introduzca el capital inicial') or 1000)
print('Capital inicial=', C)
n = float(input('Introduzca los años') or 3)
print('años=', n)
i = float(input('Introduzca el tipo de interés, por ejemplo 0.08 para 8%') or .08)
print('Tipo de interés anual=', i)
print('Capital final=', round(C*(1+i)**n, 2))