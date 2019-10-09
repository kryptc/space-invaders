import pygame
# from alien import *
from miscVariables import *
from missiles import *
from miscFunctions import *


class spaceshipClass (pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super(spaceshipClass, self).__init__()

        self.image = pygame.Surface((width, height))

        # self.image.fill (WHITE)
        # self.image.set_colorkey (WHITE) # make the background transparent

        self.image = pygame.image.load(
            'fly-launch-rocket-space-spaceship-start-startup-35de16d292d4dc39-512x512.png')
        self.image = pygame.transform.scale(self.image, (100, 100))

        # pygame.draw.polygon(self.image, color, ((45, 10), (10, 90), (90, 90)))

        self.rect = self.image.get_rect()

    def moveRight(self, byHowMuch):
        if self.rect.x < 700:
            self.rect.x += byHowMuch
        else:
            self.rect.x -= 700
        # if self.rect.x == 700:
            # self.rect.x -= 700

    def moveLeft(self, byHowMuch):
        if self.rect.x > -40:
            self.rect.x -= byHowMuch
        else:
            self.rect.x = 700

    def makeSmallMissile(self):
        smallMissile = smallMissileClass(100, 100)
        smallMissile.rect.x = self.rect.x + 10
        smallMissile.rect.y = self.rect.y - 90
        return smallMissile

    def makeBigMissile(self):
        bigMissile = BigMissileClass(100, 100)
        bigMissile.rect.x = self.rect.x
        bigMissile.rect.y = self.rect.y - 100
        return bigMissile


spaceship = spaceshipClass(800, 800, RED)
spaceship.rect.x = 0
spaceship.rect.y = 800
