import pygame
from config import *
import random


pygame.init()


# ----- Gera tela inicial
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cabeças Copulares')
from imagens_digitalizadas import *
from classes import *
font = pygame.font.SysFont("Arial", 50)
text_game = font.render('Cabeças Copulares', True, (0, 255, 0))
state = 'start screen'
clock = pygame.time.Clock()
bem_vindo = font.render('Bem-Vindo ao JOGO CABEÇAS COPULARES!', True, AZUL_ESCURO)
jogador=Player(cup_parado, 400, 254)
escolhido=random.choice([cog_marrom, cog_vermelho, yoshi, feno, arbusto])
monstro=Cogumelo(escolhido, 900, 413)
jogando= False
monstros = pygame.sprite.Group()
monstros.add(monstro)

# Clock
clock = pygame.time.Clock()

tempo_total = pygame.time.get_ticks() # variável responsável por armazenar o tempo decorrido desde o início do jogo
tempo_criacao= tempo_total
tempo_espera= 5

if state == 'start screen':   
    window.blit(tela_inicial, (0,0))
    window.blit(cup_parado, (630,254))  
    window.blit(cup_armado, (100,254))  
    window.blit(bem_vindo, (50, 150))


# ----- Inicia estruturas de dados
STATUS = INIT

# ===== Loop principal =====
while STATUS != QUIT:

    clock.tick(FPS)
    
    # ----- Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STATUS = QUIT
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            if x > 0 and y > 0 and x < 1000 and y < 650:
                STATUS = GAME
                clock.tick(FPS)
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    jogador.jumping= True

        

    
    
    if STATUS == GAME:
        
        window.blit(tela_jogo,(x_img, 0))
        window.blit(tela_jogo,(x_img + WIDTH, 0))
        if x_img + WIDTH == 0:
            x_img = 0
        else:
            x_img -= 1
          
        colisao= pygame.sprite.spritecollide(jogador, monstros, False, pygame.sprite.collide_mask)

            ## TImer

        fonte_timer = pygame.font.SysFont("Arial", 30)# Fonte para o timer
        tempo_passado = pygame.time.get_ticks() - tempo_total # Variável para armazenar o tempo - o temp total
        segundos =  tempo_passado // 1000  # Convertendo para segundos

        if segundos >= 60:
            segundos -= 60 * (int(minutos))
        pontos = segundos
        score = font.render('score: {}'.format(pontos), True, VERDE)
        window.blit(score, (800, 50))

        minutos = tempo_passado // 60000 # Convertendo para minutos

        if segundos < 10:
            segundo = '0' + str(segundos)
        if minutos < 10:
            minutos = '0' + str(minutos)
        
        mili = str(tempo_passado)[-3:]
        
        time = f'{minutos}: {segundos}.{mili}'

        crono = fonte_timer.render(time, True, VERDE)
        crono_rect = crono.get_rect()
        #crono_pos = WIDTH / 2
        #crono
        window.blit(crono, (800, 100))


        if len(colisao)>0:
            STATUS = END_SCREEN
        
        tempo_criacao2=(pygame.time.get_ticks() - tempo_criacao)//1000
        if int(tempo_criacao2)>=tempo_espera:
            escolhido=random.choice([cog_marrom, cog_vermelho, yoshi, feno, arbusto])
            monstro=Cogumelo(escolhido, 900, 413)
            monstros.add(monstro)
            tempo_criacao = pygame.time.get_ticks()
            tempo_espera=random.uniform(2,6)


            



        if segundos>10:
            window.blit(noite_lua,(x_img,0))
            window.blit(noite,(x_img + WIDTH, 0))
            window.blit(crono, (800, 100))
            window.blit(score, (800, 50))
            if x_img + WIDTH == 0:
                x_img = 0
            else:
                x_img -= 1

        jogador.update()
        monstros.update()
        monstros.draw(window) 
        window.blit(jogador.image, jogador.rect)
  
    if STATUS == END_SCREEN:
        window.blit(tela_fim, (0, 0))
        pontos_finais = font.render('Sua pontuação foi {0}'.format(pontos), True, VERMELHO)
        window.blit(pontos_finais, (250, 17))


       
          

    # ----- Gera saídas
    
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados