from .constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS

import pygame

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.start()

    def start(self):
        pygame.init()
        while self.run:
            self.game_loop()
        #
        pygame.quit()

    def game_loop(self):
        self.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            #
        #