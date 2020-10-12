import pygame
import random
import config


class Food(pygame.sprite.Sprite):
    def __init__(self):
        self.width = 20
        self.height = 20

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((120, 60, 200))

        self.rect = self.image.get_rect()
        self.rect.x = random.choice([i for i in range(0, config.WIDTH+20, 20)])
        self.rect.y = random.choice([i for i in range(0, config.HEIGHT+20, 20)])
