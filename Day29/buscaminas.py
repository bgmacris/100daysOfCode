import random
import numpy as np

def mapa():
    map = []
    for i in range(9):
        map.append(['U' for i in range(9)])
    return map


def put_mine(map):
    index_mines = []
    for i in range(9):
        row = random.randint(0, 8)
        column = random.randint(0, 8)
        if map[row][column] != 'X':
            index_mines.append((row, column))
            map[row][column] = 'X'
    print(index_mines)
    return index_mines


def calcular_numeros(map, pos_x, pos_y, method):
    if method == 'IZQ' or method == 'DER':
        desigual = 0 if method == 'IZQ' else 8
        if pos_y != desigual:
            if method == 'IZQ':
                pos_y_num = pos_y - 1
            else:
                pos_y_num = pos_y + 1
            if map[pos_x][pos_y_num] != 'X':
                if map[pos_x][pos_y_num] == 'U':
                    map[pos_x][pos_y_num] = '1'
                else:
                    map[pos_x][pos_y_num] = str(int(map[pos_x][pos_y_num]) + 1)
    
    if method == 'UP' or method == 'DOWN':
        desigual = 0 if method == 'UP' else 8
        if pos_x != desigual:
            if method == 'UP':
                pos_x_num = pos_x - 1
            else:
                pos_x_num = pos_x + 1
            if map[pos_x_num][pos_y] != 'X':
                if map[pos_x_num][pos_y] == 'U':
                    map[pos_x_num][pos_y] = '1'
                else:
                    map[pos_x_num][pos_y] = str(int(map[pos_x_num][pos_y]) + 1)
                    
    if 'DIAG-' in method:
        if method == 'DIAG-UP-IZQ' or method == 'DIAG-UP-DER':
            desigual_x = 0
            desigual_y = 0 if method == 'DIAG-UP-IZQ' else 8
            pos_x_num = pos_x - 1
            op_y = -1 if 'IZQ' in method else 1
            pos_y_num = pos_y + op_y
        if method == 'DIAG-DOWN-IZQ' or method == 'DIAG-DOWN-DER':
            desigual_x = 8
            desigual_y = 0 if method == 'DIAG-DOWN-IZQ' else 8
            pos_x_num = pos_x + 1
            op_y = -1 if 'IZQ' in method else 1
            pos_y_num = pos_y + op_y
        if pos_x != desigual_x and pos_y != desigual_y:
            if map[pos_x_num][pos_y_num] != 'X':
                if map[pos_x_num][pos_y_num] == 'U':
                    map[pos_x_num][pos_y_num] = '1'
                else:
                    map[pos_x_num][pos_y_num] = str(
                        int(map[pos_x_num][pos_y_num]) + 1)

def num_next_to(map, index_mines):
    for ind in index_mines:
        pos_x = ind[0]
        pos_y = ind[1]

        # Calcular todos los numeros al lado de las bombas
        # Izquierda
        calcular_numeros(map, pos_x, pos_y, 'IZQ')
        
        # Derecha
        calcular_numeros(map, pos_x, pos_y, 'DER')

        # Arriba
        calcular_numeros(map, pos_x, pos_y, 'UP')
        
        # Abajo
        calcular_numeros(map, pos_x, pos_y, 'DOWN')
        
        # Diagonal UP Izquierda
        calcular_numeros(map, pos_x, pos_y, 'DIAG-UP-IZQ')
        
        # Diagonal UP Derecha
        calcular_numeros(map, pos_x, pos_y, 'DIAG-UP-DER')
        
        # Diagonal Down Izquierda
        calcular_numeros(map, pos_x, pos_y, 'DIAG-DOWN-IZQ')
        
        # Diagonal Down Derecha
        calcular_numeros(map, pos_x, pos_y, 'DIAG-DOWN-DER')

map = mapa()
index_mines = put_mine(map)
num_next_to(map, index_mines)
for i in map:
    print(i)
