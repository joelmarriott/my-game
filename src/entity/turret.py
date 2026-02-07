"""The turret sprite class

Typical usage example:
    Turret(1, 1, pygame.surface.Surface)
"""
from pygame.sprite import Sprite
from engine.constants import TILE_SIZE

class Turret(Sprite):
    "The turret sprite class"

    def __init__(self, tile_x, tile_y, image):
        """Initialises a turret

        Args:
            tile_x (int): x coordinate of the turret tile
            tile_y (int): y coordinate of the turret tile
            image (pygame.surface.Surface): image for the turret
        """
        Sprite.__init__(self)
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.x = (self.tile_x + 0.5) * TILE_SIZE
        self.y = (self.tile_y + 0.5) * TILE_SIZE
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
