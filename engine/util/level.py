"""Loads levels"""
from entity.level import Level
from engine.constants import LEVELS

class LevelLoader:
    "Loads levels"
        
    def load(self, level):
        """Loads a level given a level identifier

        Args:
            level (str): The level identifier (e.g. 'level_1')

        Returns:
            Level: The loaded level instance
        """
        if level not in LEVELS.keys():
            raise Exception(f"Level {level} not found")
        #
        if 'waypoints' not in LEVELS[level].keys():
            raise Exception(f"Level {level} does not have waypoints")
        #
        return Level(LEVELS[level]['waypoints'])