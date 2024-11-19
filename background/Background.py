import pygame
from main import SCREEN_HEIGHT, load_image, window

class Background:
    
  def __init__(self, image_path, speed = 10):
    
    self.image0, self.rect0 = load_image(image_path, 1280, 720)
    self.image1, self.rect1 = load_image(image_path, 1280, 720)
    
    self.rect0.bottom = SCREEN_HEIGHT
    self.rect1.bottom = SCREEN_HEIGHT
    
    self.rect1.left = self.rect0.right
    
    self.speed = speed
    
  def draw(self):
    window.blit(self.image0, self.rect0)
    window.blit(self.image1, self.rect1)
      
  def update(self):
    self.rect0.left -= int(self.speed)
    self.rect1.left -= int(self.speed)
      
    if self.rect0.right < 0:
      self.rect0.left = self.rect1.right
        
    if self.rect1.right < 0:
      self.rect1.left = self.rect0.right
