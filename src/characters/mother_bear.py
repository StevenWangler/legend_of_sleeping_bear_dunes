import pygame
from pygame.locals import *

class MotherBear:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, 50, 50))

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.x -= self.speed
        if keys[K_RIGHT]:
            self.x += self.speed
        if keys[K_UP]:
            self.y -= self.speed
        if keys[K_DOWN]:
            self.y += self.speed