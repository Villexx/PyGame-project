import pygame
import Const
from Entity import Entity

class Background(Entity):
    def __init__(self, image: pygame.Surface, start_y: float):
        super().__init__("Background", image, image.get_rect(topleft=(0, start_y)))
                                                                                              
        self.exact_y = float(start_y)

    def move(self, global_speed_multiplier: float):
        self.exact_y += Const.BASE_BG_SPEED * global_speed_multiplier
        if self.exact_y >= self.surf.get_height():
            self.exact_y -= self.surf.get_height() * 2
            
        self.rect.y = int(self.exact_y)
