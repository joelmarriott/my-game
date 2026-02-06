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


ROWS = 15
COLUMNS = 15
TILE_SIZE = 48

WINDOW_WIDTH = TILE_SIZE * COLUMNS
WINDOW_HEIGHT = TILE_SIZE * ROWS
FPS = 60
ENTITIES = {
    'enemy': {
        'enemy_1': image_path('enemy', 'enemy_1.png'),
    }
}
LEVELS = {
    'level_1': 
        {
            'map': [
                [ 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF' ],
                
                [ 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF' ],
                
                [ 'GRF', 'GRF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'GRF', 'GRF' ],
                
                [ 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF' ],
                
                [ 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF' ],
                
                [ 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'GRF', 'GRF' ],
                
                [ 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF' ],
                
                [ 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF' ],
                
                [ 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF' ],
                
                [ 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'GRF', 'GRF' ],
                
                [ 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF' ],
                
                [ 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF' ],
                
                [ 'GRF', 'GRF', 'PAF', 'PAF', 'PAF', 'PAF', 'GRF', 'GRF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF' ],
                
                [ 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF' ],
                
                [ 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF' ],
            ],
            'waypoints': [
                (13, -1),
                (13, 3),
                (3, 3),
                (3, 13),
                (6, 13),
                (6, 6),
                (13, 6),
                (13, 10),
                (9, 10),
                (9, 13),
                (16, 13)
            ]    
        }
}
TILES = {
    'BEF': image_path('tile', 'beach_full.png'),
    'DIF': image_path('tile', 'dirt_full.png'),
    'GRF': image_path('tile', 'grass_full.png'),
    'PAF': image_path('tile', 'path_full.png')
}