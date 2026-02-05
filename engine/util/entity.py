"""Loads entities from a given set of images

Typical usage example:
    from constants import ENTITIES
    entity_loader = EntityLoader()
    entity_loader.load(ENTITIES)
    entities = entity_loader.entities
"""
from entity.enemy import Enemy

import pygame

class EntityLoader:
    "Loads entities from a given set of images"
    def __init__(self):
        "Initializes an entity loader"
        self.images = {}
        self.entities = {}


    def load(self, images):
        """Loops through all entity types and image items to load the entities

        Args:
            images (dict): entity type to image items mapping
                           (see ENTITIES in constants.py for example)
        """
        for entity_key, image_items in images.items():
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
            self.entities[entity_key].add(Enemy((200, 300), image_path))
        #