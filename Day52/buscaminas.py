import pygame
import copy
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
        

def see_map(map, poss):
    max_pos_x = len(map[0])
    max_pos_y = len(map)
    UP, DOWN, LEFT, RIGHT = True
    D_UP_R, D_UP_L, D_DOWN_R, D_DOWN_L = True
    
    if poss[0] == 0 and poss[1] == 0:
        UP, LEFT, D_UP_L, D_UP_R, D_DOWN_L = False
    
    if poss[0] == max_pos_x and poss[1] == 0:
        UP, RIGHT, D_UP_R, D_DOWN_R, D_UP_L = False
        
    if poss[0] == 0 and poss[1] == max_pos_y:
        DOWN, LEFT, D_UP_L, D_DOWN_L, D_DOWN_R = False
        
    if poss[0] == max_pos_x and poss[1] == max_pos_y:
        D_UP_R, RIGHT, D_DOWN_L, DOWN = False
    


map = mapa()
index_mines = put_mine(map)
num_next_to(map, index_mines)
for i in map:
    print(i)

pygame.init()
dimensiones = [500, 500]
ventana = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Buscaminas")

reloj = pygame.time.Clock()
ancho = 50
alto = 50
margen = 5

visitados = []
pendientes = []

GAME_OVER = False
while (not GAME_OVER):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            GAME_OVER = True
            
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            columna = pos[0] // (ancho + margen)
            fila = pos[1] // (alto + margen)
            print(pos, columna, fila)
            
        
        ventana.fill((250, 0, 0))
        
        for i in range(len(map)):
            for j in range(len(map[0])):
                color = [161, 158, 157]
                pygame.draw.rect(ventana, color, [
                                 (margen + ancho) * j + margen, (margen + alto) * i + margen, ancho, alto
                                 ], 0)
                
        pygame.display.flip()
