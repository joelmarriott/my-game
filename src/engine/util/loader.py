"""Loads entities from a given set of images

Typical usage example:
    from constants import ENTITIES
    entity_loader = EntityLoader()
    entity_loader.load(ENTITIES)
    entities = entity_loader.entities
"""
from entity.enemy import Enemy
from entity.turret import Turret
from engine.constants import ENTITIES, TILE_SIZE

import logging, pygame

class Loader:
    "Loads entities from a given set of images"
    def __init__(self, level):
        "Initializes an entity loader"
        self.level = level
        self.images = {}
        self.entities = {}


    def load(self):
        "Loops through all entity types and image items to load the entities"
        for entity_key, image_items in ENTITIES.items():
            self.load_image_items(entity_key, image_items)
        #
        self.load_entities()


    def load_image_items(self, entity_key, image_items):
        """Loops through image items for an entity key and loads the image

        Args:
            entity_key  (str) : entity identifier (e.g. 'enemy')
            image_items (dict): key to path mapping for images
                             (e.g. {'enemy_1': 'asset/image/enemy/enemy_1.png'})
        """
        if entity_key not in self.images.keys():
            self.images[entity_key] = {}
        #
        for image_key, image_path in image_items.items():
            self.images[entity_key][image_key] = self.load_image(image_path)
        #


    def load_image(self, image_path):
        """Loads an image given it's path

        Args:
            image_path (str): Path to the image
                              (e.g. 'asset/image/enemy/enemy_1.png')

        Returns:
            pygame.surface.Surface: The loaded image as a pygame surface
        """
        return pygame.image.load(image_path).convert_alpha()


    def load_entities(self):
        "Loops through all entity types and image items to load the entities"
        for entity_key, image_items in self.images.items():
            self.group_entities(entity_key, image_items)


    def group_entities(self, entity_key, image_items):
        """Groups all entities for an entity_key

        Args:
            entity_key (str): entity identifier (e.g. 'enemy')
            image_items (dict): key to path mapping for surfaces
                             (e.g. {'enemy_1': pygame.surface.Surface})
        """
        if entity_key not in self.entities.keys():
            self.entities[entity_key] = pygame.sprite.Group()
        #
        for image_key in image_items.keys():
            image_path = self.images[entity_key][image_key]
            if entity_key == 'enemy':
                entity = Enemy(self.level.waypoints, image_path)
            else:
                return
            #
            self.entities[entity_key].add(entity)
        #
        
    
    def create_turret(self, x, y):
        """Creates a turret at the given coordinates

        Args:
            x (int): x coordinate of the turret
            y (int): y coordinate of the turret
        """
        tile_x = x // TILE_SIZE
        tile_y = y // TILE_SIZE
        if self.level.map[tile_y][tile_x] != 'GRF':
            logging.warning(f'Tile position ({tile_x}, {tile_y}) '\
                'is not buildable')
            return
        #
        for turret in self.entities['turret']:
            if turret.tile_x == tile_x and turret.tile_y == tile_y:
                logging.warning(f'Tile position ({tile_x}, {tile_y}) '\
                    'is occupied by another turret')
                return
            #
        #
        logging.info(f'Creating turret at tile position ({tile_x}, {tile_y})')
        turret = Turret(tile_x, tile_y, self.images['turret']['turret_1'])
        self.entities['turret'].add(turret)