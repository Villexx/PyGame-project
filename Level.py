import pygame
import random
import Const
from GameState import GameState
from EntityFactory import EntityFactory

class Level:
    def __init__(self, window: pygame.Surface, game, name: str):
        self.window = window
        self.game = game
        self.name = name
        self.entity_factory = EntityFactory(game.assets)
        self.entity_list = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()
        
        self.victory_score = Const.VICTORY_SCORE
        self.global_speed_multiplier = 1.0
        self.spawn_timer = 0
        
        self.player = None
        self.setup_level()

    def setup_level(self):
        self.entity_list.empty()
        self.backgrounds.empty()
        
                      
        self.player = self.entity_factory.get_entity("Player")
        
                           
        bg1 = self.entity_factory.get_entity("Background", start_y=0)
        bg2 = self.entity_factory.get_entity("Background", start_y=-bg1.surf.get_height())
        self.backgrounds.add(bg1, bg2)

    def set_victory_score(self, score):
        self.victory_score = score

    def run(self, events):
        keys = pygame.key.get_pressed()
        
        self.global_speed_multiplier = 1.0 + (max(0, self.player.score) // Const.SPEED_MULTIPLIER_STEP) * (Const.SPEED_INCREASE_FACTOR - 1.0)
        
                       
        self.player.move(keys)
        
                            
        for bg in self.backgrounds:
            bg.move(self.global_speed_multiplier)
            
                       
        self.spawn_timer -= 1 * self.global_speed_multiplier
        if self.spawn_timer <= 0:
            self._spawn_wave()
            delay = max(20, Const.BASE_SPAWN_DELAY - int((self.global_speed_multiplier - 1.0) * 20))
            self.spawn_timer = delay

                                             
        for entity in self.entity_list:
            if entity.name in ["Enemy", "Hole"]:
                if entity.name == "Enemy":
                    for other in self.entity_list:
                        if other != entity and other.name == "Enemy" and other.rect.centerx == entity.rect.centerx:
                            if other.rect.centery > entity.rect.centery:
                                dist = other.rect.top - entity.rect.bottom
                                if dist < 30 and entity.base_speed_y > other.base_speed_y:
                                    entity.base_speed_y = other.base_speed_y
                
                entity.move(self.global_speed_multiplier)
                
                                
                if not entity.passed and entity.rect.top > self.player.rect.bottom:
                    entity.passed = True
                    if not entity.used:
                        self.player.score += 1
                        if self.player.score >= self.victory_score:
                            self.game.state = GameState.VICTORY
                
                           
                if self.player.rect.colliderect(entity.rect):
                    if entity.name == "Hole":
                        if not entity.used:
                            self.player.hp -= Const.HOLE_DAMAGE
                            self.player.score -= 1
                            entity.used = True
                            entity.kill()
                            
                            if self.player.hp <= 0:
                                self.game.state = GameState.GAME_OVER
                    else:
                        self.game.state = GameState.GAME_OVER

        self.draw()

    def _spawn_wave(self):
        lane_idx = random.randint(0, 3)
        is_hole = random.random() < 0.2
        enemy = self.entity_factory.get_entity("Enemy", is_hole=is_hole, lane_idx=lane_idx)
        self.entity_list.add(enemy)

    def draw(self):
        self.backgrounds.draw(self.window)
        self.window.blit(self.player.image, self.player.rect)
        self.entity_list.draw(self.window)
        self.draw_hud()

    def draw_hud(self):
        margin = 15
        hud_w, hud_h = 160, 60
        hud_x = Const.SCREEN_WIDTH - hud_w - margin
        hud_y = margin

        bg_rect = pygame.Rect(hud_x, hud_y, hud_w, hud_h)
        pygame.draw.rect(self.window, (0, 0, 0, 150), bg_rect)
        pygame.draw.rect(self.window, Const.WHITE, bg_rect, 2)

        hp_x, hp_y = hud_x + 10, hud_y + 8
        pygame.draw.rect(self.window, Const.RED, (hp_x, hp_y, 140, 18))
        hp_width = max(0, (self.player.hp / Const.INITIAL_HP) * 140)
        pygame.draw.rect(self.window, Const.GREEN if self.player.hp > 30 else (255, 100, 0), (hp_x, hp_y, hp_width, 18))
        pygame.draw.rect(self.window, Const.WHITE, (hp_x, hp_y, 140, 18), 2)
        
        hp_text = self.game.assets.fonts["tutorial"].render(f"HP: {self.player.hp}", True, Const.BLACK)
        self.window.blit(hp_text, (hp_x + 5, hp_y - 2))

        score_text = self.game.assets.fonts["tutorial"].render(f"Score: {self.player.score}/{self.victory_score}", True, Const.WHITE)
        self.window.blit(score_text, (hp_x, hp_y + 24))
