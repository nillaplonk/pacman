import pygame

from pygame.math import Vector2
vec = pygame.math.Vector2


# SCHERM SETTINGS
WIDTH, HEIGHT = 610, 670
FLAGS = pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN
FPS = 90
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH - TOP_BOTTOM_BUFFER, HEIGHT - TOP_BOTTOM_BUFFER


ROW = 30
COLUM = 28

# Kleuren

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (110, 110, 110)
PLAYER_COLOR = (190, 190, 30)
RED = (220, 20, 60)


# text settings

START_TEXT_SIZE = 30
START_TEXT_SIZE_TITLE = 40
START_TEXT_SIZE_CRED = 15
START_FONT = 'arial black'


# player settings

# p_pos = vec(13, 29)

# with open("wall.txt", "r") as walls:
#     for yline, line in enumerate(walls):
#         for xline, char in enumerate(line):
#             if char == "1":
#                 P_START_POS = Vector2(xline, yline)
#     else:
#         pass

# enemy settings
