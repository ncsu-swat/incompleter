#Source: https://stackoverflow.com/questions/65802508/attributeerror-pygame-surface-object-has-no-attribute-screen
# Importing modules
import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    '''Class to manage game assets and behavior'''

    def __init__(self):
        '''Constructor to initialize the game and its assets'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self.screen)

    def run_game(self):
        '''Starts the main loop for the game'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        '''Watch for the keyboard and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        '''Redraw the screen during each pass of the loop'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        '''Make the most recently drawn screen visible'''
        pygame.display.flip()


if __name__ == '__main__':
    '''Make a game instance, and run the game'''
    alinv = AlienInvasion()
    alinv.run_game()