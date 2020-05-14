from pygame.math import Vector2


# SCHERM SETTINGS
WIDTH, HEIGHT = 560, 620
FPS = 60
PLAY_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH - PLAY_BUFFER, HEIGHT - PLAY_BUFFER


# Kleuren

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (110, 110, 110)
PLAYER_COLOR = (190, 190, 30)


# text settings

START_TEXT_SIZE = 30
START_TEXT_SIZE_TITLE = 40
START_TEXT_SIZE_CRED = 15
START_FONT = 'arial black'


# player settings
P_START_POS = Vector2(1, 1)

# enemy settings
