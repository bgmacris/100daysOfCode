import pygame
import os
from dino import Dino

pygame.init()
SCREEN_H = 300
SCREEN_W = 800
ROOT = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Dinosaur")

# IMAGE
global logImg, bgImg
STATIC_PATH = os.path.join(os.path.dirname(__file__), 'static')
logImg = pygame.image.load(os.path.join(STATIC_PATH, 'log.png'))
bgImg = pygame.image.load(os.path.join(STATIC_PATH, 'bg.png'))

def main():
    global x_pos_bg, y_pos_bg, game_speed
    RUN = True
    clock = pygame.time.Clock()
    player = Dino()
    game_speed = 15
    x_pos_bg = 0
    y_pos_bg = 250
    
    def background():
        global x_pos_bg, y_pos_bg
        image_w = bgImg.get_width()
        ROOT.blit(bgImg, (x_pos_bg, y_pos_bg))
        ROOT.blit(bgImg, (image_w + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_w:
            ROOT.blit(bgImg, (image_w + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed
        
    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
        
        ROOT.fill((255, 255, 255))
        
        INPUT = pygame.key.get_pressed()
        player.draw(ROOT)
        player.update(INPUT)
        
        background()
        
        clock.tick(30)
        pygame.display.update()

def menu():
    RUN = True
    logImg = pygame.image.load(os.path.join(STATIC_PATH, 'log.png'))
    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                main()
        
        ROOT.fill((255, 255, 255))
        font = pygame.font.Font(None, 30)
        
        text = font.render("Pulsa una tecla para empezar", True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_W // 2, SCREEN_H // 2)
        ROOT.blit(text, textRect)
        ROOT.blit(logImg, (SCREEN_W // 2 - 50, SCREEN_H // 2 - 150))
        pygame.display.update()
        
menu()