"""
startup_screen.py

This module contains the function to display the startup screen for the game "The Legend of Sleeping Bear Dunes".

Functions:
    show_startup_screen(screen): Fills the screen with a background color, renders a message in the center of the screen, and updates the display.

Constants:
    BACKGROUND_COLOR: The RGB color used for the background of the startup screen.
    TEXT_COLOR: The RGB color used for the text of the startup screen.
    FONT: The font used for the text of the startup screen.
    MESSAGE: The message displayed on the startup screen.
"""
import pygame

BACKGROUND_COLOR = (0, 0, 0) 
TEXT_COLOR = (255, 255, 255)
FONT = pygame.font.Font(None, 36)
MESSAGE = "The Legend of Sleeping Bear Dunes: The Game"

def show_startup_screen(screen):
    screen.fill(BACKGROUND_COLOR)
    text = FONT.render(MESSAGE, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
