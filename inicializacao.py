import pygame


pygame.init()



# ----- Gera tela inicial
xt = 1000
yt = 670
window = pygame.display.set_mode((xt, yt))
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
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados