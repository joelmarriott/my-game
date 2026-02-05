"""The game controller

Typical usage example:
    Game()
"""
import pygame

class Enemy(pygame.sprite.Sprite):
    """Main game controller
    
    Attributes:
        screen (pygame.Surface)   : The rendered screen
        clock  (pygame.time.Clock): The clock
        run    (boolean)          : Controls game loop 
    """

    def __init__(self, position, image):
        """Initialises an enemy

        Args:
            position (tuple): x,y position of the enemy (e.g. (100, 100))
            image (pygame.surface.Surface): image for the enemy
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
