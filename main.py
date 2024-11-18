import pygame
from pygame.locals import *

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


def Start_Game():
  run = True
  play_again = False
  game_over = False
  # Game speed later
  
  while run:
    clock.tick(FPS)
    
    
  # Will keep the main loop running as long as the player wants to play it.  
  while PLAY_GAME:
    PLAY_GAME = Start_Game()