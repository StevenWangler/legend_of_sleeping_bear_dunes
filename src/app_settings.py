"""
app_settings.py

This module initializes pygame and sets up the basic settings for the application.
It defines the screen width and height, and the frames per second (FPS) for the game loop.

Constants:
    SCREEN_WIDTH (int): The width of the application window in pixels.
    SCREEN_HEIGHT (int): The height of the application window in pixels.
    FPS (int): The frames per second the game runs at.

Note:
    The screen width and height are currently set to fixed values.
    Uncomment the commented lines to set them to 80% of the current screen resolution.
"""
import pygame

pygame.init()
infoObject = pygame.display.Info()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
#SCREEN_WIDTH = int(infoObject.current_w * 0.8)  # 80% of the screen width
#SCREEN_HEIGHT = int(infoObject.current_h * 0.8)  # 80% of the screen height
FPS = 60 # Frames per second