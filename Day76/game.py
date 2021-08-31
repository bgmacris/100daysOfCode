import random
import pygame
import os
import time


NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

pygame.init()

dimensiones = [300, 300]
root = pygame.display.set_mode(dimensiones)
pygame.display.set_caption('Piedra, Papel, Tijeras')

quit = False
clock = pygame.time.Clock()

global MAQUINA, POSIBILIDADES
MAQUINA = ['PIEDRA', 'PAPEL', 'TIJERAS']
POSIBILIDADES = {
    'PIEDRA': 'TIJERAS',
    'PAPEL': 'PIEDRA',
    'TIJERAS': 'PAPEL'
}
CONT = {
    'player': 0,
    'pc': 0
}

piedraImg = pygame.image.load(f'{os.path.dirname(__file__)}\\asset\\piedra.png')
papelImg = pygame.image.load(f'{os.path.dirname(__file__)}\\asset\\papel.png')
tijerasImg = pygame.image.load(f'{os.path.dirname(__file__)}\\asset\\tijeras.png')


def jugar(eleccion):
    global CONT
    pc_choice = random.choice(MAQUINA)
    if POSIBILIDADES[pc_choice] == eleccion:
        print(f'MAQUINA {pc_choice} GANA {eleccion}')
        root.fill(pygame.Color("black"))
        CONT['pc'] += 1
        return f'MAQUINA {pc_choice} GANA {eleccion}'
    elif POSIBILIDADES[eleccion] == pc_choice:
        print(f'JUGADOR {eleccion} GANA {pc_choice}')
        root.fill(pygame.Color("black"))
        CONT['player'] += 1
        return f'JUGADOR {eleccion} GANA {pc_choice}'
    else:
        print(f'EMPATE {pc_choice} {eleccion}')
        return f'EMPATE {pc_choice} {eleccion}'


while not quit:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            resultado = False
            if 20 < mouse[0] < 80 and 175 < mouse[1] < 234:
                resultado = jugar("PIEDRA")
            if 119 < mouse[0] < 179 and 175 < mouse[1] < 234:
                resultado = jugar("PAPEL")
            if 219 < mouse[0] < 280 and 175 < mouse[1] < 234:
                resultado = jugar("TIJERAS")
            
            if resultado:
                root.fill(pygame.Color("black"))
                resultado_txt = fuente.render(resultado, True, VERDE)
                pygame.display.flip()
                root.blit(resultado_txt, [10, 130])
                
                
            print(mouse)

    mouse = pygame.mouse.get_pos()
    # print(mouse)

    pygame.draw.rect(root, BLANCO, [20, 20, 250, 100], 2)
    fuente = pygame.font.Font(None, 25)
    player = fuente.render("Jugador", True, VIOLETA)
    pc = fuente.render("Ordenador", True, VIOLETA)
    root.blit(player, [30, 30])
    root.blit(pc, [175, 30])
    
    cont_player = fuente.render(str(CONT['player']), True, AZUL)
    cont_pc = fuente.render(str(CONT['pc']), True, AZUL)
    root.blit(cont_player, [60, 75])
    root.blit(cont_pc, [210, 75])
    
    root.blit(piedraImg, (20, 175))
    root.blit(papelImg, (120, 175))
    root.blit(tijerasImg, (220, 175))


    pygame.display.flip()
    
pygame.quit()
