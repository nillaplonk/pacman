import pygame
from settings import *
vector2 = pygame.math.Vector2


class Player:
    def __init__(self, app, position):
        self.app = app

        # dit is om het bolletje in het midden van een vierkant in de grid te krijgen
        self.grid_position = position
        self.pixel_position = vector2((
            self.grid_position.x * self.app.cell_width) + PLAY_BUFFER // 2 + self.app.cell_width // 2, (self.grid_position.y * self.app.cell_height) + PLAY_BUFFER // 2 + self.app.cell_height // 2)

    def update(self):
        pass

    def draw(self):
    	# dit is de player getekend 
        pygame.draw.circle(self.app.screen, PLAYER_COLOR, (int(
            self.pixel_position.x), int(self.pixel_position.y)), self.app.cell_width // 2 - 1)
