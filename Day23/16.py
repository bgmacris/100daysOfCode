'''
*Media ponderada*
Calcular la media ponderada de una serie de valores.
'''

print("Clauclar media ponderada de las notas")
cuantas = int(input("Cuantas notas vas a introducir? "))
notas = {}

for i in range(cuantas):
    i = float(input("Introduce la nota " + str(i + 1) + ': '))
    x = float(input("Indroduce el peso de la nota: "))
    notas[i] = x

operacion = 0
peso = 0
print(notas)
for i in notas:
    operacion += i * notas[i]

print(f'\nLa media ponderada es: \033[31m {round(operacion/sum(notas.values()),2)} \033[0;m ')
