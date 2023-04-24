import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
AQUA = (0, 255, 255)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# sets screen size
window = pygame.display.set_mode((500, 500))

# loads image of ore pictures
ore_image = pygame.image.load("ore.png")

# loads image of pickaxe
pickaxe_image = pygame.image.load("pickaxe0.png")