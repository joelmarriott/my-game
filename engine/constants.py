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


WINDOW_WIDTH = 528
WINDOW_HEIGHT = 528
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
                [ 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF' ],

                [ 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF' ],
            
                [ 'GRF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'GRF', 'GRF' ],
            
                [ 'GRF', 'PAF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF' ],
            
                [ 'GRF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'GRF' ],
            
                [ 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'PAF', 'GRF' ],
            
                [ 'GRF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'GRF' ],
            
                [ 'GRF', 'PAF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF' ],
            
                [ 'GRF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'PAF', 'GRF', 'GRF' ],

                [ 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF' ],
            
                [ 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'GRF', 'PAF', 'GRF', 'GRF' ]
            ],
            'waypoints': [
                (100, 100),
                (400, 200),
                (400, 100),
                (200, 300)
            ]    
        }
}
TILE_SIZE = 48
TILES = {
    'BEF': image_path('tile', 'beach_full.png'),
    'DIF': image_path('tile', 'dirt_full.png'),
    'GRF': image_path('tile', 'grass_full.png'),
    'PAF': image_path('tile', 'path_full.png')
}