import time

import pygame
from snake import *
import config
from food import *


pygame.init()
pygame.display.set_caption('giereczka')

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
screen.fill(config.BACKGROUND)
pygame.display.update()

clock = pygame.time.Clock()




font_style = pygame.font.SysFont(None, 50)


def message(text, color):
    message = font_style.render(text, True, color)
    screen.blit(message, [int(config.WIDTH/5), int(config.HEIGHT/4)])

def game_loop():
    snake = Snake()
    food = Food()

    game_lost = False
    game_quit = False

    while not game_quit:
        clock.tick(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.set_direction('RIGHT')
                elif event.key == pygame.K_LEFT:
                    snake.set_direction('LEFT')
                elif event.key == pygame.K_UP:
                    snake.set_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.set_direction('DOWN')
                elif event.key == pygame.K_DOWN:
                    snake.set_direction('DOWN')



        screen.fill(config.BACKGROUND)
        snake.update()
        screen.blit(snake.image, snake.head)

        if(snake.head.x == food.rect.x and snake.head.y == food.rect.y):
            food = Food()
            snake.increase_tail()

        if snake.crashed: game_lost = True
        while game_lost:
            screen.fill(config.BACKGROUND)
            message('Game over! R - restart   Q - quit', (255, 0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_loop()
                    elif event.key == pygame.K_q:
                        game_quit = True
                        game_lost = False
                        break

        food.update()
        screen.blit(food.image, food.rect)

        pygame.display.update()


game_loop()

pygame.quit()
quit()