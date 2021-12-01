import pygame
from pygame.locals import *
pygame.init()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
screen = pygame.display.set_mode((600, 600))
img = pygame.image.load("x.jpg")
screen.blit(pygame.transform.scale(img, (100, 100)),(0,0))
done = False
x=230 #largura da tela 
y = 200 #altura da tela
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
         
        screen.fill((0,0,45))
        pygame.draw.line(screen,  WHITE,(200,0), [200,600], 10)
        pygame.draw.line(screen, WHITE,(400,0), [400,600], 10)
        pygame.draw.line(screen, WHITE,(0,200), [600,200], 10)
        pygame.draw.line(screen, WHITE,(0,400), [600,400], 10)
        pygame.draw.rect(screen, (BLUE),pygame.Rect(x, y,150,150))        
        pygame.draw.circle(screen,(255,251,21),(50,50),70)

        pygame.display.flip()