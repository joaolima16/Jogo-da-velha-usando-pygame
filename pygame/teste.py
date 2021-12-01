from os import link
from typing import Collection
import pygame
import sys
import time

from pygame import image

pygame.init()

size = width, height = 650, 650

screen = pygame.display.set_mode(size)



xis = pygame.image.load("x.png")
bolinha = pygame.image.load("O.png")

xis = pygame.transform.scale(xis, (100,100))
bolinha = pygame.transform.scale(bolinha, (100,100))

#varivais 
preto = 0, 0, 0
branco = 255, 255, 255
vermelho = 255, 0, 0
verde = 0, 255, 0
azul = 0, 0, 255
cores = [preto, branco, vermelho, verde, azul]

quadrante_linha = [50, 275, 475]
quadrante_coluna = [50, 275, 475]

screen.fill(cores[1])


def desenha_quadro():
    pygame.draw.line(screen, preto, (200,0), (200,700),5)
    pygame.draw.line(screen, preto, (450,0), (450,700),5)
    pygame.draw.line(screen, preto, (0,200), (700,200),5)
    pygame.draw.line(screen, preto, (0,400), (700,400),5)



def faz_jogada(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)

    screen.blit(xis,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
    


while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT): 
            sys.exit()

    desenha_quadro()

    if event.type == pygame.MOUSEBUTTONDOWN:
        click_pos = pygame.mouse.get_pos()
        faz_jogada(click_pos)



    pygame.display.flip()