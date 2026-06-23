import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, name: str, surf: pygame.Surface, rect: pygame.Rect):
        super().__init__()
        self.name = name
        self.surf = surf
        self.rect = rect
        self.image = surf                                        

    def move(self):
        pass
