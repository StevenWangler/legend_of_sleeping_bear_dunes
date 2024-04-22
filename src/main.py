"""
main.py

This module is the main entry point of the application. It initializes the pygame screen, 
creates a clock object to control the frames per second, and creates an instance of the Menu class.

It then enters the main game loop, which continues running until the user quits the application. 
During each iteration of the loop, it handles any events (like keyboard or mouse input), 
renders the screen, and then waits for a short period of time to control the frame rate.

Functions:
    main(): Initializes the pygame screen, clock, and menu, and then enters the main game loop.

Note:
    This script is meant to be run as a standalone file. If imported, it does nothing.
"""
import pygame
import sys
from events import handle_events
from screens import render
from screens.menu import Menu
from app_settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS 

def main():
    """
    The main function of the game.
    Initializes the game window, creates a menu instance, and runs the game loop.
    """
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    menu = Menu(screen, clock)
    menu.main_menu()

    running = True
    while running:
        running = handle_events()
        render(screen)
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()