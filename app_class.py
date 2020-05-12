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
            else:
                pass

            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


# ---------------------wat help functies voor dingen---------------------------


    def draw_text(self, words, screen, position, size, color, font):
        font = pygame.font.SysFont(font, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        screen.blit(text, position)


# ------------------intro functies-----------------------------

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
        self.draw_text("PRESS SPACE TO START", self.screen, (115, HEIGHT // 2), START_TEXT_SIZE,
                       (170, 130, 60), START_FONT)
        self.draw_text("PACMAN", self.screen, (150, HEIGHT // 4), START_TEXT_SIZE,
                       (40, 180, 175), START_FONT)
        pygame.display.update()
        pygame.display.flip()


