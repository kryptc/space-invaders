import pygame


class Background (pygame.sprite.Sprite):
    def __init__(self, image, location):
        super(Background, self).__init__()
        # pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = location[0]
        self.rect.top = location[1]
