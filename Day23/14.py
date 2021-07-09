'''
*Funciones*
Crear una función que calcule el cuadrado de un número. Probar la función con los números entre -10 y +10.
Crear otra función que lo único que hace es imprimir al final la frase “Programa finalizado”. Ejecutar ambas funciones.
'''

def fin():
    print("Programa finalizado")

def calcular():
    num = int(input("Introduce el numero: "))
    resultado = num**2
    print(str(num) + "**2 = " + str(resultado))
    fin()

calcular()

