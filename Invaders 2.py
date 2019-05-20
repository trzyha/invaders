import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Invaders')

BLACK = (0, 0, 0)
WHITE = (200, 255, 255)


animation_time = 100
reach_the_screen = 0

image_1 = pygame.image.load('invader1-1.png')#.convert_alpha()
image_2 = pygame.image.load('invader1-2.png')#.convert_alpha()
image_3 = pygame.image.load('invader1-3.png')#.convert_alpha()
image_4 = pygame.image.load('invader1-4.png')#.convert_alpha()


def invader(pos_x, pos_y):
    screen.blit(image_1, (pos_x,pos_y))
    pygame.display.update()
    pygame.time.wait(animation_time)
    pygame.draw.rect(screen, WHITE, (100,100,32,32))
    pygame.display.update()
        
    screen.blit(image_2, (pos_x, pos_y))
    pygame.display.update()
    pygame.time.wait(animation_time)
    pygame.draw.rect(screen, WHITE, (100,100,32,32))
    pygame.display.update()

    screen.blit(image_3, (pos_x, pos_y))
    pygame.display.update()
    pygame.time.wait(animation_time)
    pygame.draw.rect(screen, WHITE, (100,100,32,32))
    pygame.display.update()

    screen.blit(image_4, (pos_x, pos_y))
    pygame.display.update()
    pygame.time.wait(animation_time)
    pygame.draw.rect(screen, WHITE, (100,100,32,32))
    pygame.display.update()

    
gameLoop = True

while gameLoop:
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop = False
        
    screen.fill(WHITE)

    if reach_the_screen < 800:
        invader(100+reach_the_screen,100)
        reach_the_screen = reach_the_screen+1
    

    pygame.display.flip()
    
    

pygame.quit()

