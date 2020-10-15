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
        self.image.fill((0, 230, 50))

        self.head = self.image.get_rect()
        self.head.x = (config.WIDTH / 2) - self.width
        self.head.y = (config.HEIGHT / 2) - self.height
        self.tail = []
        self.length = 1

        self.direction = [0, 0]
        self.crashed = False

    def update(self):
        at_left_border = self.head.x < 0
        at_right_border = self.head.x + self.width > config.WIDTH
        at_top_border = self.head.y < 0
        at_bottom_border = self.head.y + self.height > config.HEIGHT

        self.crashed = at_left_border or at_right_border or at_top_border or at_bottom_border

        if not self.crashed:
            self.head.move_ip(*self.direction)
            print("snake pos: (", self.head.x, ',', self.head.y, ')')

    def set_direction(self, new_direction):
        if new_direction == "RIGHT":
            if self.direction != LEFT:
                self.direction = RIGHT
        elif new_direction == "LEFT":
            if self.direction != RIGHT:
                self.direction = LEFT
        elif new_direction == "UP":
            if self.direction != DOWN:
                self.direction = UP
        elif new_direction == "DOWN":
            if self.direction != UP:
                self.direction = DOWN

    def increase_tail(self):
        self.length += 1
        print('YUMMY')