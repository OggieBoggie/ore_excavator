import pygame

class Ore(pygame.sprite.Sprite):
    '''This class is for the clickable ore class
    The init constructor takes 3 attributes for:
        The image
        The x position
        The Y position'''
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
    
    def draw(self, screen):
        '''Draws ore sprite on the screen'''
        screen.blit(self.image, (self.x, self.y))