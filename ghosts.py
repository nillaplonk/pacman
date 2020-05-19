import pygame
from settings import *
from app_class import *

vec = pygame.math.Vector2
Blinky = pygame.transform.scale(
    pygame.image.load("images/Blinky.png"), (20, 20))
Clyde = pygame.transform.scale(
    pygame.image.load("images/Clyde.png"), (20, 20))
Inky = pygame.transform.scale(
    pygame.image.load("images/Inky.png"), (20, 20))
Pinky = pygame.transform.scale(
    pygame.image.load("images/Pinky.png"), (20, 20))


class Ghost:
    def __init__(self, app, position, number):
        self.app = app
        self.grid_position = position
        self.pixel_position = self.get_pix_pos()
        self.screen = self.app.screen
        self.ghost_number = number
        self.direction = vec(1, 0)
        self.mood = self.set_mood()
        self.target = None
        self.speed = 2

    def update(self):
        self.target = self.set_target()
        if self.target != self.grid_position:
            self.pixel_position += self.direction * self.speed
        if self.time_to_move:
            self.move()

        self.grid_position[0] = (self.pixel_position[0] - TOP_BOTTOM_BUFFER +
                                 self.app.cell_width // 2) // self.app.cell_width + 1
        self.grid_position[1] = (self.pixel_position[1] - TOP_BOTTOM_BUFFER +
                                 self.app.cell_height // 2) // self.app.cell_height + 1

    def draw(self):
        if self.ghost_number == 0:
            self.screen.blit(Blinky, (int(self.pixel_position.x - self.app.cell_width //
                                          2 - 1), int(self.pixel_position.y - self.app.cell_height // 2 - 1)))
        elif self.ghost_number == 1:
            self.screen.blit(Clyde, (int(self.pixel_position.x - self.app.cell_width //
                                         2 - 1), int(self.pixel_position.y - self.app.cell_height // 2 - 1)))
        elif self.ghost_number == 2:
            self.screen.blit(Inky, (int(self.pixel_position.x - self.app.cell_width //
                                        2 - 1), int(self.pixel_position.y - self.app.cell_height // 2 - 1)))
        elif self.ghost_number == 3:
            self.screen.blit(Pinky, (int(self.pixel_position.x - self.app.cell_width //
                                         2 - 1), int(self.pixel_position.y - self.app.cell_height // 2 - 1)))

    def set_target(self):
        if self.mood == "fast" or self.mood == "slow":
            return self.app.player.grid_position
        else:
            if self.app.player.grid_position[0] > COLUM // 2 and self.app.player.grid_position[1] > ROW // 2:
                return vec(1, 1)
            if self.app.player.grid_position[0] > COLUM // 2 and self.app.player.grid_position[1] < ROW // 2:
                return vec(1, ROW - 2)
            if self.app.player.grid_position[0] < COLUM // 2 and self.app.player.grid_position[1] > ROW // 2:
                return vec(COLUM - 2, 1)
            else:
                return vec(COLUM - 2, ROW - 2)

    def set_mood(self):
        if self.ghost_number == 0:
            return "fast"
        elif self.ghost_number == 1:
            return "slow"
        elif self.ghost_number == 2:
            return "scared"
        elif self.ghost_number == 3:
            return "random"

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

    def move(self):
        if self.mood == "random":
            self.direction = self.random_direction()
        if self.mood == "slow":
            self.direction = self.get_direction(self.target)
        if self.mood == "fast":
            self.direction = self.get_direction(self.target)
        if self.mood == "scared":
            self.direction = self.get_direction(self.target)

    def get_direction(self, target):
        next_cell = self.find_next_path(target)
        xdir = next_cell[0] - self.grid_position[0]
        ydir = next_cell[1] - self.grid_position[1]
        return vec(xdir, ydir)

    def find_next_path(self, target):
        path = self.path_algorithm([int(self.grid_position.x), int(self.grid_position.y)], [
            int(target[0]), int(target[1])])
        return path[1]

    def path_algorithm(self, start, target):
        grid = [[0 for x in range(28)] for x in range(30)]
        for cell in self.app.walls:
            if cell.x < 28 and cell.y < 30:
                grid[int(cell.y)][int(cell.x)] = 1
        q = [start]
        path = []
        visited = []
        while q:
            current = q[0]
            q.remove(q[0])
            visited.append(current)
            if current == target:
                break
            else:
                neighbours = [[0, -1], [1, 0], [0, 1], [-1, 0]]
                for neighbour in neighbours:
                    if neighbour[0] + current[0] >= 0 and neighbour[0] + current[0] < len(grid[0]):
                        if neighbour[1] + current[1] >= 0 and neighbour[1] + current[1] < len(grid):
                            next_cell = [neighbour[0] + current[0],
                                         neighbour[1] + current[1]]
                            if next_cell not in visited:
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    q.append(next_cell)
                                    path.append(
                                        {"Current": current, "Next": next_cell})

        shortest = [target]
        while target != start:
            for step in path:
                if step["Next"] == target:
                    target = step["Current"]
                    shortest.insert(0, step["Current"])
        return shortest

    def random_direction(self):
        while True:
            number = random.randint(-2, 1)
            if number == -2:
                x_dir, y_dir = 1, 0
            elif number == -1:
                x_dir, y_dir = 0, 1
            elif number == 0:
                x_dir, y_dir = -1, 0
            else:
                x_dir, y_dir = 0, -1
            next_pos = vec(self.grid_position.x + x_dir,
                           self.grid_position.y + y_dir)
            if next_pos not in self.app.walls:
                break
        return vec(x_dir, y_dir)
