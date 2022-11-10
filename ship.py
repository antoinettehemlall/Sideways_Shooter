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

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Movement flag

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # update rect object from position attribures
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw ship at its current location."""
        self.screen.blit(self.image , self.rect)