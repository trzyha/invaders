import pygame
import sys

WHITE = (255,255,255)

resolution = (800,600)
game_over = False

screen = pygame.display.set_mode(resolution)

carImg = pygame.image.load('inv1.gif')

def invader(x,y):
    screen.blit(carImg, (x, y))



while not game_over:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    invader(100,100)
    pygame.display.flip()
