import pygame

from itertools import cycle

class Pickaxe(pygame.sprite.Sprite):
    '''This class is for the pickaxe sprite
        The init constructor takes three default arguments
        for the pickaxe image
        for the x position of the pickaxe
        for the y postion of the pickaxe'''
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
    
    # draws the pickaxe sprite on the screen
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    # updates the postion of the sprite to follow the player's cursor
    def update_postion(self, x, y):
        self.x = (x - 20)
        self.y = (y - 20)