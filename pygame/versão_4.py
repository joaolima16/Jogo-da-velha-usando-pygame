import pygame
from pygame.locals import *
pygame.init()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
screen = pygame.display.set_mode((600, 600))
altura  = screen.get_height()
largura = screen.get_width()
print(altura)
print(largura)
img_x = pygame.image.load("x.png")  #Criando a imagem x usada no jogo
img_O = pygame.image.load("O.png") #criando a imagem O usada no jogo
img_x = pygame.transform.scale(img_x,(100,100)) #definindo o tamanho dela
img_O = pygame.transform.scale(img_O,(100,100))
done = False
x=230 #largura da tela 
y = 200 #altura da tela
# ------- Inicia o jogo -------
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
# ---------------------------------------------         
        
        screen.fill(WHITE) #define a cor de fundo da tela
        
        
        # ---- posisão da primeira coluna----------------- 
        screen.blit(img_x,(50,50))
        screen.blit(img_O,(250,50))
        screen.blit(img_x,(450,50))

        # ---------------posição da segunda coluna----------
        
        screen.blit(img_x,(50,250))
        screen.blit(img_x,(250,250))
        screen.blit(img_O,(450,250))


        # ------ posição da terceira coluna------------
        screen.blit(img_x,(50,450))
        screen.blit(img_x,(250,450))
        screen.blit(img_x,(450,450))        
      #--------------------- criando as linhas do jogo ------------------------  
        pygame.draw.line(screen, BLACK,(200,0), [200,600], 10)
        pygame.draw.line(screen, BLACK,(400,0), [400,600], 10)
        pygame.draw.line(screen, BLACK,(0,200), [600,200], 10)
        pygame.draw.line(screen, BLACK,(0,400), [600,400], 10)
        
      #---------------------------------------------------------------------------   
        
        pygame.display.flip() 
