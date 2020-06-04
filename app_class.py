import pygame
import os
import random
import time
from settings import *
import sys
from player_class import *
from ghosts import *

pygame.init()

pygame.mixer.music.load("pacman.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            [WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        # voor het maken van de grid
        self.cell_width = MAZE_WIDTH // COLUM
        self.cell_height = MAZE_HEIGHT // ROW
        self.walls = []
        self.food = []
        self.ghosts = []
        self.ghost_position = []
        self.player_position = None
        self.score = 0

    # maken van de spelers

        self.load()
        self.player = Player(self, vec(self.player_position))
        self.make_ghosts()

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_draw()
                self.start_update()
            elif self.state == "playing":
                self.playing_events()
                self.playing_draw()
                self.playing_update()

            else:
                self.running = False

            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


# ---------------------wat help functies voor dingen---------------------------


    def draw_text(self, words, screen, position, size, color, font):
        font = pygame.font.SysFont(font, size)
        text = font.render(words, False, color)
        text_size = text.get_size()

        # Hierdoor komt de text in het midden van het scherm
        position[0] = position[0] - text_size[0] // 2
        position[1] = position[1] - text_size[1] // 2
        screen.blit(text, position)

# laden achtergrond
    def load(self):
        self.background = pygame.image.load("./images/maze.png")
        self.background = pygame.transform.scale(
            self.background, (MAZE_WIDTH, MAZE_HEIGHT))

        # openen van het bestand met muren.
        # maakt een lijst met coordinaten van de muren, 1 is een muur, C niet
        with open("wall.txt", "r") as text:
            for yline, line in enumerate(text):
                for xline, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xline, yline))
                    elif char == "F":
                        self.food.append(vec(xline, yline))
                    elif char == "P":
                        self.player_position = [xline, yline]
                    elif char in ["2", "3", "4", "5"]:
                        self.ghost_position.append([xline, yline])
                    elif char == "G":
                        pygame.draw.rect(self.background, BLACK, (xline * self.cell_width,
                                                                  yline * self.cell_height, self.cell_width, self.cell_height))
                        # deze functie tekent lijnen over het scherm die we kunnen gebruiken om de muren de definieren.

    def make_ghosts(self):
        for index, position in enumerate(self.ghost_position):
            self.ghosts.append(Ghost(self, vec(position), index))

    def grid(self):
        for x in range(WIDTH // self.cell_width):
            pygame.draw.line(self.background, GREY, (x * self.cell_width, 0),
                             (x * self.cell_width, HEIGHT))
        for x in range(HEIGHT // self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x * self.cell_height),
                             (WIDTH, x * self.cell_height))

        for food in self.food:
            pygame.draw.rect(self.background, (0, 255, 0),
                             (food.x * self.cell_width, food.y * self.cell_height, self.cell_width, self.cell_height))

# ------------------INTRO  FUNCTIES -----------------------------

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'

    def start_update(self):
        pass

# ---------Dit tekent de tekst het scherm en maakt gebruik van de draw_text functie---------------------
    def start_draw(self):
        self.screen.fill(BLACK)

        # Text aan het begin van het spel, in het midden van het scherm. input = functie draw_text
        self.draw_text("PRESS SPACE TO START", self.screen, [WIDTH // 2, HEIGHT // 2], START_TEXT_SIZE,
                       (170, 130, 60), START_FONT)
        self.draw_text("PACMAN", self.screen, [WIDTH // 2, HEIGHT // 4.5], START_TEXT_SIZE_TITLE,
                       (40, 180, 175), START_FONT)
        self.draw_text("@NILLAPLONK", self.screen, [WIDTH // 2, HEIGHT // 1.1], START_TEXT_SIZE_CRED,
                       (164, 255, 55), START_FONT)
        self.draw_text("HIGHSCORE: ", self.screen, [45, 10], START_TEXT_SIZE_CRED,
                       (255, 255, 255), START_FONT)

        pygame.display.update()


# ------------------PLAYING  FUNCTIES -----------------------------

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0, -1))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0, 1))

    def playing_update(self):
        self.player.update()
        for ghost in self.ghosts:
            ghost.update()

        for ghost in self.ghosts:
            if ghost.grid_position == self.player.grid_position:
                self.die()

                # ---------Dit tekent de tekst het scherm en maakt gebruik van de draw_text functie---------------------

                # achtergrond maze

    def playing_draw(self):
        self.screen.fill(BLACK)

        self.screen.blit(
            self.background, (TOP_BOTTOM_BUFFER // 2, TOP_BOTTOM_BUFFER // 2))
        # self.grid()
        self.draw_food()
        self.draw_text("HIGHSCORE: 0", self.screen, [
                       WIDTH // 2 + TOP_BOTTOM_BUFFER, 15], 20, (255, 255, 255), START_FONT)
        self.draw_text(f"SCORE : {self.score}", self.screen, [WIDTH // 4 - TOP_BOTTOM_BUFFER, 15], 20,
                       (255, 255, 255), START_FONT)

        self.player.draw()
        for ghost in self.ghosts:
            ghost.draw()

        pygame.display.update()

    def draw_food(self):
        for food in self.food:
            pygame.draw.circle(self.screen, (255, 215, 0), ((int(
                food.x * self.cell_width) + self.cell_width // 2) + TOP_BOTTOM_BUFFER // 2, (int(food.y * self.cell_height) + self.cell_height // 2) + TOP_BOTTOM_BUFFER // 2), 5)

    def die(self):
        self.player.life += -1
        if self.player.life == 0:
            self.state == "Game Over"
        else:
            self.player.grid_position = vec(self.player_position)
            self.player.pixel_position = self.player.get_pix_pos()
            self.player.direction *= 0
