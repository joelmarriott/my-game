"""Constants for the game

Typical usage example:
    from constants import WINDOW_WIDTH
    print(WINDOW_WIDTH)
"""
from pathlib import Path
import os


ROOT = Path(__file__).parent.parent


def asset_path(asset_type, entity_type, asset_key):
    """Returns the asset path given the entity type and image key

    Args:
        asset_type  (str): Asset type (e.g. 'image')
        entity_type (str): Entity type (e.g. 'enemy')
        asset_key   (str): Asset key (e.g. 'enemy_1.png')

    Returns:
        str: os safe path to the image (e.g. 'asset/image/enemy/enemy_1.png')
    """
    return os.path.join(ROOT, 'asset', asset_type, entity_type, asset_key)


ROWS = 15
COLUMNS = 15
TILE_SIZE = 48

PLAYAREA_WIDTH = TILE_SIZE * COLUMNS
PLAYAREA_HEIGHT = TILE_SIZE * ROWS

WINDOW_WIDTH = PLAYAREA_WIDTH + 200
WINDOW_HEIGHT = TILE_SIZE * ROWS

FPS = 60
ENTITIES = {
    'enemy': {
        'enemy_1': asset_path('image', 'enemy', 'enemy_1.png'),
    },
    'turret': {
        'turret_1': asset_path('image', 'turret', 'turret_1.gif'),
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
    'BEF': asset_path('image', 'tile', 'beach_full.png'),
    'DIF': asset_path('image', 'tile', 'dirt_full.png'),
    'GRF': asset_path('image', 'tile', 'grass_full.png'),
    'PAF': asset_path('image', 'tile', 'path_full.png')
}