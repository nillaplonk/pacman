import pygame
import os
import random
import time
from settings import *
import sys

pygame.init()


vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'

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
        pygame.display.flip()


# ------------------PLAYING  FUNCTIES -----------------------------


    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def playing_update(self):
        pass

# ---------Dit tekent de tekst het scherm en maakt gebruik van de draw_text functie---------------------
    def playing_draw(self):
        self.screen.fill(WHITE)
        pygame.display.flip()