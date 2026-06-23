import pygame
import Const
from Entity import Entity

class Enemy(Entity):
    def __init__(self, image: pygame.Surface, lane_x: int, y: int, speed_y: float, is_hole: bool=False):
        super().__init__("Enemy" if not is_hole else "Hole", image, image.get_rect(center=(lane_x, y)))
        self.base_speed_y = speed_y
        self.is_hole = is_hole
        self.passed = False
        self.used = False

    def move(self, global_speed_multiplier: float):
        self.rect.y += self.base_speed_y * global_speed_multiplier
        if self.rect.top > Const.SCREEN_HEIGHT:
            self.kill()
