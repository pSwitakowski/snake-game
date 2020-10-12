import time

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

font_style = pygame.font.SysFont(None, 50)


def message(text, color):
    message = font_style.render(text, True, color)
    screen.blit(message, [int(config.WIDTH/2) - 100, int(config.HEIGHT/2)])


crashed = False
while not crashed:
    dt = clock.tick(config.FPS) / 1000

    if snake.crashed:
        crashed = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.set_direction('RIGHT')
            elif event.key == pygame.K_LEFT:
                snake.set_direction('LEFT')
            elif event.key == pygame.K_UP:
                snake.set_direction('UP')
            elif event.key == pygame.K_DOWN:
                snake.set_direction('DOWN')


    screen.fill(config.BACKGROUND)
    snake.update()

    screen.blit(snake.image, snake.rect)
    pygame.display.update()




message("GAME OVER", (255, 0, 0))
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()