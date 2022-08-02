import pygame
from config import *


pygame.init()


# ----- Gera tela inicial
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cabeças Copulares')
from imagens_digitalizadas import *
from classes import *
font = pygame.font.SysFont(None, 60)
text_game = font.render('Cabeças Copulares', True, (0, 255, 0))
state = 'start screen'
clock = pygame.time.Clock()
bem_vindo = font.render('Bem-Vindo ao JOGO CABEÇAS COPULARES!', True, AZUL_ESCURO)

if state == 'start screen':   
    window.blit(tela_inicial, (0,0))
    window.blit(cup_parado, (630,254))  
    window.blit(cup_armado, (100,254))  
    window.blit(bem_vindo, (50, 150))

pontos = 0
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
                clock.tick(FPS)

    if STATUS == GAME:
        score = font.render('score: {}'.format(pontos), True, (255, 255, 255))
        window.blit(tela_jogo,(x_img, 0))
        window.blit(tela_jogo,(x_img + WIDTH, 0))
        if x_img + WIDTH == 0:
            x_img = 0
        else:
            x_img -= 1
        
        window.blit(score, (800, 100))
        window.blit(cup_parado, (100,254))
        monstro=Cogumelo(cog_marrom, 900, 413)
        window.blit(monstro.image, monstro.rect)
            

    # ----- Gera saídas
    
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados