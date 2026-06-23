import pygame
import os
import Const
from Assets import Assets
from GameState import GameState
from Menu import Menu
from Level import Level

class Game:
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption("Counter Flow")
        pygame.display.set_mode((1, 1), pygame.HIDDEN)
        
        self.assets = Assets()
        self.assets.load_all()
        
        self.window = pygame.display.set_mode((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT), pygame.SHOWN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = GameState.MENU
        
        self.menu = Menu(self.window, self)
        self.level = Level(self.window, self, "Level 1")
        
        self.play_music(self.assets.music_paths.get("menu"))

    def play_music(self, path):
        try:
            if path and os.path.exists(path):
                pygame.mixer.music.load(path)
                pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Error playing music: {e}")

    def start_level(self, victory_score):
        self.state = GameState.PLAYING
        self.play_music(self.assets.music_paths.get("playing"))
        self.level.set_victory_score(victory_score)
        self.level.setup_level()

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    
                if self.state == GameState.TUTORIAL:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.state = GameState.MENU
                        
                elif self.state in [GameState.GAME_OVER, GameState.VICTORY]:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.start_level(self.level.victory_score)
                        elif event.key == pygame.K_ESCAPE:
                            self.state = GameState.MENU
                            self.play_music(self.assets.music_paths.get("menu"))

                elif self.state == GameState.PLAYING:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.state = GameState.PAUSED
                        pygame.mixer.music.pause()

                elif self.state == GameState.PAUSED:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.state = GameState.PLAYING
                        pygame.mixer.music.unpause()

            if self.state == GameState.MENU:
                self.menu.run(events)
            elif self.state == GameState.PLAYING:
                self.level.run(events)
            elif self.state == GameState.TUTORIAL:
                self.draw_tutorial()
            elif self.state == GameState.PAUSED:
                self.level.draw()                    
                self.draw_paused()
            elif self.state == GameState.GAME_OVER:
                self.level.draw()                    
                self.draw_game_over()
            elif self.state == GameState.VICTORY:
                self.level.draw()                    
                self.draw_victory()

            pygame.display.flip()
            self.clock.tick(Const.FPS)

        pygame.quit()

    def draw_paused(self):
        overlay = pygame.Surface((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.window.blit(overlay, (0, 0))

        text1 = self.assets.fonts["title"].render("JOGO PAUSADO", True, Const.WHITE)
        rect1 = text1.get_rect(center=(Const.SCREEN_WIDTH // 2, Const.SCREEN_HEIGHT // 2))
        self.window.blit(text1, rect1)

        text2 = self.assets.fonts["menu"].render("Pressione ESC para Continuar", True, Const.WHITE)
        rect2 = text2.get_rect(center=(Const.SCREEN_WIDTH // 2, Const.SCREEN_HEIGHT // 2 + 50))
        self.window.blit(text2, rect2)

    def draw_tutorial(self):
        overlay = pygame.Surface((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.window.blit(overlay, (0, 0))

        lines = [
            "Comandos: WASD ou Setas",
            "para movimentar o carro.",
            "Durante o jogo, aperte ESC para pausar.",
            "",
            "Vitória (Iniciar): 50 carros desviados.",
            "Vitória (Modo Teste): 10 carros desviados.",
            "",
            "Penalidade: Bater em buracos",
            "deduz 1 ponto do score e deduz 30 HP.",
            "Bater em carros é Game Over.",
            "",
            "Dificuldade: O jogo acelera",
            "a cada 10 carros desviados.",
            "",
            "Pressione ESC para voltar."
        ]

        for i, line in enumerate(lines):
            text = self.assets.fonts["tutorial"].render(line, True, Const.WHITE)
            rect = text.get_rect(center=(Const.SCREEN_WIDTH // 2, Const.SCREEN_HEIGHT // 4 + i * 30))
            self.window.blit(text, rect)

    def draw_game_over(self):
        overlay = pygame.Surface((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.window.blit(overlay, (0, 0))

        if "game_over" in self.assets.images:
            go_img = self.assets.images["game_over"]
            rect = go_img.get_rect(center=(Const.SCREEN_WIDTH // 2, Const.SCREEN_HEIGHT // 2))
            self.window.blit(go_img, rect)

        text1 = self.assets.fonts["menu"].render("Pressione ESPAÇO para Reiniciar", True, Const.WHITE)
        rect1 = text1.get_rect(center=(Const.SCREEN_WIDTH // 2, int(Const.SCREEN_HEIGHT * 0.8)))
        self.window.blit(text1, rect1)

        text2 = self.assets.fonts["menu"].render("ESC para Voltar ao Menu", True, Const.WHITE)
        rect2 = text2.get_rect(center=(Const.SCREEN_WIDTH // 2, int(Const.SCREEN_HEIGHT * 0.8) + 40))
        self.window.blit(text2, rect2)

    def draw_victory(self):
        overlay = pygame.Surface((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.window.blit(overlay, (0, 0))

        if "victory" in self.assets.images:
            vic_img = self.assets.images["victory"]
            rect = vic_img.get_rect(center=(Const.SCREEN_WIDTH // 2, Const.SCREEN_HEIGHT // 2))
            self.window.blit(vic_img, rect)

        text1 = self.assets.fonts["menu"].render("ESPAÇO para Jogar Novamente", True, Const.WHITE)
        rect1 = text1.get_rect(center=(Const.SCREEN_WIDTH // 2, int(Const.SCREEN_HEIGHT * 0.8)))
        self.window.blit(text1, rect1)

        text2 = self.assets.fonts["menu"].render("ESC para Voltar ao Menu", True, Const.WHITE)
        rect2 = text2.get_rect(center=(Const.SCREEN_WIDTH // 2, int(Const.SCREEN_HEIGHT * 0.8) + 40))
        self.window.blit(text2, rect2)
