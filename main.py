import pygame
from pygame.locals import *
import os
# to-do: sys.exit() when exiting game
# Put in main gameplay loop later
import sys
# Use for obstacle placement later
import random
from chicken import Chicken
from tree import Tree
from hawk import Hawk
from background import Background
from allBackgrounds import AllBackgrounds
# Something I found that places window in center of display
os.environ['SDL_VIDEO_CENTERED'] = '1'

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GROUND_HEIGHT = SCREEN_HEIGHT - 70
PLAY_GAME = True

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chicken Run')

clock = pygame.time.Clock()
FPS = 30
#Possible audio later

def draw_text(text, font_name, size, text_color, position_x, position_y, position):

  font = pygame.font.Font(font_name, size)  # loads font

  text_plane = font.render(text, True, text_color)  # renders text in the selected font
  text_rect = text_plane.get_rect()

  # setting text position
  if position == "midtop":
      text_rect.midtop = (int(position_x), int(position_y))
  elif position == "topright":
      text_rect.topright = (int(position_x), int(position_y))

  window.blit(text_plane, text_rect)  # draws the text on the screen

def load_image(path, size_x=0, size_y=0):
   image = pygame.image.load(path).convert_alpha()

   if size_x > 0 and size_y > 0:
    image = pygame.transform.scale(image, (size_x, size_y))

    return image, image.get_rect()
   
def load_sprites(image_path, image_name_prefix, number_of_image, size_x=0, size_y=0):
  #image list
  images = []
  # Gets image path, takes image name, and puts extension into string
  for i in range(0, number_of_image):
    path = image_path + image_name_prefix + str(i) + '.png' 
    image = pygame.image.load(path).convert_alpha
    
    # Resizes image to given size
    if size_x > 0 and size_y > 0:
      image = pygame.transform.scale(image, (size_x, size_y))
      
    images.append(image)
  
  return images


def Start_Game():
  run = True
  play_again = False
  game_over = False
  # Game speed later
  
  # Main gameplay loop.
  while run:
    clock.tick(FPS)
        
  # Will keep the main loop running as long as the player wants to play it.  
  while PLAY_GAME:
    PLAY_GAME = Start_Game()
