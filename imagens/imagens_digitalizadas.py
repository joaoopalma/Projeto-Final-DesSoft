import pygame

pygame.init()
cup_armado = pygame.image.load("imagens\\cup_armado.png").convert_alpha()
cup_armado = pygame.transform.scale(cup_armado, (300, 300))

cup_parado = pygame.image.load("imagens\\cup_parado.png").convert_alpha()
cup_parado = pygame.transform.scale(cup_parado, (300, 300))

tela_inicial = pygame.image.load("imagens\\tela_inicial.png").convert_alpha()
tela_inicial = pygame.transform.scale(tela_inicial, (1000, 670))