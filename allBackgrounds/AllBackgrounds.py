import pygame
from background import Background

class AllBackgrounds:
  
  def __init__(self, game_speed):
        self.background_0 = Background("Assets/Background/Background-0.png", game_speed)
        self.background_1 = Background("Assets/Background/Background-1.png", game_speed - 12)
        self.background_2 = Background("Assets/Background/Background-2.png", game_speed - 13)
        self.background_3 = Background("Assets/Background/Background-3.png", game_speed - 14)
        
  def update_speed(self, speed):
    self.background_0.speed = speed
    self.background_1.speed = speed - 12
    self.background_2.speed = speed - 13
    self.background_3.speed = speed - 14
    
  def draw(self):
    self.background_3.draw()
    self.background_2.draw()
    self.background_1.draw()
    self.background_0.draw()
  
  def update(self):
    self.background_3.update()
    self.background_2.update()
    self.background_1.update()
    self.background_0.update()
