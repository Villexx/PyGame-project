import pygame
import Const
from GameState import GameState

class Menu:
    def __init__(self, window: pygame.Surface, game):
        self.windows = window
        self.game = game
        self.assets = game.assets
        self.menu_options = ["Iniciar", "Modo Teste", "Tutorial & Controles", "Sair"]
        self.selected_option = 0

    def run(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                elif event.key == pygame.K_RETURN:
                    self.select_option()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                for i in range(len(self.menu_options)):
                    rect_y = Const.SCREEN_HEIGHT // 2 + 50 + i * 50
                    if Const.SCREEN_WIDTH // 2 - 100 < mx < Const.SCREEN_WIDTH // 2 + 100:
                        if rect_y - 20 < my < rect_y + 20:
                            self.selected_option = i
                            self.select_option()

        self.draw()

    def select_option(self):
        if self.selected_option == 0:
            self.game.start_level(Const.VICTORY_SCORE)
        elif self.selected_option == 1:
            self.game.start_level(10)
        elif self.selected_option == 2:
            self.game.state = GameState.TUTORIAL
        elif self.selected_option == 3:
            self.game.running = False

    def draw(self):
                              
        if self.assets.bg_surface:
                                              
            self.windows.blit(self.assets.bg_surface, (0, 0))
            
                                                                                         
            overlay = pygame.Surface((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 120))
            self.windows.blit(overlay, (0, 0))
        else:
            self.windows.fill(Const.BLACK)
        
        if "menu" in self.assets.images:
            menu_img = self.assets.images["menu"]
            rect = menu_img.get_rect(center=(Const.SCREEN_WIDTH // 2, Const.SCREEN_HEIGHT // 2))
            self.windows.blit(menu_img, rect)

        for i, option in enumerate(self.menu_options):
            color = Const.RED if i == self.selected_option else Const.WHITE
            text = self.assets.fonts["menu"].render(option, True, color)
            rect = text.get_rect(center=(Const.SCREEN_WIDTH // 2, int(Const.SCREEN_HEIGHT * 0.75) + i * 40))
            self.windows.blit(text, rect)
