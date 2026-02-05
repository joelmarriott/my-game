"""The game controller

Typical usage example:
    Game()
"""
from .constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from engine.util.entity import EntityLoader
from entity.level import Level

import pygame

class Game():
    """Main game controller
    
    Attributes:
        screen (pygame.Surface)   : The rendered screen
        clock  (pygame.time.Clock): The clock
        run    (boolean)          : Controls game loop 
    """

    def __init__(self):
        "Initializes a game instance"
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.level = Level('level_1')

        entity_loader = EntityLoader(self.level)
        entity_loader.load()
        self.entities = entity_loader.entities
        self.start()


    def start(self):
        "Starts the game"
        self.setup_window()
        self.level.load()
        while self.run:
            self.game_loop()
        #
        pygame.quit()


    def setup_window(self):
        "Sets up the game window"
        pygame.init()
        pygame.display.set_caption("Tower Defence")



    def game_loop(self):
        "The game loop"
        self.clock.tick(FPS)
        
        self.screen.fill("grey100")
        
        self.level.draw(self.screen)
        self.draw_path()
        
        for entity_group in self.entities.values():
            entity_group.update()
            entity_group.draw(self.screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            #
        #
        
        pygame.display.flip()
        
    
    def draw_path(self):
        "Draws the path for this level"
        path = self.level.waypoints.copy()
        pygame.draw.lines(self.screen, "grey0", False, path)