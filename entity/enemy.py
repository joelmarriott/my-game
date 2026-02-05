"""The enemy sprite class

Typical usage example:
    Enemy((100, 100), pygame.surface.Surface)
"""
from engine.constants import WINDOW_WIDTH, WINDOW_HEIGHT
import pygame

class Enemy(pygame.sprite.Sprite):
    "The enemy sprite class"

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


    def update(self):
        "Updates the enemy"
        self.move()


    def move(self):
        """Moves the enemy
        
        Enemy moves across the screen and resets to the left once it
        reaches the right edge
        """
        self.rect.x += 1
        if self.rect.x > WINDOW_WIDTH - (self.rect.width / 2):
            self.rect.x = 0 - (self.rect.width / 2)
        #