import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Invaders')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

image = pygame.image.load('\assets\invader1-1.png').convert_alpha()



gameLoop = True

while gameLoop:
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop = False

    screen.fill(BLACK)

    screen.blit(image, (10,10))
    pygame.display.flip()

pygame.quit()

