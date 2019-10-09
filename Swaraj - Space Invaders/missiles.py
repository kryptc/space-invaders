import pygame
from miscVariables import *
from miscFunctions import *


class missile (pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(missile, self).__init__()

        self.width = width
        self.height = height

        self.image = pygame.Surface((width, height))

        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

    def moveUp(self, byHowMuch):
        if self.missileType == 'small':
            self.rect.y -= byHowMuch
        else:
            if self.rect.y != 100:
                self.rect.y -= 2 * byHowMuch
            else:
                self.rect.y -= byHowMuch


class smallMissileClass (missile):
    # def moveUp (self, byHowMuch):
    # 	self.rect.y -= byHowMuch

    def __init__(self, width, height):
        # super (smallMissileClass, self).__init__(self, width, height)
        missile.__init__(self, width, height)

        self.missileType = 'small'

        # self.image = pygame.Surface((width, height))

        # self.image.fill (WHITE)
        # self.image.set_colorkey (WHITE)

        self.image = pygame.image.load('bullet_ammunition_army_shoot-512.png')
        self.image = pygame.transform.scale(self.image, (80, 80))

        # pygame.draw.circle (self.image, color, (50, 50), 20, 10)

        self.rect = self.image.get_rect()


class BigMissileClass (missile):
    # def moveUp (self, byHowMuch):
    # 	if self.rect.y != 100:
    # 		self.rect.y -= 2 * byHowMuch
    # 	else:
    # 		self.rect.y -= byHowMuch

    def __init__(self, width, height):
        # super (BigMissileClass, self).__init__(self, width, height)
        missile.__init__(self, width, height)

        self.missileType = 'big'

        # self.width = width
        # self.height = height

        # self.image = pygame.Surface((width, height))

        # self.image.fill (WHITE)
        # self.image.set_colorkey (WHITE)

        self.image = pygame.image.load('imageedit_36_6827120959.png')
        self.image = pygame.transform.scale(self.image, (80, 80))

        # pygame.draw.circle (self.image, color, (50, 50), 40, 10)

        self.rect = self.image.get_rect()
