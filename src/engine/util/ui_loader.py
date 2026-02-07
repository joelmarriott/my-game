"""Loads UI from a given set of elements

"""
from engine.constants import UI_ELEMENTS
from entity.button import Button

import logging, pygame

class UiLoader:
    "Loads UI elements from a given set of images"
    def __init__(self):
        "Initializes a UI loader"
        self.configs = {}
        self.elements = {}


    def load(self):
        "Loops through all UI element types and image items to load the elements"
        for element_key, element_items in UI_ELEMENTS.items():
            self.load_configs(element_key, element_items)
        #
        self.load_elements()


    def load_configs(self, element_key, element_items):
        """Loops through image items for an element key and loads the image

        Args:
            element_key  (str) : element identifier (e.g. 'button')
            element_items (dict): key to config mapping for elements
        """
        if element_key not in self.configs.keys():
            self.configs[element_key] = {}
        #
        for element_id, element_data in element_items.items():
            if element_id not in self.configs[element_key].keys():
                self.configs[element_key][element_id] = {}
            #
            for config_key, config_value in element_data.items():
                if config_key == 'asset_path':
                    self.configs[element_key][element_id]['image'] = self.load_image(config_value)
                else:
                    self.configs[element_key][element_id][config_key] = config_value
                #
        #


    def load_image(self, image_path):
        """Loads an image given it's path

        Args:
            image_path (str): Path to the image
                              (e.g. 'asset/image/button/buy_turret.png')

        Returns:
            pygame.surface.Surface: The loaded image as a pygame surface
        """
        return pygame.image.load(image_path).convert_alpha()


    def load_elements(self):
        "Loops through all element types and element items to load the elements"
        for element_key, element_items in self.configs.items():
            self.group_elements(element_key, element_items)


    def group_elements(self, element_key, element_items):
        """Groups all elements for an element_key

        Args:
            element_key  (str) : element identifier (e.g. 'button')
            image_items (dict): key to path mapping for images
                             (e.g. {'buy_turret': 'asset/image/button/buy_turret.png'})
        """
        if element_key not in self.elements.keys():
            self.elements[element_key] = []
        #
        for element_id, element_item in element_items.items():
            print(element_id)
            if element_key == 'button':
                add_object = Button(
                    element_id,
                    element_item['position_x'],
                    element_item['position_y'],
                    element_item['image']
                )
            #
            if add_object:
                self.elements[element_key].append(add_object)
            else:
                logging.ERROR(f'Element {element_item} of type {element_key} could not be loaded')
            #
        #