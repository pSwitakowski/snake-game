import pygame
from snake import *
import config


pygame.init()
pygame.display.set_caption('giereczka')

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
screen.fill(config.BACKGROUND)
pygame.display.update()

clock = pygame.time.Clock()

snake = Snake()


crashed = False
while not crashed:
    dt = clock.tick(config.FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.set_velocity('RIGHT')
            elif event.key == pygame.K_LEFT:
                snake.set_velocity('LEFT')
            elif event.key == pygame.K_UP:
                snake.set_velocity('UP')
            elif event.key == pygame.K_DOWN:
                snake.set_velocity('DOWN')

    print("at_border: ", snake.at_borders)
    print("velocity: ", snake.velocity)

    screen.fill(config.BACKGROUND)
    snake.update()

    screen.blit(snake.image, snake.rect)
    pygame.display.update()


pygame.quit()
quit()