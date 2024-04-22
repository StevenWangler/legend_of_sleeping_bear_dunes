import pygame
from pygame.locals import *

class MotherBear:

    bear_image = None 

    def __init__(self, x=50, y=570, speed=5, scale_size=(100, 100), jump_strength=20, gravity=1):
        if MotherBear.bear_image is None:
            MotherBear.bear_image = pygame.image.load('src/assets/Temp Mother Bear.png').convert_alpha()
        self.speed = speed
        self.jump_strength = jump_strength
        self.gravity = gravity
        self.vertical_velocity = 0
        self.in_air = False

        # Scale the image and initialize the rect
        self.image = pygame.transform.scale(MotherBear.bear_image, scale_size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.base_y = y  # Starting ground level for calculating jumps

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, dx, dy):
        self.rect.x += dx
        if not self.in_air:
            self.rect.y += dy

    def jump(self):
        if not self.in_air:
            self.in_air = True
            self.vertical_velocity = -self.jump_strength

    def update(self):
        if self.in_air:
            self.rect.y += self.vertical_velocity
            self.vertical_velocity += self.gravity
            if self.rect.y >= self.base_y:
                self.rect.y = self.base_y
                self.in_air = False
                self.vertical_velocity = 0

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.move(-self.speed, 0)
        if keys[K_RIGHT]:
            self.move(self.speed, 0)
        if keys[K_UP]:
            self.jump()
