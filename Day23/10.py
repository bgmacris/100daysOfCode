'''
*Progresión geométrica*
Calcular cuantos granos de trigo tendríamos que utilizar si por cada casilla de un tablero de ajedrez pusiéramos un grano en la primera casilla, 
dos en la segunda, cuatro en la tercera, y así doblando hasta la última.
'''

### NOSE SI ESTA BIEN RESUELTO EL PROBLEMA xd####
casillas = {
    1: 0,
    2: 0,
    3: 0,
}

# Utilizando el bucle for, range(64) porque es el numero de casillas en el tablero.
# Por cada casilla, sumamos el valor correspondiente a las 3 casillas principales.
for i in range(64):
    casillas[1] = casillas[1] + (i + 1)
    casillas[2] = casillas[2] + (i + 2)
    casillas[3] = casillas[3] + (i + 4)

print(casillas)
print('Total trigo: ' + str(sum(casillas.values())))
