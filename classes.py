import pygame 
from config import *
from imagens_digitalizadas import *

class Cogumelo (pygame.sprite.Sprite):

    velocidade_inicial=1

    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.speed=Cogumelo.velocidade_inicial
        self.image = img 
        self.rect = self.image.get_rect()


        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.x = 900
        self.rect.y = 413

    def update(self):
        self.rect.x -= 4 * self.speed
        
        
        if self.rect.x >= WIDTH+57 or self.rect.x < 0 or self.rect.y >= HEIGHT or self.rect.y < 0:
            #self.rect.x = 900
            #self.rect.y = 413
            Cogumelo.velocidade_inicial+=0.5
            if Cogumelo.velocidade_inicial >= 3:
                Cogumelo.velocidade_inicial=1
            self.kill()
            

class Player (pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self. altura_pulo= 70
        self.subindo= True
        self.jumping= False
        self.image = img 
        self.rect = self.image.get_rect()


        # Coloca no lugar inicial definido em x, y do constutor
        x= 400
        y=254
        self.rect.x = x
        self.rect.y = y

    def update(self):
    
        if self.jumping:
            if self.subindo:
                self.rect.y -= 4
                if self.altura_pulo > self.rect.y:
                    self.subindo = False
            else:
                self.rect.y+=4

            if self.rect.y > 254:
                self.jumping = False
                self.subindo = True
                self.rect.y = 254


                        
    
