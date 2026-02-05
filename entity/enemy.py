"""The enemy sprite class

Typical usage example:
    Enemy((100, 100), pygame.surface.Surface)
"""
from engine.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from pygame.math import Vector2
from pygame.sprite import Sprite

import math
import pygame

class Enemy(Sprite):
    "The enemy sprite class"

    def __init__(self, waypoints, image):
        """Initialises an enemy

        Args:
            position (tuple): x,y position of the enemy (e.g. (100, 100))
            image (pygame.surface.Surface): image for the enemy
        """
        Sprite.__init__(self)
        self.waypoints = waypoints
        self.position = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 2
        self.angle = 0
        self.original_image = image
        self.rotate_and_update_image()


    def update(self):
        "Updates the enemy"
        self.move()
        self.calculate_rotation()
        self.rotate_and_update_image()


    def move(self):
        """Moves the enemy
        
        Enemy follows waypoints until it reached the end of the path,
        then it is removed from the game
        """
        if self.target_waypoint >= len(self.waypoints):
            self.target_waypoint = 0
            #self.kill()
            #return
        #
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.position
        
        distance = self.movement.length()
        if distance >= self.speed:
            self.position += self.movement.normalize() * self.speed
        else:
            if distance != 0:
                self.position += self.movement.normalize() * distance
            #
            self.target_waypoint += 1


    def calculate_rotation(self):
        "Calculate rotation"
        (x, y) = self.target - self.position
        self.angle = math.degrees(math.atan2(-y, x))


    def rotate_and_update_image(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.position