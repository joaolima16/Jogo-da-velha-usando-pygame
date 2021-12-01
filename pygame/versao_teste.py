from os import link
import pygame
from pygame.locals import *
import sys 
import time 
from pygame import image
from pygame import font

pygame.init()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
screen = pygame.display.set_mode((600, 600))
altura  = screen.get_height()
largura = screen.get_width()
xis = pygame.image.load("x.png")  #Criando a imagem x usada no jogo
bola = pygame.image.load("O.png") #criando a imagem O usada no jogo
xis = pygame.transform.scale(xis,(100,100)) #definindo o tamanho dela
bola = pygame.transform.scale(bola,(100,100))
done = False
continuar = False
quadrante_linha = [50,250,450]
quadrante_coluna = [50,250,450]
'''line_one = ['00', '01', '02']
line_two = ["10", "11", "12"]
line_three = ["20", "21", "22"]'''

matriz_jogo = [ 
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]
# ------- Inicia o jogo -------

screen.fill(RED) 
pygame.draw.line(screen, BLACK,(200,0), [200,600], 10)
pygame.draw.line(screen, BLACK,(400,0), [400,600], 10)
pygame.draw.line(screen, BLACK,(0,200), [600,200], 10)
pygame.draw.line(screen, BLACK,(0,400), [600,400], 10)
jogadas = 0 

    



def jogadas_1(pos,continua):    
    index_linha= int(pos[0]/200)
    index_coluna= int(pos[1]/200)
    if matriz_jogo[index_linha][index_coluna] =='_': 
        screen.blit(xis,(quadrante_linha[index_linha],quadrante_coluna[index_coluna]))
        matriz_jogo[index_linha][index_coluna] = 'x'
    else:
        print("posicao ja ocupada!")           

def jogadas_2(pos):
        index_linha= int(pos[0]/200)
        index_coluna = int(pos[1]/200)
        if matriz_jogo[index_linha][index_coluna]=='_':
            screen.blit(bola,(quadrante_linha[index_linha],quadrante_coluna[index_coluna]))
            matriz_jogo[index_linha][index_coluna] = 'O'
        
        else:
            print("posicao ocupada!")


while not done:
      mouse_pos = pygame.mouse.get_pos()   
      pygame.display.flip()
      
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # ---------------- pegando a posição com o click do mouse ---------------      
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos  = pygame.mouse.get_pos()
                
                if ( jogadas%2== 0):
                    jogadas_1(click_pos,continuar)
                    jogadas = jogadas + 1
                   
                    
                
                elif (  jogadas%2 == 1):
                    jogadas_2(click_pos)  
                    jogadas = jogadas + 1
                    '''print(line_one)
                    print(line_two)
                    print(line_three)
                    print("")'''
                   
                    
                if jogadas >=9:
                    done= True
                    break
print(matriz_jogo)                
      # ------------------------------------------------------------------------          
     
    
   