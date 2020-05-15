import pygame
from settings import *
vec = pygame.math.Vector2


class Player:
    def __init__(self, app, position):
        self.app = app

        # dit is om het bolletje in het midden van een vierkant in de grid te krijgen
        self.grid_position = position
        self.pixel_position = self.get_pix_pos()
        self.direction = vec(1, 0)
        # hier word de richting in opgeslagen
        self.stored_direction = None

    def update(self):
        self.pixel_position += self.direction
        if self.time_to_move():
            if self.stored_direction != None:
                self.direction = self.stored_direction

        # Setting grid position in reference to pix pos
        self.grid_position[0] = (self.pixel_position[0] - TOP_BOTTOM_BUFFER +
                                 self.app.cell_width // 2) // self.app.cell_width + 1
        self.grid_position[1] = (self.pixel_position[1] - TOP_BOTTOM_BUFFER +
                                 self.app.cell_height // 2) // self.app.cell_height + 1

    def draw(self):
        # dit is de player getekend
        pygame.draw.circle(self.app.screen, PLAYER_COLOR, (int(
            self.pixel_position.x), int(self.pixel_position.y)), self.app.cell_width // 2 - 1)

        # tekent de grid positie vierkant
        pygame.draw.rect(self.app.screen, RED, (self.grid_position[0] * self.app.cell_width + TOP_BOTTOM_BUFFER // 2,
                                                self.grid_position[1] * self.app.cell_height + TOP_BOTTOM_BUFFER // 2, self.app.cell_width, self.app.cell_height), 1)

    def move(self, direction):
        self.stored_direction = direction


# maakt de self.pixel_position niet zo rommelig


    def get_pix_pos(self):
        return vec((
            self.grid_position.x * self.app.cell_width) + TOP_BOTTOM_BUFFER // 2 + self.app.cell_width // 2, (self.grid_position.y * self.app.cell_height) + TOP_BOTTOM_BUFFER // 2 + self.app.cell_height // 2)

    def time_to_move(self):
        if int(self.pixel_position.x + TOP_BOTTOM_BUFFER // 2) % self.app.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                return True
        if int(self.pixel_position.y + TOP_BOTTOM_BUFFER // 2) % self.app.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                return True
