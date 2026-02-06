"""The level class

Typical usage example:
    self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    level_1 = Level('level_1')
    level_1.load()
    while 1:
        level_1.draw(screen)
"""
from engine.constants import LEVELS, TILES, TILE_SIZE
from entity.tile import Tile

class Level():
    "The level class"

    def __init__(self, level_id):
        """"Initializes a level instance"

        Args:
            waypoints (list): x,y tuple coordinates for enemy entities to follow
        """
        level_config = LEVELS[level_id]
        self.waypoints = self.to_coordinates(level_config['waypoints'])
        self.map = level_config['map']
        self.tiles = {}
    

    def load(self):
        "Loads the map data/images"
        for map_row in self.map:
            for map_tile_id in map_row:
                if map_tile_id not in self.tiles.keys():
                    self.tiles[map_tile_id] = Tile(TILES[map_tile_id])
                #
            #
        #


    def draw(self, screen):
        """Draws the tiles on the screen using previously loaded data

        Args:
            screen (pygame.display): The currently rendered pygame screen
        """
        for map_row_index, map_row in enumerate(self.map):
            for map_column_index, tile in enumerate(map_row):
                x = map_column_index * TILE_SIZE
                y = map_row_index * TILE_SIZE
                screen.blit(self.tiles[tile].image, (x, y))
            #
        #
        
        
    def to_coordinates(self, waypoints):
        """Converts tile waypoints to pixel coordinates

        Args:
            waypoints (list): x,y tuple coordinates of tiles

        Returns:
            list: x,y tuple coordinates of tile centers (pixels)
        """
        coordinates = []
        for waypoint in waypoints:
            x = waypoint[0] * TILE_SIZE - (TILE_SIZE / 2)
            y = waypoint[1] * TILE_SIZE - (TILE_SIZE / 2)
            coordinates.append((x, y))
        #
        return coordinates
