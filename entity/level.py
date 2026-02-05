"""The level class

"""

class Level():
    "The level class"

    def __init__(self, waypoints):
        """"Initializes a level instance"

        Args:
            waypoints (list): x,y tuple coordinates for enemy entities to follow
        """
        self.waypoints = waypoints