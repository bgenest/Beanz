import pygame
pygame.init()

# Set the dimensions of the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
