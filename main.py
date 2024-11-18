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