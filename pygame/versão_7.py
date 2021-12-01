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
    


def vitoria():
            if matriz_jogo[0][0] =="X" and matriz_jogo[0][1] == "X" and matriz_jogo [0][2] == "X":
                return 1       
                
            elif matriz_jogo[0][0] =="O" and matriz_jogo[0][1] == "O" and matriz_jogo [0][2] == "O":
                return 2       
                
            elif matriz_jogo[1][0] =="X" and matriz_jogo [1][1] == "X" and matriz_jogo [1][2] =="X":
                return 1       
                
            elif matriz_jogo[1][0] =="O" and matriz_jogo [1][1] == "O" and matriz_jogo [1][2] =="O":
                    return 2       
                
            elif matriz_jogo[2][0] =="X" and matriz_jogo[2][1] == "X" and matriz_jogo [2][2]=="X":
                    return 1       
            
            elif matriz_jogo[2][0] =="O" and matriz_jogo[2][1] == "O" and matriz_jogo [2][2]=="O":
                    return 2       
                
            elif matriz_jogo[0][0]=="X" and matriz_jogo[1][0]=="X" and matriz_jogo[2][0]=="X":
                    return 1                                
                
            elif matriz_jogo[0][0]=="O" and matriz_jogo[1][0]=="O" and matriz_jogo[2][0]=="O":
                return 2       
                
            elif matriz_jogo[1][0]=="X" and matriz_jogo[1][1]=="X" and matriz_jogo[1][2]=="X":         
                    return 1              
                
            elif matriz_jogo[1][0]=="O" and matriz_jogo[1][1]=="O" and matriz_jogo[1][2]=="O":          
                    return 2        
                
            elif matriz_jogo[2][0]=="O" and matriz_jogo[2][1]=="O" and matriz_jogo[2][2]=="O":      
                    return 2   
                
            elif matriz_jogo[0][0]=="X" and matriz_jogo[1][1]=="X" and matriz_jogo[2][2]=="X":
                    return 1 
                
            elif matriz_jogo[0][0]=="O" and matriz_jogo[1][1]=="O" and matriz_jogo[2][2]=="O":
                    return 2
                
            elif matriz_jogo[0][0]=="X" and matriz_jogo[1][0]=="X" and matriz_jogo[2][0]=="X":
                    return 1 
                
            elif matriz_jogo[0][0]=="O" and matriz_jogo[1][0]=="O" and matriz_jogo[2][0]=="O":
                    return 2
                
            elif matriz_jogo[0][2]=="X" and matriz_jogo[1][2]=="X" and matriz_jogo[2][2]=="X":
                    return 1
                
            elif matriz_jogo[0][2]=="O" and matriz_jogo[1][2]=="O" and matriz_jogo[2][2]=="O":
                    return 2
                
            elif matriz_jogo[0][1]=="X" and matriz_jogo[1][1]=="X" and matriz_jogo[2][1]=="X":
                    return 1         
                
            elif matriz_jogo[0][1]=="O" and matriz_jogo[1][1]=="O" and matriz_jogo[2][1]=="O":
                    return 2
                
            elif matriz_jogo[0][0]=="X" and matriz_jogo[1][0]=="X" and matriz_jogo[2][0]=="X":
                    return 2
                
            elif matriz_jogo[0][0]=="O" and matriz_jogo[0][1]=="O" and matriz_jogo[0][2]=="O":
                    return 2
                
            elif matriz_jogo[0][0] == "X" and matriz_jogo[0][1] == "X" and matriz_jogo[0][2] == "X":
                    return 1
                
            elif matriz_jogo[0][0]== "X" and matriz_jogo[1][0]== "X" and matriz_jogo[2][0]== "X":
                    return 1
                
            elif matriz_jogo[0][0]== "O" and matriz_jogo[1][0]== "O" and matriz_jogo[2][0]== "O":
                    return 2
                
            elif matriz_jogo[0][1]=="X" and matriz_jogo[1][1]== "X" and matriz_jogo[2][1]== "X":
                    return 1
                
            elif matriz_jogo[0][1]=="O" and matriz_jogo[1][1]== "O" and matriz_jogo[2][1]== "O":
                    return 2
                
            elif matriz_jogo[0][2]== "X" and matriz_jogo[1][2]== "X" and matriz_jogo[2][2]== "X":
                    return 1
                
            elif matriz_jogo[0][2] == "O" and matriz_jogo[1][2] == "O" and matriz_jogo[2][2] == "O":
                    return 2

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
             
            if ( jogadas%2== 0):
                soma = jogadas_1(click_pos)
                jogadas = jogadas + 1 + soma
                ganhador = vitoria()
                print(ganhador)             
                if ganhador == 1:
                    print('vitoria')
                    done = True
                if ganhador == 2:
                    print('vitoria')
                    done = True
            elif (  jogadas%2 == 1):
                soma = jogadas_2(click_pos)
                jogadas = jogadas + 1 + soma
                ganhador = vitoria()
                print(ganhador)
    
            if jogadas >=9:
                 done= True
                 break
    pygame.display.flip()

               
print(matriz_jogo)                
      # ------------------------------------------------------------------------          