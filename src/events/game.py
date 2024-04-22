import pygame
from characters.mother_bear import MotherBear

class Game:
    def __init__(self, FPS):
        pygame.init()
        self.player = MotherBear()
        self.screen_width = 800  # Assume some screen width
        self.world_width = 2400  # Assume some total level width wider than the screen
        try:
            self.background = pygame.image.load('src/assets/Temp Game Background.png').convert()
            self.background_width = self.background.get_width()
        except pygame.error as e:
            print(f"Failed to load the background image: {e}")
            raise SystemExit
        self.background_pos = 0
        self.FPS = FPS
        self.camera_offset = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        return True

    def update_background(self):
        player_x = self.player.rect.x
        right_boundary = self.screen_width * 0.7
        left_boundary = self.screen_width * 0.3

        # Scroll right
        if player_x > right_boundary and self.camera_offset < self.world_width - self.screen_width:
            shift = player_x - right_boundary
            self.camera_offset += shift
            self.player.rect.x = right_boundary
        
        # Scroll left
        elif player_x < left_boundary and self.camera_offset > 0:
            shift = left_boundary - player_x
            self.camera_offset -= shift
            self.player.rect.x = left_boundary

        self.background_pos = -self.camera_offset

    def render(self, screen):
        # This accounts for any position of the background
        screen.blit(self.background, (self.background_pos, 0))
        self.player.draw(screen)

    def run(self, screen):
        clock = pygame.time.Clock()
        running = True
        while running:
            running = self.handle_events()
            self.player.handle_keys()
            self.player.update()
            self.update_background()
            self.render(screen)
            pygame.display.flip()
            clock.tick(self.FPS)
