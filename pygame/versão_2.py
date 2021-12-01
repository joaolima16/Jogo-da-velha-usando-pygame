import pygame
from pygame.locals import *
pygame.init()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
screen = pygame.display.set_mode((600, 600))
img_x = pygame.image.load("x.png")
img_O = pygame.image.load("O.png")
img_x = pygame.transform.scale(img_x,(100,100))
img_O = pygame.transform.scale(img_O,(100,100))
done = False
x=230 #largura da tela 
y = 200 #altura da tela
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
         
        
        screen.fill(WHITE)
        screen.blit(img_x,(100,500))
        screen.blit(img_O,(150,400))
        pygame.draw.line(screen, BLACK,(200,0), [200,600], 10)
        pygame.draw.line(screen, BLACK,(400,0), [400,600], 10)
        pygame.draw.line(screen, BLACK,(0,200), [600,200], 10)
        pygame.draw.line(screen, BLACK,(0,400), [600,400], 10)
        pygame.display.flip()