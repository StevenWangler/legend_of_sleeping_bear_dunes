import pygame
import sys
from events import handle_events
from screens import render
from screens.menu import Menu

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    menu = Menu(screen, clock)  # Create a new instance of 'Menu'
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