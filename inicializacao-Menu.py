import pygame
from config import *
from classes import *
#from imagens.imagens_digitalizadas import *


pygame.init()



# ----- Gera tela inicial
window = pygame.display.set_mode((WIDTH, HEIGHT))
import imagens.imagens_digitalizadas as img
pygame.display.set_caption('Cabeças Copulares')
font = pygame.font.SysFont(None, 60)
text_game = font.render('Cabeças Copulares', True, (0, 255, 0))
state = 'start screen'

if state == 'start screen':
    window.blit(img.tela_inicial, (0,0))
    window.blit(img.cup_parado, (630,254))  
    window.blit(img.cup_armado, (100,254))  



# ----- Inicia estruturas de dados
STATUS = INIT

# ===== Loop principal =====
while STATUS != QUIT:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            if x > 0 and y > 0 and x < 1000 and y < 650:
                STATUS = GAME

    if STATUS == GAME:
        window.blit(img.tela_jogo,(0, 0))
        window.blit(img.cup_parado, (100,254))
            

    # ----- Gera saídas
    
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados