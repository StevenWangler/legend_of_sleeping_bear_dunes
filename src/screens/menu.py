import pygame
import sys

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
FPS = 60

class Menu:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.menu_options = ['Start', 'Load', 'Settings', 'Quit']
        # Try to load a nicer font here. If not found, default to None, which uses the default font.
        try:
            self.font = pygame.font.Font("your_font_path_here.ttf", 50)  # Customize your font path and size
        except IOError:
            self.font = pygame.font.Font(None, 50)  # Fallback to default font

        self.options_rects = []
        self.bg_color = (50, 50, 50)  # Dark grey background
        self.text_color = (255, 255, 255)  # White text
        self.highlight_color = (255, 0, 0)  # Red highlight
        self.normal_color = (0, 200, 0)  # Green for non-highlighted options
        self.title_font = pygame.font.Font(None, 100)  # Customize your font size
        self.title_text = self.title_font.render("The Legend of Sleeping Bear Dunes", True, self.text_color)
        self.background = pygame.image.load('src/assets/Temp Menu Background.png')  # add background image

    def draw_menu(self):
        self.screen.fill(self.bg_color)
        title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200))  # Customize your title position
        self.screen.blit(self.title_text, title_rect)
        del self.options_rects[:]  # Clear previous rects to avoid duplication
        self.screen.blit(self.background, (0, 0))  # Draw the background image
        for index, option in enumerate(self.menu_options):
            text = self.font.render(option, True, self.text_color)
            rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50 + 100 * index))
            self.options_rects.append(rect)
            self.screen.blit(text, rect)

    def main_menu(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.options_rects[0].collidepoint(mouse_pos):
                        print("Start game")  # Placeholder for starting the game
                        running = False
                    elif self.options_rects[1].collidepoint(mouse_pos):
                        print("Load game")  # Placeholder for loading a game
                    elif self.options_rects[2].collidepoint(mouse_pos):
                        print("Settings")  # Placeholder for showing settings
                    elif self.options_rects[3].collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

            self.draw_menu()

            # Highlight option if mouse hover
            mouse_pos = pygame.mouse.get_pos()
            for rect in self.options_rects:
                if rect.collidepoint(mouse_pos):
                    pygame.draw.rect(self.screen, self.highlight_color, rect, 2)
                else:
                    pygame.draw.rect(self.screen, self.normal_color, rect, 2)

            pygame.display.flip()
            self.clock.tick(FPS)
