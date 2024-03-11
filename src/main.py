import pygame
import sys

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
FPS = 60

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def render(screen):
    screen.fill((0, 0, 0))
    # Draw everything here
    pygame.display.flip()

def main_menu(screen, clock):
    menu_options = ['Start', 'Load', 'Settings', 'Quit']
    # Try to load a nicer font here. If not found, default to None, which uses the default font.
    try:
        font = pygame.font.Font("your_font_path_here.ttf", 50)  # Customize your font path and size
    except IOError:
        font = pygame.font.Font(None, 50)  # Fallback to default font

    options_rects = []
    bg_color = (50, 50, 50)  # Dark grey background
    text_color = (255, 255, 255)  # White text
    highlight_color = (255, 0, 0)  # Red highlight
    normal_color = (0, 200, 0)  # Green for non-highlighted options

    def draw_menu():
        screen.fill(bg_color)
        del options_rects[:]  # Clear previous rects to avoid duplication
        for index, option in enumerate(menu_options):
            text = font.render(option, True, text_color)
            rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50 + 100 * index))
            options_rects.append(rect)
            screen.blit(text, rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if options_rects[0].collidepoint(mouse_pos):
                    print("Start game")  # Placeholder for starting the game
                    running = False
                elif options_rects[1].collidepoint(mouse_pos):
                    print("Load game")  # Placeholder for loading a game
                elif options_rects[2].collidepoint(mouse_pos):
                    print("Settings")  # Placeholder for showing settings
                elif options_rects[3].collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        draw_menu()

        # Highlight option if mouse hover
        mouse_pos = pygame.mouse.get_pos()
        for rect in options_rects:
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, highlight_color, rect, 2)
            else:
                pygame.draw.rect(screen, normal_color, rect, 2)

        pygame.display.flip()
        clock.tick(FPS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    main_menu(screen, clock)  # Updated to pass clock

    running = True
    while running:
        running = handle_events()
        render(screen)
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
