from os import link
import pygame
from pygame.locals import *
import sys 
import time 
from pygame import image
from pygame import font

pygame.init()

#------------------------ Definindo as cores no pygame------------------------
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
#------------------------------------------------------------------------------

#-------------------------- Criando a tela e definindo o Tamanho dela-----------------------

screen = pygame.display.set_mode((600, 600))
altura  = screen.get_height()
largura = screen.get_width()
#--------------------------------------------------------------------------------------------

#---------------------- Criando e dimensionando as formulas X e O ----------------------------

xis = pygame.image.load("x.png")  #Criando a imagem x usada no jogo
bola = pygame.image.load("O.png") #criando a imagem O usada no jogo
xis = pygame.transform.scale(xis,(100,100)) #definindo o tamanho dela
bola = pygame.transform.scale(bola,(100,100))

#---------------------------------------------------------------------------------------------
done = False
velha = pygame.image.load('empate.png')
quadrante_linha = [50,250,450]
quadrante_coluna = [50,250,450]
#------------------- Criando a matriz do Jogo-------------------------------
matriz_jogo = [ 
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]
vencedor = 0
#--------------------------------------------------------------------------

#---------------- Definindo a cor de fundo e as linhas da tela-------------
screen.fill(WHITE) 
pygame.draw.line(screen, BLACK,(200,0), [200,600], 10)
pygame.draw.line(screen, BLACK,(400,0), [400,600], 10)
pygame.draw.line(screen, BLACK,(0,200), [600,200], 10)
pygame.draw.line(screen, BLACK,(0,400), [600,400], 10)
jogadas = 0

#--------------------------------------------------------------------------
    
def vitoria():
    #----------------------- validação dos jogadores------------------------
    if matriz_jogo[0][0]==matriz_jogo[0][1]=='X' and matriz_jogo[0][0]==matriz_jogo[0][2] =='X':
        pygame.draw.line(screen, BLUE,(0,100), [600,100], 10)
        return 1
    elif matriz_jogo[1][0]==matriz_jogo[1][1]=='X' and matriz_jogo[1][0]==matriz_jogo[1][2] =='X':
        pygame.draw.line(screen, BLUE,(0,300), [600,300], 10)
        return 1
    elif matriz_jogo[2][0]==matriz_jogo[2][1]=='X' and matriz_jogo[2][0]==matriz_jogo[2][2]=='X':
        pygame.draw.line(screen, BLUE,(0,500), [600,500], 10)
        return 1
    elif matriz_jogo[0][0]==matriz_jogo[1][0]=='X' and matriz_jogo[0][0]==matriz_jogo[2][0]=='X':
        pygame.draw.line(screen, BLUE,(100,0), [100,600], 10)
        return 1
    elif matriz_jogo[0][1]==matriz_jogo[1][1]=='X' and matriz_jogo[0][1]==matriz_jogo[2][1]=='X':
        pygame.draw.line(screen, BLUE,(300,0), [300,600], 10)
        return 1
    elif matriz_jogo[0][2]==matriz_jogo[1][2]=='X' and matriz_jogo[0][2]==matriz_jogo[2][2]=='X':
        pygame.draw.line(screen, BLUE,(500,0), [500,600], 10)
        return 1
    elif matriz_jogo[0][0]==matriz_jogo[1][1]=='X' and matriz_jogo[0][0]==matriz_jogo[2][2]=='X':
        pygame.draw.line(screen, BLUE,(0,0), [600,600], 10)
        return 1
    elif matriz_jogo[0][2]==matriz_jogo[1][1]=='X' and matriz_jogo[0][2]==matriz_jogo[2][0]=='X':
        pygame.draw.line(screen, BLUE,(600,0), [0,600], 10)
        return 1
    

    #---------------------------------------JOGADOR 2--------------------------------------------

    if matriz_jogo[0][0]==matriz_jogo[0][1]== 'O' and matriz_jogo[0][0]==matriz_jogo[0][2] =='O':
        pygame.draw.line(screen, RED,(0,300), [600,300], 10)
        return 2
    elif matriz_jogo[1][0]==matriz_jogo[1][1]=='O' and matriz_jogo[1][0]==matriz_jogo[1][2] =='O':
        pygame.draw.line(screen, RED,(0,300), [600,300], 10)
        return 2
    elif matriz_jogo[2][0]==matriz_jogo[2][1]=='O' and matriz_jogo[2][0]==matriz_jogo[2][2]=='O':
        pygame.draw.line(screen, RED,(0,500), [600,500], 10)
        return 2
    elif matriz_jogo[0][0]==matriz_jogo[1][0]=='O' and matriz_jogo[0][0]==matriz_jogo[2][0]=='O':
        pygame.draw.line(screen, RED,(100,0), [100,600], 10)
        return 2
    elif matriz_jogo[0][1]==matriz_jogo[1][1]=='O' and matriz_jogo[0][1]==matriz_jogo[2][1]=='O':
        pygame.draw.line(screen, RED,(300,0), [300,600], 10)
        return 2
    elif matriz_jogo[0][2]==matriz_jogo[1][2]=='O' and matriz_jogo[0][2]==matriz_jogo[2][2]=='O':
        pygame.draw.line(screen, RED,(500,0), [500,600], 10)
        return 2
    elif matriz_jogo[0][0]==matriz_jogo[1][1]=='O' and matriz_jogo[0][0]==matriz_jogo[2][2]=='O':
        pygame.draw.line(screen, RED,(0,0), [600,600], 10)
        return 2
    elif matriz_jogo[0][2]==matriz_jogo[1][1]=='O' and matriz_jogo[0][2]==matriz_jogo[2][0]=='O':
        pygame.draw.line(screen, RED,(600,0), [0,600], 10)
        return 2

# ----------------------- Função de vericação do jogador 1 ----------------------------
def jogadas_1(pos):    
    index_coluna= int(pos[0]/200)
    index_linha= int(pos[1]/200)
    if matriz_jogo[index_linha][index_coluna] =='_': 
        screen.blit(xis,(quadrante_linha[index_coluna],quadrante_coluna[index_linha]))
        matriz_jogo[index_linha][index_coluna] = 'X'
        return 0
    else:
        print("posicao ja ocupada!")           
        return -1
#-------------------------------------------------------------------------------------

#------------------------------Função do Jogador 2-------------------------------------
def jogadas_2(pos):
        index_coluna= int(pos[0]/200)
        index_linha = int(pos[1]/200)
        if matriz_jogo[index_linha][index_coluna]=='_':
            screen.blit(bola,(quadrante_linha[index_coluna],quadrante_coluna[index_linha]))
            matriz_jogo[index_linha][index_coluna] = 'O'
            return 0
        
        else:
            print("posicao ocupada!")
            return -1

#--------------------------------------------------------------------------------------------
while not done:
    ganhador = 0
    soma = 0
    mouse_pos = pygame.mouse.get_pos()   

      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             done = True
        # ---------------- pegando a posição com o click do mouse ---------------      
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos  = pygame.mouse.get_pos()
        #--------------------------------------------------------------------------    

        #-------------------- substituindo na tela e validação se ganhou---------------------------------
            if ( jogadas%2== 0):
                soma = jogadas_1(click_pos)
                jogadas = jogadas + 1 + soma
                ganhador = vitoria()
                print(ganhador)             
                if ganhador == 1:
                    print('vitoria')
                    done = True
                    vencedor = 100
                if ganhador == 2:
                    print('vitoria')
                    vencedor = 100
            elif (  jogadas%2 == 1):
                soma = jogadas_2(click_pos)
                jogadas = jogadas + 1 + soma
                ganhador = vitoria()
                print(ganhador)
        #--------------------------------------------------------------------------    
            
            if jogadas >=9:
                screen.fill(WHITE)
                screen.blit(velha,(200,250)) 
                break
    pygame.display.flip()

               
print(matriz_jogo)                
      # ------------------------------------------------------------------------  