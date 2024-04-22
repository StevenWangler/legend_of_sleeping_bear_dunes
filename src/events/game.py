import pygame
from characters.mother_bear import MotherBear

class Game:
    def __init__(self):
        self.player = MotherBear()
        self.background = pygame.image.load('src/assets/Temp Menu Background.png')
        self.background_pos = [0, 0]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.move_right()
                    self.background_pos[0] -= 5  # Move background to the left
                elif event.key == pygame.K_LEFT:
                    self.player.move_left()
                    self.background_pos[0] += 5  # Move background to the right
                # Handle up and down movement similarly
        return True

    def render(self, screen):
        screen.blit(self.background, self.background_pos)
        self.player.draw(screen)

    def run(self, screen):
        while self.handle_events():
            self.render(screen)
            pygame.display.flip()