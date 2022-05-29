import sys
import pygame
#from ship import Ship
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((780, 400))
    pygame.display.set_caption("Mac's Alien Invasion")
    bg_color = (128, 0, 128)
    #ship = Ship(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        screen.fill(ai_settings.bg_color)
        #ship.blitme()
        pygame.display.flip()


run_game()
