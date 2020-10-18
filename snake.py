import pygame
import config
import random

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
        self.image.fill(((random.randrange(0, 255)), random.randrange(0, 255), random.randrange(0, 255)))

        self.head = self.image.get_rect()
        self.head.x = (config.WIDTH / 2) - self.width
        self.head.y = (config.HEIGHT / 2) - self.height

        self.body = []
        self.body.insert(0, self.head)
        self.length = 1

        self.direction = [0, 0]
        self.crashed = False
        self.movable = True

    def update(self):
        at_left_border = self.body[0].x < 0
        at_right_border = self.body[0].x + self.width > config.WIDTH
        at_top_border = self.body[0].y < 0
        at_bottom_border = self.body[0].y + self.height > config.HEIGHT

        self.crashed = at_left_border or at_right_border or at_top_border or at_bottom_border

        if not self.crashed:
            new_part = pygame.rect.Rect((self.body[0].x + self.direction[0], self.body[0].y + self.direction[1]), (20, 20))
            # new_part.x = self.body[0].x + self.direction[0]
            # new_part.y = self.body[0].y + self.direction[1]

            del self.body[-1]

            self.body.insert(0, new_part)
            self.head = self.body[0]

            print(self.body)
            # self.head.move_ip(*self.direction)
            # print(f"snake head pos: ({self.head.x},{self.head.y})")

    def set_direction(self, new_direction):
        if self.movable:
            if new_direction == "RIGHT":
                if self.direction != LEFT:
                    self.direction = RIGHT
                    self.movable = False
            elif new_direction == "LEFT":
                if self.direction != RIGHT:
                    self.direction = LEFT
                    self.movable = False
            elif new_direction == "UP":
                if self.direction != DOWN:
                    self.direction = UP
                    self.movable = False
            elif new_direction == "DOWN":
                if self.direction != UP:
                    self.direction = DOWN
                    self.movable = False

    def increase_tail(self, food):

        # increase snake length on screen
        new_image = food.image.copy()
        new_part = new_image.get_rect()

        new_part.x = self.body[0].x + self.direction[0]
        new_part.y = self.body[0].y + self.direction[1]
        self.body.insert(0, new_part)
        self.head = self.body[0]

        self.length += 1
        print('YUMMY')

    def check_self_crash(self):
        if len(self.body) > 1:
            for part in self.body[1:]:
                if self.head == part:
                    self.crashed = True
        # for part in self.body:
        #     print(part.image.get_at(1,1), ',')