import pygame

#pygame.init()
cup_armado = pygame.image.load("imagens\\cup_armado.png").convert_alpha()
cup_armado = pygame.transform.scale(cup_armado, (300, 300))

cup_parado = pygame.image.load("imagens\\cup_parado.png").convert_alpha()
cup_parado = pygame.transform.scale(cup_parado, (300, 300))

tela_inicial = pygame.image.load("imagens\\tela_inicial.png").convert_alpha()
tela_inicial = pygame.transform.scale(tela_inicial, (1000, 670))

tela_jogo = pygame.image.load("imagens\\tela_jogo.png").convert_alpha()
tela_jogo = pygame.transform.scale(tela_jogo, (1000, 670))

yoshi = pygame.image.load("imagens\\yoshi.png").convert_alpha()
yoshi = pygame.transform.scale(yoshi, (75, 75))

cog_marrom = pygame.image.load("imagens\\cog_marrom.png").convert_alpha()
cog_marrom = pygame.transform.scale(cog_marrom, (75, 75))

cog_vermelho = pygame.image.load("imagens\\cog_vermelho.png").convert_alpha()
cog_vermelho = pygame.transform.scale(cog_vermelho, (75, 75))




