import pygame
import os

pygame.init()

class Dino:
    X_POS = 30
    y_POS = 250
    JUMP_VEL = 8.5
    
    global RUNNING
    STATIC_PATH = os.path.join(os.path.dirname(__file__), 'static', 'player')
    print(os.path.join(STATIC_PATH, 'run1'))
    RUNNING = [pygame.image.load(os.path.join(STATIC_PATH, 'run1.png')),
               pygame.image.load(os.path.join(STATIC_PATH, 'run2.png')),
               pygame.image.load(os.path.join(STATIC_PATH, 'run3.png'))]
    # RUNNING = pygame.image.load(os.path.join(STATIC_PATH, 'run.png')).convert_alpha()
    
    def __init__(self):
        self.run_img = RUNNING
        
        self.step_index = 0
        self.image = self.run_img[0]
        
        self.player_run = True
    
    def update(self, Input):
        if self.player_run == True:
            self.run()
        if self.step_index >= 3:
            self.step_index = 0
            
        if not Input:
            self.player_run = True
    
    def run(self):
        print(self.step_index // 3)
        self.image = self.run_img[self.step_index]
        self.step_index += 1
        
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (10, 250))