"""The game controller

Typical usage example:
    Game()
"""
from .constants import PLAYAREA_WIDTH, PLAYAREA_HEIGHT
from .constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from engine.util.loader import Loader
from entity.level import Level
from entity.turret import Turret

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

        self.loader = Loader(self.level)
        self.loader.load()
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
        
        self.level.draw(self.screen)
        self.draw_path()
        
        for entity_group in self.loader.entities.values():
            entity_group.update()
            entity_group.draw(self.screen)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.run = False
            #
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_position = pygame.mouse.get_pos()
                mouse_x = mouse_position[0]
                mouse_y = mouse_position[1]
                if mouse_x < PLAYAREA_WIDTH and mouse_y < PLAYAREA_HEIGHT:
                    self.loader.create_turret(mouse_x, mouse_y)
            #
        #
        
        pygame.display.flip()
        
    
    def draw_path(self):
        "Draws the path for this level"
        path = self.level.waypoints.copy()
        pygame.draw.lines(self.screen, "grey0", False, path)