import pygame

class Ship:

    def __init__(self, ss_game):
        """Set starting position of ship."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Load ship image
        self.image = pygame.image.load('images/Sideways_rocket_image.bmp')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        """Draw ship at its current location."""
        self.screen.blit(self.image , self.rect)