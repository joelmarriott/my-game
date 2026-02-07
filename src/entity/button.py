"""The button class"""
import logging, pygame

class Button():
    "The button class"
    
    def __init__(self, name, x, y, image):
        """Initialises a button

        Args:
            x (int): x position of the button
            y (int): y position of the button
            image (pygame.surface.Surface): image for the button
        """
        self.name = name
        self.image = image
        self.original_image = image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.action = False
        
        
    def draw(self, surface):
        """Draws the button on the given surface

        Args:
            surface (pygame.surface.Surface): surface to draw the button on
        """
        hovered = False
        self.image = self.original_image.copy()
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
                if not self.action:
                    logging.info(f'Button {self.name} clicked')
                #
                self.action = True
                hovered = True
                self.image.fill((200, 200, 200), special_flags=pygame.BLEND_RGBA_MULT)
            else:
                self.image.fill((255, 255, 255, 200), special_flags=pygame.BLEND_RGBA_MULT)
                hovered = True
        #
        if not hovered:
            self.action = False
        #
        surface.blit(self.image, self.rect)
        return self.action