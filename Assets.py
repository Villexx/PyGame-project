import pygame
import os
import sys
import Const

class Assets:
    def __init__(self):
        self.images = {}
        self.fonts = {}
        self.bg_surface = None
        self.music_paths = {}

    def get_resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
                                                                           
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def load_all(self):
        pygame.font.init()
        base_dir = self.get_resource_path("asset")

        def load_image(name, filename, convert_alpha=True):
            path = os.path.join(base_dir, filename)
                                                                                
            mapping = {
                "Enimy_1_car.png": "Enimy_1_car 1.png",
                "Enimy_2_taxi.png": "Enimy_2_taxi 1.png",
                "Enimy_3_caminhao1.png": "Enimy_3_caminhao1 1.png",
                "Enimy_4_van.png": "Enimy_4_van 1.png",
                "Enimy_5_caminhao2.png": "Enimy_5_caminhao2 1.png",
                "Enimy_6_buraco_1.png": "Enimy_6_buraco_1 1.png",
                "Enimy_7_buraco_2.png": "Enimy_7_buraco_2 1.png",
            }
            if not os.path.exists(path) and filename in mapping:
                path = os.path.join(base_dir, mapping[filename])

            if os.path.exists(path):
                img = pygame.image.load(path)
                self.images[name] = img.convert_alpha() if convert_alpha else img.convert()
            else:
                surf = pygame.Surface((100, 100))
                surf.fill((255, 0, 255))
                self.images[name] = surf

                               
        load_image("left_track", "lateral_esquerda_da_pista 1.png", False)
        load_image("track", "Pista.png", False)
        load_image("right_track", "lateral_direita_da_pista 1.png", False)

                  
        load_image("player", "Player.png")
        load_image("car1", "Enimy_1_car.png")
        load_image("car2", "Enimy_2_taxi.png")
        load_image("truck1", "Enimy_3_caminhao1.png")
        load_image("van", "Enimy_4_van.png")
        load_image("truck2", "Enimy_5_caminhao2.png")
        load_image("hole1", "Enimy_6_buraco_1.png")
        load_image("hole2", "Enimy_7_buraco_2.png")

            
        load_image("menu", "Logo_Menu.png")
        load_image("game_over", "GameOver 1.png")
        load_image("victory", "Vitoria.png")

                                   
        left = self.images["left_track"]
        track = self.images["track"]
        right = self.images["right_track"]

        orig_bg_w = left.get_width() + track.get_width() + right.get_width()
        orig_bg_h = track.get_height()

        orig_bg_surface = pygame.Surface((orig_bg_w, orig_bg_h))
        orig_bg_surface.blit(left, (0, 0))
        orig_bg_surface.blit(track, (left.get_width(), 0))
        orig_bg_surface.blit(right, (left.get_width() + track.get_width(), 0))

                                                    
        desktop_sizes = pygame.display.get_desktop_sizes()
        if desktop_sizes:
            monitor_h = desktop_sizes[0][1]
        else:
            info = pygame.display.Info()
            monitor_h = info.current_h
            if monitor_h <= 1:
                monitor_h = 1080           
                
        target_h = int(monitor_h * 0.85)                       
        target_w = int(target_h * 0.5625)                      

        Const.SCREEN_WIDTH = target_w
        Const.SCREEN_HEIGHT = target_h

                                 
        scale_x = target_w / orig_bg_w
        scale_y = target_h / orig_bg_h

                          
        self.bg_surface = pygame.transform.scale(orig_bg_surface, (target_w, target_h))

                                            
        Const.TRACK_X = int(left.get_width() * scale_x)
        Const.TRACK_WIDTH = int(track.get_width() * scale_x)
        lane_w = Const.TRACK_WIDTH / Const.LANE_COUNT
        Const.LANE_CENTERS = [Const.TRACK_X + lane_w * i + lane_w / 2 for i in range(Const.LANE_COUNT)]

                                                        
        entities = ["player", "car1", "car2", "truck1", "van", "truck2", "hole1", "hole2"]
        uniform_scale = scale_x
        for key in entities:
            img = self.images[key]
            new_w = max(1, int(img.get_width() * uniform_scale))
            new_h = max(1, int(img.get_height() * uniform_scale))
            new_size = (new_w, new_h)
                                                                    
            scaled_img = pygame.transform.scale(img, new_size)
                                                                      
            bg_color = scaled_img.get_at((0, 0))
            scaled_img.set_colorkey(bg_color)
            self.images[key] = scaled_img

                                                                                                      
        for key in ["menu", "game_over", "victory"]:
            if key in self.images:
                img = self.images[key]
                
                if key == "menu":
                                                                                          
                    new_w = max(1, int(img.get_width() * uniform_scale))
                    new_h = max(1, int(img.get_height() * uniform_scale))
                    scaled_img = pygame.transform.scale(img, (new_w, new_h))
                else:
                                                                            
                    scaled_h = int(img.get_height() * scale_y)
                    scaled_img = pygame.transform.scale(img, (Const.TRACK_WIDTH, scaled_h))
                
                                
                bg_color = scaled_img.get_at((0, 0))
                scaled_img.set_colorkey(bg_color)
                self.images[key] = scaled_img

               
               
        self.fonts["hud"] = pygame.font.SysFont("Arial", 28, bold=True)
        self.fonts["title"] = pygame.font.SysFont("Arial", 26, bold=True)
        self.fonts["menu"] = pygame.font.SysFont("Arial", 24, bold=True)
        self.fonts["tutorial"] = pygame.font.SysFont("Arial", 18, bold=True)

        self.music_paths["menu"] = os.path.join(base_dir, "audio_menu.mp3")
        self.music_paths["playing"] = os.path.join(base_dir, "audio_playing.mp3")
