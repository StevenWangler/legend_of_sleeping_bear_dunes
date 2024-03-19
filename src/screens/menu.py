import pygame
import sys
from screens.settings import SettingsScreen
from app_settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

class Menu:

    def __init__(self, screen, clock):
            """
            Initializes the Menu object.

            Args:
                screen (pygame.Surface): The surface to draw the menu on.
                clock (pygame.time.Clock): The clock object to control the frame rate.

            Attributes:
                menu_options (list): The list of menu options.
                font (pygame.font.Font): The font used for rendering text.
                options_rects (list): The list of rectangles for each menu option.
                bg_color (tuple): The background color of the menu.
                text_color (tuple): The color of the menu text.
                highlight_color (tuple): The color of the highlighted menu option.
                normal_color (tuple): The color of the non-highlighted menu options.
                title_font (pygame.font.Font): The font used for rendering the title.
                title_text (pygame.Surface): The rendered title text.
                background (pygame.Surface): The background image of the menu.
            """
            self.screen = screen
            self.clock = clock
            self.menu_options = ['Start', 'Load', 'Settings', 'Quit']
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
        """
        Draws the menu on the screen.

        This method fills the screen with the background color, displays the title text,
        draws the background image, and renders and displays the menu options as buttons.

        Returns:
            None
        """
        self.screen.fill(self.bg_color)
        title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200))  # Customize your title position
        self.screen.blit(self.title_text, title_rect)
        del self.options_rects[:]  # Clear previous rects to avoid duplication
        self.screen.blit(self.background, (0, 0))  # Draw the background image
        for index, option in enumerate(self.menu_options):
            text = self.font.render(option, True, self.text_color)
            rect = text.get_rect(center=(SCREEN_WIDTH // 2 - 300 + 200 * index, SCREEN_HEIGHT // 2))  # Change here for x-coordinate
            button_rect = pygame.Rect(rect.left - 20, rect.top - 10, rect.width + 40, rect.height + 20)  # Add padding for button
            pygame.draw.rect(self.screen, self.normal_color, button_rect)  # Draw button background
            self.options_rects.append(button_rect)  # Use button rect for collision
            self.screen.blit(text, rect)


    def main_menu(self):
        """
        Displays the main menu screen and handles user input.

        This method continuously runs a loop to handle events and update the menu screen.
        It checks for user input such as mouse clicks and updates the screen accordingly.
        The method also highlights the menu options when the mouse hovers over them.

        Returns:
            None
        """
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
                        #running = False
                    elif self.options_rects[1].collidepoint(mouse_pos):
                        print("Load game")  # Placeholder for loading a game
                    elif self.options_rects[2].collidepoint(mouse_pos):
                        # Instantiate the settings screen and call its main method
                        settings_screen = SettingsScreen(self.screen, self.clock)
                        settings_screen.main_settings()
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
