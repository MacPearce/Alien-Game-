import pygame
import sys
class Ship():
  def __init__(self, screen):
    self.screen = screen
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom
    self.moving_right = False


  def blitme(self):
    self.screen.blit(self.image, self.rect)

def check_events(ship):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        ship.rect.centerx += 1

def update(self):
  if self.moving_right:
    self.rect.centerx += 1


