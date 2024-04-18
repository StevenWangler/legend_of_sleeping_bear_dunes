import pygame
from pygame.locals import *
from characters import mother_bear
import sys

class Tutorial:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)  # Change the font and size as needed
        self.text = [
            "Welcome to the game!",
            "Here are some instructions to get you started:",
            " - Use the arrow keys to move",
            " - Press space to jump",
            " - Avoid enemies and obstacles",
            "Press any key to start the game..."
        ]
        self.player = mother_bear()

    def start_tutorial(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black

        # Render the text
        for i, line in enumerate(self.text):
            text_surface = self.font.render(line, True, (255, 255, 255))  # White text
            self.screen.blit(text_surface, (50, 50 + i * 40))  # Adjust the position as needed

        pygame.display.flip()  # Update the display

        # Wait for the user to press any key
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    return  # Exit the tutorial

            self.player.handle_keys()
            self.screen.fill((0, 0, 0))  # Clear the screen before drawing the player
            self.player.draw(self.screen)
            pygame.display.flip()