'''
*Número mayor y menor*
Dados dos números decir cuál es mayor, o si ambos son iguales.
'''

import random

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

comprovar = lambda x, y: f"{x} > {y}" if x > y else (f"{y} > {x}" if y > x else f"{x} = {y}")
print(comprovar(num1, num2))
