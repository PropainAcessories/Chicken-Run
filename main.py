import pygame
# imports EVERYTHING from pygame, will shrink later.
from pygame.locals import *
import os
import sys
# Use for obstacle placement later
# import random
# from chicken import Chicken
# from tree import Tree
# from hawk import Hawk

# kameron's comment


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


# Re-usable functions for drawing text such as game over, menus, etc
# All three functions below may need tweaking as we get to initializing assets.
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

# Re-usable function for loading images
def load_image(path, size_x=0, size_y=0):
  
  image = pygame.image.load(path).convert_alpha()

  if size_x > 0 and size_y > 0:
    image = pygame.transform.scale(image, (size_x, size_y))

  return image, image.get_rect()

# Re=usable function to load sprites into the game.
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

# Defines the background classs
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

# Loads all the backgrounds together.
# Extends background class into a class that combines
# All four seperate assets into a background.
class AllBackgrounds:
  def __init__(self, game_speed):
    self.background_0 = Background("Assets/Background/background-0.png", game_speed)
    self.background_1 = Background("Assets/Background/background-1.png", game_speed - 12)
    self.background_2 = Background("Assets/Background/background-2.png", game_speed - 13)
    self.background_3 = Background("Assets/Background/background-3.png", game_speed - 14)
        
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

class GameOver:
  def __init__(self):
    self.replay_image, self.rect = load_image('Assets/game_over/replayBtn.png', 200, 60)

    self.rect.center = (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))
  
  def draw(self):
    draw_text('GAME OVER', 'Assets/font/northcliff_stencil.otf', 80, (255, 0, 0),
      SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3, 'midtop')
    window.blit(self.replay_image, self.rect)

def Start_Game():
  run = True
  play_again = False
  game_over = False
  # Number of pixels the game moves
  game_speed = 15
  backgrounds = AllBackgrounds(game_speed)
  game_over_modal = GameOver()
  # Main gameplay loop.
  while run:
    clock.tick(FPS)
    
    # some event handling
    for event in pygame.event.get():
      # Quits pygame and exits the program
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      
      if event.type == pygame.MOUSEBUTTONDOWN:
         # Gets mouse click coordinates
        mx, my = pygame.mouse.get_pos()
        # detects if the mouse clicks the game over screen to play again
        if game_over:
        # checks if the play again button is clicked
          if game_over_modal.rect.left < mx < game_over_modal.rect.right and \
                  game_over_modal.rect.top < my < game_over_modal.rect.bottom:
              play_again = True
              run = False

             #Listens for keys to get pressed
    key = pygame.key.get_pressed()
    
    if key[K_SPACE] or key[K_UP]:
      if game_over:
        play_again = True
        run = False
      # elif for jumping while chicken is alive
  # Draw functions for our assets
  
    # Unseal once we have chicken, this function makes the background scroll
    # Does most of the work for the running chicken Chicken.run() will mostly
    # animate the chicken by iterating through the run images.
    
    # backgrounds.update()
    
    
    window.fill((0, 0, 0))
    backgrounds.draw()
    
    
  
    if game_over:
      game_over_modal.draw()
  # else will go here for the score, backgrounds, and obstacles to update
  # As well as for speeds to change and to check collisions
    pygame.display.flip()
  return play_again

  # Will keep the main loop running as long as the player wants to play it.  
while PLAY_GAME:
  PLAY_GAME = Start_Game()
