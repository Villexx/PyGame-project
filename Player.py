import pygame
import Const
from Entity import Entity

class Player(Entity):
    def __init__(self, image: pygame.Surface):
        super().__init__("Player", image, image.get_rect())
        self.reset_position()
        self.hp = Const.INITIAL_HP
        self.score = 0

    def reset_position(self):
        self.rect.midbottom = (Const.SCREEN_WIDTH // 2, Const.SCREEN_HEIGHT - 30)

    def move(self, keys):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= Const.PLAYER_SPEED_Y
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += Const.PLAYER_SPEED_Y
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= Const.PLAYER_SPEED_X
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += Const.PLAYER_SPEED_X

                         
        if self.rect.left < Const.TRACK_X:
            self.rect.left = Const.TRACK_X
        if self.rect.right > Const.TRACK_X + Const.TRACK_WIDTH:
            self.rect.right = Const.TRACK_X + Const.TRACK_WIDTH

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Const.SCREEN_HEIGHT:
            self.rect.bottom = Const.SCREEN_HEIGHT
