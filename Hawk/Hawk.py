from main import load_sprites, GROUND_HEIGHT
import os
import random
import pygame
TRACK_POSITION = 620

class Hawk:
  BIRD_HEIGHTS: list = [30, 50, 60, 90, 110]
  
  def __init__(self, x):
    self.hawk_images = load_sprites('Assets/Hawk/', 'Hawk_', 100, 75)

