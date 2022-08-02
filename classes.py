import pygame 
from config import *
from imagens_digitalizadas import *

class Player (pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img 
        self.rect = self.image.get_rect()


        # Coloca no lugar inicial definido em x, y do constutor
        x= 900
        y=413
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        self.rect.x += self.d_x
        self.rect.y = self.d_y
        
        if self.rect.x >= WIDTH or self.rect.x < 0 or self.rect.y >= HEIGHT or self.rect.y < 0:
            self.kill()
