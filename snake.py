import pygame
import enum
import config

LOW = config.WIDTH / 50
# MEDIUM = 2 * LOW
# FAST = 3 * LOW
# EXPERT = 4 * LOW

LEFT = [-config.WIDTH / 50, 0]
RIGHT = [config.WIDTH / 50, 0]
UP = [0, -config.WIDTH / 50]
DOWN = [0, config.WIDTH / 50]


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.default_color = (0, 230, 50, 220)
        self.image.fill(self.default_color)
        self.rect = self.image.get_rect()
        self.rect.x = config.WIDTH / 2
        self.rect.y = config.HEIGHT / 2
        self.at_border = False

        self.velocity = UP

    def update(self):

        at_left_border = self.rect.x <= 0
        at_right_border = self.rect.x + self.width >= config.WIDTH
        at_top_border = self.rect.y <= 0
        at_bottom_border = self.rect.y + self.height >= config.HEIGHT
        self.at_border = [at_left_border, at_right_border, at_top_border, at_bottom_border]

        if True not in self.at_border:
            self.rect.move_ip(*self.velocity)


    def reset_at_border(self):
        self.at_border = [False, False, False, False]

    def set_velocity(self, new_direction):
        if new_direction == "RIGHT":
            self.reset_at_border()
            self.velocity = RIGHT
        elif new_direction == "LEFT":
            self.reset_at_border()
            self.velocity = LEFT
        elif new_direction == "UP":
            self.reset_at_border()
            self.velocity = UP
        elif new_direction == "DOWN":
            self.reset_at_border()
            self.velocity = DOWN

