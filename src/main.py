"""
main.py

This module contains the main game loop and event handling for a Pygame application.

Functions:
    handle_events(): Handles Pygame events such as quitting the game.
    render(screen): Clears the screen, draws everything, and updates the display.
    main(): Initializes Pygame, sets up the display and clock, shows the startup screen, 
            runs the main game loop, and quits Pygame when done.

Constants:
    SCREEN_WIDTH: The width of the game window.
    SCREEN_HEIGHT: The height of the game window.
    FPS: The frames per second the game runs at.
"""
import pygame
import sys
from screens import startup_screen

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60

def handle_events():
    """
    Handles Pygame events such as quitting the game.

    Iterates over all the events currently in the Pygame event queue. If the QUIT event is found,
    the function returns False, indicating the game should stop. If no QUIT event is found, the 
    function returns True, indicating the game should continue.

    Returns:
        bool: False if the QUIT event is found, True otherwise.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def render(screen):
    """
    Clears the screen, draws everything, and updates the display.

    This function first fills the entire screen with black, effectively clearing it. 
    Then, it draws everything that needs to be drawn. Finally, it updates the display 
    to show the new frame.

    Args:
        screen (pygame.Surface): The surface to draw on.

    """
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Draw everything here
    
    # Update the display
    pygame.display.flip()

def main():
    """
    Initializes Pygame, sets up the display and clock, shows the startup screen, 
    runs the main game loop, and quits Pygame when done.

    This function first initializes Pygame and sets up the display and the clock. 
    Then, it shows the startup screen. After that, it enters the main game loop, 
    which continues until a QUIT event is detected. Finally, it quits Pygame and 
    exits the program.

    """
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up the clock for FPS control
    clock = pygame.time.Clock()

    # Show the start up screen
    startup_screen.show_startup_screen(screen)

    # Main game loop
    running = True
    while running:
        running = handle_events()
        render(screen)
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
