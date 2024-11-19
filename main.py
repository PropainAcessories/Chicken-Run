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
   
def load_sprites(image_path, image_name_prefix, number_of_image, size_x=0, size_y=0):
  #image list
  images = []
  
  for i in range(0, number_of_image):
    path = image_path + image_name_prefix + str(i) + '.png' # Gets image path, takes image name, and puts extension into string
    image = pygame.image.load(path).convert_alpha
    
    if size_x > 0 and size_y > 0:
      image = pygame.transform.scale(image, (size_x, size_y)) # Resizes image to given size
      
    images.append(image)
  
  return images

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
    