"""The turret sprite class

Typical usage example:
    Turret((100, 100), pygame.surface.Surface)
"""
from pygame.sprite import Sprite

class Turret(Sprite):
    "The turret sprite class"

    def __init__(self, position, image):
        """Initialises a turret

        Args:
            position (tuple): x,y position of the turret (e.g. (100, 100))
            image (pygame.surface.Surface): image for the turret
        """
        Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
