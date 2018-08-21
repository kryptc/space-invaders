import pygame
from pygame.locals import *
import time

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Alien(pygame.sprite.Sprite):

    def __init__(self, row, col):
        super(Alien, self).__init__()
        self.image = pygame.image.load("alien1.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
        self.rect.x = row * 100 + 15
        self.rect.y = col * 100
        self.spawnTime = time.time()

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect) 

    def annihilate(self):
        if time.time() - self.spawnTime >= 8:
            self.kill()

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y


class frozenAlien(pygame.sprite.Sprite):

    alreadyFrozen = 0

    def __init__(self, row, col):
        super(frozenAlien, self).__init__()
        self.image = pygame.image.load("alien2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect()
      
        self.rect.x = row 
        self.rect.y = col
        self.spawnTime = time.time() 
        frozenAlien.alreadyFrozen = 0

    def annihilate(self):
        if time.time() - self.spawnTime >= 5:

            self.kill()

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y
