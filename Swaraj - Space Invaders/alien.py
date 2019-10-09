import pygame
from miscVariables import *
from miscFunctions import *


class alienClass (pygame.sprite.Sprite):
    def __init__(self, width, height, location):
        super(alienClass, self).__init__()

        self.width = width
        self.height = height
        # self.color = color

        self.image = pygame.Surface((width, height))

        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # if lifetime == 20:
        self.image = pygame.image.load('imageedit_11_9306499499.jpg')
        # else:
        # self.image = pygame.image.load('imageedit_11_9306499499.jpg')

        self.image = pygame.transform.scale(self.image, (80, 80))

        self.lifetime = 20

        # pygame.draw.rect (self.image, self.color, [0, 0, width, height])

        self.rect = self.image.get_rect()

        self.rect.x = location[0]
        self.rect.y = location[1]

    def returnLocation(self):
        return (self.rect.x, self.rect.y)

    def returnLifetime(self):
        return self.lifetime

    def reduceLifetime(self):
        self.lifetime -= 1

    def increaseLifetime(self):
        self.lifetime += 5

    def gotHitByBigMissile(self):
        # pass
        self.image = pygame.Surface((self.width, self.height))
        self.image = pygame.image.load('imageedit_13_2318882770.jpg')
        self.image = pygame.transform.scale(self.image, (80, 80))
