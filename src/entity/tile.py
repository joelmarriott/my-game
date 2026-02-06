"""The tile class

Typical usage example:
    Tile('BEF')
    See TILES in constants.py
"""
from engine.constants import TILE_SIZE
from pygame.surface import Surface

import pygame

class Tile(Surface):
    "The tile class"

    def __init__(self, image_path):
        """Initialises a tile

        Args:
            image (str): Path to the image for this tile
        """
        Surface.__init__(self, (TILE_SIZE, TILE_SIZE))
        self.image = pygame.image.load(image_path).convert_alpha()
