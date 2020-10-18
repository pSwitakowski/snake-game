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




game_over_font = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 100)


def show_game_over_text():
    message = game_over_font.render('Game over! R - restart   Q - quit', True, (255, 0, 0))
    screen.blit(message, [int(config.WIDTH/2) - int(message.get_width()/2), int(config.HEIGHT/4)])


def show_score_text(score):
    message = score_font.render(score, True, (255, 223, 0))
    screen.blit(message, [int(config.WIDTH/2) - int(message.get_width()/2), 20])


def game_loop():
    snake = Snake()
    food = Food()

    game_lost = False
    game_quit = False

    while not game_quit:
        clock.tick(config.FPS)
        snake.movable = True
        # pygame.display.update()

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

        snake.check_self_crash()

        if snake.crashed:
            game_lost = True

        while game_lost:
            screen.fill(config.BACKGROUND)
            show_game_over_text()
            show_score_text(str(snake.length-1))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        config.FPS = 10
                        game_loop()
                    elif event.key == pygame.K_q:
                        game_lost = False
                        game_quit = True
                        break



        screen.fill(config.BACKGROUND)
        # ---------------------------


        snake.update()
        for part in snake.body:
            screen.blit(snake.image, [part.x, part.y])

        # check food collision
        if snake.head == food:
            config.FPS += 1
            food = Food()
            snake.increase_tail(food)

        show_score_text(str(snake.length-1))

        food.update()
        screen.blit(food.image, food.rect)

        # ----------------------------
        pygame.display.update()


game_loop()

pygame.quit()
quit()