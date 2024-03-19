import pygame
import sys
import time
import random

# Game setup
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Snake and food setup
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [50, 50]
direction = 'RIGHT'
change_to = direction

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Direction validation
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_position = [60,60]
    else:
        snake_body.pop()

    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] > width-10:
        pygame.quit()
    if snake_position[1] < 0 or snake_position[1] > height-10:
        pygame.quit()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            pygame.quit()

    # Graphics
    screen.fill((0, 0, 0))
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Refresh game screen
    pygame.display.flip()
    # Frame rate
    clock.tick(30)
