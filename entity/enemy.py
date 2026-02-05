"""The enemy sprite class

Typical usage example:
    Enemy((100, 100), pygame.surface.Surface)
"""
from engine.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from pygame.math import Vector2
from pygame.sprite import Sprite

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
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 2
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos


    def update(self):
        "Updates the enemy"
        self.move()


    def move(self):
        """Moves the enemy
        
        Enemy follows waypoints in an endless loop
        """
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.pos
        
        distance = self.movement.length()
        if distance >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        else:
            if distance != 0:
                self.pos += self.movement.normalize() * distance
            #
            self.target_waypoint += 1
            if self.target_waypoint >= len(self.waypoints):
                self.target_waypoint = 0
            #
        #
        self.rect.center = self.pos