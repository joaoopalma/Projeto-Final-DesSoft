import pygame 
from config import *
from imagens_digitalizadas import *

class Cogumelo (pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

    

        self.image = img 
        self.rect = self.image.get_rect()


        # Coloca no lugar inicial definido em x, y do constutor
        x= 900
        y=413
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.x
        self.rect.y = self.y
        
        if self.rect.x >= WIDTH or self.rect.x < 0 or self.rect.y >= HEIGHT or self.rect.y < 0:
            self.kill()
            score+=10
