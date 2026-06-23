from enum import Enum

class GameState(Enum):
    MENU = 1
    TUTORIAL = 2
    PLAYING = 3
    GAME_OVER = 4
    VICTORY = 5
    PAUSED = 6
