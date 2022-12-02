import pygame
pygame.init()
black = (0,0,0)
size = (700,600)
screen = pygame.pygame.display.set_mode(size)
clock = pygame.time.Clock()

done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
    
