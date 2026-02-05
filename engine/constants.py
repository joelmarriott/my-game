"""Constants for the game

Typical usage example:
    from constants import WINDOW_WIDTH
    print(WINDOW_WIDTH)
"""
import os


def image_path(entity_type, image_key):
    """Returns the image path given the entity type and image key

    Args:
        entity_type (str): Entity type (e.g. 'enemy')
        image_key   (str): image key (e.g. 'enemy_1')

    Returns:
        str: os safe path to the image (e.g. 'asset/image/enemy/enemy_1.png')
    """
    return os.path.join('asset', 'image', entity_type, image_key)


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FPS = 60
ENTITIES = {
    'enemy': {
        'enemy_1': image_path('enemy', 'enemy_1.png'),
    }
}