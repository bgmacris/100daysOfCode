"""
Calcular la suma de los divisores de cada número
introducido por teclado. Terminaremos cuando el número
ingresado sea negativo.
"""

num = int(input("Introduce un numero: "))

while num > 0:
    total = 0
    for divisor in range(1, num+1):
        if (num % divisor) == 0:
            total = total + divisor
    print(total)
    num = int(input("Introduce un numero: "))
