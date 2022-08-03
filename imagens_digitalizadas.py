import pygame

cup_armado = pygame.image.load("imagens/cup_armado.png").convert_alpha()
cup_armado = pygame.transform.scale(cup_armado, (300, 300))

cup_parado = pygame.image.load("imagens/cup_parado.png").convert_alpha()
cup_parado = pygame.transform.scale(cup_parado, (300, 300))

tela_inicial = pygame.image.load("imagens/tela_inicial.png").convert_alpha()
tela_inicial = pygame.transform.scale(tela_inicial, (1000, 670))

tela_jogo = pygame.image.load("imagens/tela_jogo.png").convert_alpha()
tela_jogo = pygame.transform.scale(tela_jogo, (1000, 670))

yoshi = pygame.image.load("imagens/yoshi.png").convert_alpha()
yoshi = pygame.transform.scale(yoshi, (400, 170))

cog_marrom = pygame.image.load("imagens/cog_marrom.png").convert_alpha()
cog_marrom = pygame.transform.scale(cog_marrom, (200, 200))

cog_vermelho = pygame.image.load("imagens/cog_vermelho.png").convert_alpha()
cog_vermelho = pygame.transform.scale(cog_vermelho, (200, 200))

noite=pygame.image.load("imagens/noite.png").convert_alpha()
noite = pygame.transform.scale(noite, (1000, 670))

noite_lua = pygame.image.load("imagens/noite_lua.png").convert_alpha()
noite_lua = pygame.transform.scale(noite_lua, (1000, 670))

tela_fim = pygame.image.load("imagens/tela_fim.png").convert_alpha()
tela_fim = pygame.transform.scale(tela_fim, (1000, 670))




