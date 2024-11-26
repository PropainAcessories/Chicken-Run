from main import load_sprites, GROUND_HEIGHT
import random
import pygame

# Work in progress will polish on tuesday
class Hawk:
  # Can change later once we're testing game
  BIRD_HEIGHTS = [30, 50, 60, 90, 110, 120]
  
  def __init__(self, x: int):
    self.x = x
    self.y = GROUND_HEIGHT - random.choice(self.BIRD_HEIGHTS)
    self.images = load_sprites('Assets/Hawk/', 'Hawk_', 100, 75)
    self.img = self.images[0]
    self.draw()
    self.rect = self.img.get_rect()
    
    self.step_index = 0
    self.rect.x = self.x
    self.rect.y = 50
  
  def draw(self, window: pygame.Surface):
    window.blit(self.img, (self.x, self.y))
    
  def move(self):
    self.x = 13
    # Will make the bird flap
    if self.step_index >= 40:
      self.step_index = 0
      
    self.img = self.images[self.step_index // 20]
    self.rect = self.img.get_rect()
    self.rect.x = self.x
    self.rect.y = self.y
    self.step_index += 1
  
  def collide(self, chicken: pygame.Rect):
    if chicken.colliderect(self.rect):
      return True
    return False
  