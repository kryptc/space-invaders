import pygame
from pygame.locals import *

BLACK = (0, 0, 0)

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, width, height):

        super(Spaceship, self).__init__()

        self.image = pygame.image.load("fighter.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = height


    def moveRight(self, pixels):
        if self.rect.right >= 800:
            self.rect.right = 800
        else:
            self.rect.move_ip(pixels, 0)

    def moveLeft(self, pixels):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.move_ip(-1 * pixels, 0)

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y
        
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect) 
