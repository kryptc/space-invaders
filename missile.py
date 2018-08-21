import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

width = 10
height = 80

class Missile(pygame.sprite.Sprite):

    def __init__(self):
        super(Missile, self).__init__()

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect) 

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    def burnUp(self):
        self.kill()


class MissileA(Missile):

    colour = RED

    def __init__(self, position):
        super(MissileA, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, MissileA.colour, [0, 0, width, height])  
        self.rect = self.image.get_rect()
        self.rect.x = position + 45
        self.rect.y = 610

    def moveUp(self):
        if self.rect.y < 0:
            self.burnUp()
        else:
            self.rect.move_ip(0, - 5)

    def draw(self, screen):
        super(MissileA, self).draw(screen)

    def burnUp(self):
        super(MissileA, self).burnUp()



class MissileB(Missile):

    colour = BLUE

    def __init__(self, position):
        super(MissileB, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, MissileB.colour, [0, 0, width, height])  
        self.rect = self.image.get_rect()
        self.rect.x = position + 45
        self.rect.y = 600

    def moveUp(self):
        if self.rect.y < 0:
            self.burnUp()
        else:
            self.rect.move_ip(0, -10)

    def draw(self, screen):
        super(MissileB, self).draw(screen)

    def burnUp(self):
        super(MissileB, self).burnUp()

    def isCollide(self, sprite):
        return self.rect.colliderect(sprite.rect)
