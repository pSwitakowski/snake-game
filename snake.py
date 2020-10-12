import pygame
import enum
import config

SPEED = 20

LEFT = [-SPEED, 0]
RIGHT = [SPEED, 0]
UP = [0, -SPEED]
DOWN = [0, SPEED]


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 20
        self.height = 20
        self.image = pygame.Surface((self.width, self.height))
        self.default_color = (0, 230, 50, 220)
        self.image.fill(self.default_color)
        self.rect = self.image.get_rect()
        self.rect.x = (config.WIDTH / 2) - self.width
        self.rect.y = (config.HEIGHT / 2) - self.height
        self.direction = [0, 0]
        self.crashed = False

    def update(self):
        print("snake pos: (", self.rect.x, ',', self.rect.y, ')')

        at_left_border = self.rect.x <= 0
        at_right_border = self.rect.x + self.width >= config.WIDTH
        at_top_border = self.rect.y <= 0
        at_bottom_border = self.rect.y + self.height >= config.HEIGHT

        self.crashed = at_left_border or at_right_border or at_top_border or at_bottom_border

        if not self.crashed:
            self.rect.move_ip(*self.direction)

    def set_direction(self, new_direction):
        if new_direction == "RIGHT":
            self.direction = RIGHT
        elif new_direction == "LEFT":
            self.direction = LEFT
        elif new_direction == "UP":
            self.direction = UP
        elif new_direction == "DOWN":
            self.direction = DOWN

