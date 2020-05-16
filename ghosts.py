import pygame
from settings import *
from app_class import *

vec = pygame.math.Vector2
pic = pygame.image.load("images/Blinky.png")


class Ghost:
    def __init__(self, app, position):
        self.app = app
        self.grid_position = position
        self.pixel_position = self.get_pix_pos()
        self.screen = self.app.screen

    def get_pix_pos(self):
        return vec((
            self.grid_position[0] * self.app.cell_width) + TOP_BOTTOM_BUFFER // 2 + self.app.cell_width // 2, (self.grid_position[1] * self.app.cell_height) + TOP_BOTTOM_BUFFER // 2 + self.app.cell_height // 2)

    def update(self):
        pass

    def draw(self):
        self.screen.blit(pic, (int(
            self.pixel_position.x - self.app.cell_width // 2 - 1), int(self.pixel_position.y - self.app.cell_height // 2 - 1)))
