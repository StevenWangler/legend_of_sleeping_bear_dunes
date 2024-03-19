"""
This module contains the SettingsScreen class which is used to manage the settings screen of the game.

Classes:
    SettingsScreen: A class to represent the settings screen.

The SettingsScreen class has the following methods:
    __init__(self, screen, clock): Initializes the SettingsScreen with a screen and a clock.
    draw_text(self, text, x, y): Draws the given text at the given position on the screen.
    main_settings(self): Manages the main settings screen loop.

The SettingsScreen class has the following attributes:
    screen: The screen to draw the settings on.
    clock: The clock used to control the frame rate.
    font: The font used to render the text.
    back_button: A pygame.Rect representing the back button.
"""
import pygame
import sys

class SettingsScreen:
    """
    Represents the settings screen of the game.
    """

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.font = pygame.font.Font(None, 36)

        # Define a rect for the back button with smaller size
        self.back_button = pygame.Rect(50, self.screen.get_height() - 80, 100, 30)


    def draw_text(self, text, x, y):
        """
        Draws text on the screen at the specified position.

        Args:
            text (str): The text to be drawn.
            x (int): The x-coordinate of the text position.
            y (int): The y-coordinate of the text position.
        """
        text_surface = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)


    def main_settings(self):
        """
        Displays the main settings screen.
        """
        # Load the background image
        background = pygame.image.load('src/assets/Temp Settings Background.png')

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    # If the back button is clicked, return to the main menu
                    if self.back_button.collidepoint(mouse_pos):
                        running = False

            # Draw the background image
            self.screen.blit(background, (0, 0))

            self.draw_text('Settings', self.screen.get_width() // 2, 50)

            # Draw the back button
            pygame.draw.rect(self.screen, (0, 0, 0), self.back_button)
            self.draw_text('Back', self.back_button.x + 50, self.back_button.y + 15)

            pygame.display.flip()
            self.clock.tick(60)
