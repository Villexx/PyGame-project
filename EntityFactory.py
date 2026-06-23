import pygame
import random
import Const
from Player import Player
from Enemy import Enemy
from Background import Background

class EntityFactory:
    def __init__(self, assets):
        self.assets = assets
        self.vehicles = ['car1', 'car2', 'truck1', 'van', 'truck2']
        self.holes = ['hole1', 'hole2']

    def get_entity(self, entity_type: str, **kwargs):
        if entity_type == "Player":
            return Player(self.assets.images["player"])
            
        elif entity_type == "Enemy":
            is_hole = kwargs.get("is_hole", False) 
            lane_idx = kwargs.get("lane_idx", 0)
            lane_x = Const.LANE_CENTERS[lane_idx]
            
            if is_hole:
                img_key = random.choice(self.holes)
                speed = Const.BASE_BG_SPEED
            else:
                img_key = random.choice(self.vehicles)
                speed = Const.BASE_BG_SPEED + random.uniform(1.0, 2.5)
                
            image = self.assets.images[img_key]
            y_pos = -image.get_height()
            return Enemy(image, lane_x, y_pos, speed, is_hole)
            
        elif entity_type == "Background":
            start_y = kwargs.get("start_y", 0)
            return Background(self.assets.bg_surface, start_y)
            
        return None
