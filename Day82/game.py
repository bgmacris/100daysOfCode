import pygame
import sys
import time
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((400,400))
pygame.display.set_caption("RUN")

font = pygame.font.Font('freesansbold.ttf', 32)
score = 0
text = font.render(str(score), True, (255,255,255), (0,0,0))
textRect = text.get_rect()
textRect.center = (15, 15)

#COLORES
Wallpaper = pygame.Color(102,182,155)
WallColor = pygame.Color(41,41,41)
PlayerColor = pygame.Color(255,255,255)
EnemyColor = pygame.Color(0,0,0)
DrinkColor = pygame.Color(100,14,215)

Yellow = pygame.Color(205,200,52)
Green1 = pygame.Color(30,155,100)
Green2 = pygame.Color(0,155,0)
Red1 = pygame.Color(200,10,10)
Red2 = pygame.Color(155,10,10)
Blue = pygame.Color(0,0,175)

#CARACTERISTICAS JUGADOR
posXP = 200
posYP = 350
heigh = 25
velocidad = 0.07

#POSICION/VELOCIDAD ENEMY
posXE = 0
posYE = 0
velEnemy = 0.03

#POSICION DRINK(SCORE)
posXD = 0
posYD = 0

#BOOLEANOS JUEGO
inicio = 0
gameover = 1

# Menu de juego (Opciones: Start-Quit)
def boton(msg,x,y,a,s,d,f):
    global ventana, font, gameover, posXE, posXP, posYE, posYP, inicio
    Mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Cambiar color botones si el raton esta encima
    if  x+a > Mouse[0] > x and y+s > Mouse[1] > y:
        pygame.draw.rect(ventana, d,(x,y,a,s))
        Text = font.render(msg, True, (255,255,255), d)
        # Valores posicion jugador y enemigo al pulsar 'Start'
        if click[0] and msg != "Quit":
            velocidad = 0.05
            posXP = 200
            posYP = 350
            posXE = 0
            posYE = 0
            gameover = 0
        # Se cierra el juego al pulsar 'Quit'
        elif click[0] and msg == "Quit":
            pygame.quit()
            sys.exit()
    # Definir colores de los botones si el raton no esta encima
    else:
        pygame.draw.rect(ventana, f,(x,y,a,s))
        Text = font.render(msg, True, (255,255,255), f)

    # Centrar texto
    textRect = Text.get_rect()
    textRect.center = (x+(a/2), y+(s/2))
    ventana.blit(Text, textRect)

# Sumar puntuacion en el Score cada vez que se colision con el objeto 'Drink'
def Score(countScore = True):
    global score, posXD, posYD, beber
    if beber:
        score += 1
        while True:
            posXD = randint(10,390)
            posYD = randint(10,390)
            if 260 > posXD > 120 and  260 > posYD > 140:
                posXD = randint(10,390)
                posYD = randint(10,390)
            else:
                break
        print("(" + str(posXD) + "," + str(posYD) + ")")
        beber = False
    if countScore == False:
        score = 0

while True:
    # pygame.time.delay(-100)
    ventana.fill(Wallpaper)

    # Cerrar ventana
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    # Si el enemigo nos atrapa, volvemos a la pantalla de inicio
    if gameover:
        boton("Start",150,100,100,50,Green1,Green2)
        boton("Quit",150,200,100,50,Red1,Red2)

    # Siemre y cuando el enemigo no nos atrapa el juego sigue
    if gameover != 1:
        # Dibujar el score en pantalla
        text = font.render(str(score), True, (255,255,255), (0,0,0))
        ventana.blit(text, textRect)
        keys = pygame.key.get_pressed()
        # Funcion para la teletransportacio (Cuadrado negro del centro) Calcular salida a la otra parte(Solo salidas diagonales)
        def WallSpeed(op,direccion,posPX,pos,x, y):
            global posXP, posYP
            velocidad = 0.05
            if op == "r" and direccion == "h":
                if int(posXP) - 1 - velocidad > x or int(posXP) - 1 - velocidad < y:
                    colision = False
                    posXP -= 1
                else:
                    if posPX:
                        posXP = pos
                    else:
                        posYP = pos
            elif op == "s" and direccion == "h":
                if int(posXP) + 1 + velocidad > x or int(posXP) + 1 + velocidad < y:
                    colision = False
                    posXP += 1
                else:
                    if posPX:
                        posXP = pos
                    else:
                        posYP = pos

        # Control movimiento jugador
        if keys[pygame.K_a]:
            if  posXP - velocidad <= 0:
                posXP = 0
            if velocidad == 0:
                WallSpeed("r","h",1, 133, 249, 136)
            else:
                posXP -= velocidad
        if keys[pygame.K_d]:
            if  posXP + velocidad >= 385:
                posXP = 385
            if velocidad == 0:
                WallSpeed("s","h",1, 252, 249, 136)
            else:
                posXP += velocidad
        if keys[pygame.K_w]:
            if  posYP - velocidad <= 1:
                posYP = 1
            if velocidad == 0:
                velocidad = 0.05
                if int(posYP) - 1 - velocidad > 249 or int(posYP) - 1 - velocidad < 126:
                    colision = False
                else:
                    posYP = 123
            else:
                posYP -= velocidad
        if keys[pygame.K_s]:
            if  posYP + velocidad >= 375:
                posYP = 375
            if velocidad == 0:
                velocidad = 0.05
                if int(posYP) + 1 + velocidad > 249 or int(posYP) + 1 + velocidad < 126:
                    colision = False
                else:
                    posYP = 252
            else:
                posYP += velocidad

        # Volver a dibujar la bebida despues de colisionar con el jugador
        if posXD == 0 and posYD == 0:
            while True:
                posXD = randint(10,390)
                posYD = randint(10,390)
                if 260 > posXD > 120 and  260 > posYD > 140:
                     posXD = randint(10,390)
                     posYD = randint(10,390)
                else:
                    break
            print("(" + str(posXD) + "," + str(posYD) + ")")
        Drink = pygame.Rect(posXD, posYD, 15,15)
        pygame.draw.rect(ventana,DrinkColor, Drink)

        Player = pygame.Rect(posXP,posYP,15,heigh)
        pygame.draw.rect(ventana,PlayerColor,Player)

        # Detectar colision player - drink
        if Player.colliderect(Drink):
            beber = True
            Score()
            Drink = pygame.Rect(posXD, posYD, 15,15)
            pygame.draw.rect(ventana,Blue, Drink)

        # Control seguimiento enemigo al jugador
        if posXE < posXP:
            posXE += velEnemy
        if posXE > posXP:
            posXE -= velEnemy
        if posYE < posYP:
            posYE += velEnemy
        if posYE > posYP:
            posYE -= velEnemy

        # Control colision enemy - player
        Enemy = pygame.Rect(posXE,posYE,15,heigh)
        pygame.draw.rect(ventana, EnemyColor, Enemy)
        if Enemy.colliderect(Player):
            gameover = 1
            posXD, posYD = 0,0
            try:
                Score(False)
            except:
                pass
        

        # Control colision teletransportación (Cuadrado negro del centro del mapa)
        if int(posXP) < 249 and int(posXP) > 136:
            if int(posYP) < 249 and int(posYP) > 126:
                if colision:
                    velocidad = 0
                    colision = False
        else:
            velocidad = 0.05
        colision = True
        Wall = pygame.Rect(150, 150, 100, 100)
        pygame.draw.rect(ventana,WallColor,Wall)
    
    pygame.display.update()
