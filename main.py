
import pygame
from ship import Ship
from settings import Settings
import game_functions as gf

def run_game():
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Mac's Alien Invasion")
  ship = Ship(screen)
  while True:
    gf.check_events()
    gf.update_screen(ai_settings, screen, ship)   
run_game()
