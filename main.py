import pygame.display, pygame.time, pygame.event, pygame.key, pygame.font, pygame.surface
from pygame.locals import QUIT, K_SPACE, K_UP

import os
import sys

import random




# Something I found that places window in center of display
os.environ['SDL_VIDEO_CENTERED'] = '1'
# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GROUND_HEIGHT = SCREEN_HEIGHT - 190
PLAY_GAME = True
# Globals and boilerplate
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chicken Run')
clock = pygame.time.Clock()
# Constant, controls how many times per second the screen updates.
FPS = 24
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
  # Takes filepath and converts to pixels
  image = pygame.image.load(path).convert_alpha()
  # Scales my image
  if size_x > 0 and size_y > 0:
    image = pygame.transform.scale(image, (size_x, size_y))
  # Returns my image and that sweet sweet rectangle
  return image, image.get_rect()

# Re=usable function to load sprites into the game.
def load_sprites(image_path, image_name_prefix, number_of_image, size_x=0, size_y=0):
  #image list
  images = []
  # Gets image path, takes image name, and puts extension into string
  for i in range(0, number_of_image):
    path = image_path + image_name_prefix + str(i) + '.png' 
    image = pygame.image.load(path).convert_alpha()
    
    # Resizes image to given size
    if size_x > 0 and size_y > 0:
      image = pygame.transform.scale(image, (size_x, size_y))

    images.append(image)
  
  return images

# Defines the background classs
class Background:
  def __init__(self, image_path, speed = 10):
    # load the background images to the screen
    self.image0, self.rect0 = load_image(image_path, 1280, 720)
    self.image1, self.rect1 = load_image(image_path, 1280, 720)
    # Set the rectangles
    self.rect0.bottom = SCREEN_HEIGHT
    self.rect1.bottom = SCREEN_HEIGHT
    # Keep the rectangles coming, infinite rectangles.
    self.rect1.left = self.rect0.right
    
    self.speed = speed
  # Blit my rectangles onto the screen    
  def draw(self):
    window.blit(self.image0, self.rect0)
    window.blit(self.image1, self.rect1)
  # Move my rectangles.
  def update(self):
    self.rect0.left -= int(self.speed)
    self.rect1.left -= int(self.speed)
    # keep making rectangles.
    if self.rect0.right < 0:
      self.rect0.left = self.rect1.right


    if self.rect1.right < 0:
      self.rect1.left = self.rect0.right

# Loads all the backgrounds together.
# Extends background class into a class that combines
# All four seperate assets into a background.
class AllBackgrounds:
  def __init__(self, game_speed):
    self.background_0 = Background("Assets/Background/background_0.png", game_speed)
    self.background_1 = Background("Assets/Background/background_1.png", game_speed - 12)
    self.background_2 = Background("Assets/Background/background_2.png", game_speed - 13)
    self.background_3 = Background("Assets/Background/background_3.png", game_speed - 14)
  # Update the speed to the backgrounds      
  def update_speed(self, speed):
    self.background_0.speed = speed
    self.background_1.speed = speed - 12
    self.background_2.speed = speed - 13
    self.background_3.speed = speed - 14
  # Draws backgrounds in desired order, renders in first to last order
  # 3,2,1,0  
  def draw(self):
    self.background_3.draw()
    self.background_2.draw()
    self.background_1.draw()
    self.background_0.draw()
  # moves backgrounds
  def update(self):
    self.background_3.update()
    self.background_2.update()
    self.background_1.update()
    self.background_0.update()

class GameOver:
  def __init__(self):
    # Button and hitbox
    self.replay_image, self.rect = load_image('Assets/game_over/replayBtn.png', 200, 60)
    # Center my button
    self.rect.center = (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))
  # Blit button to screen
  def draw(self):
    draw_text('GAME OVER', 'Assets/font/northcliff_stencil.otf', 80, (255, 0, 0),
      SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3, 'midtop')
    window.blit(self.replay_image, self.rect)
    
# class Hawk:
#   # Can change later once we're testing game
#   BIRD_HEIGHTS = [30, 50, 60, 90, 110, 120]
  
#   def __init__(self, speed = 10):
#     # May need to adjust sprite size
#     self.hawk_images = load_sprites('Assets/Hawk/', 'Hawk_', 5,  160, 160)
    
#     self.hawk_image_0, self.rect_0 = self.hawk_images[0], self.hawk_images[0].get_rect()
#     self.hawk_image_0, self.rect_0 = self.hawk_images[1], self.hawk_images[1].get_rect()

#     # May need to adjust rectangle size
#     self.step_index = 0
#     self.rect.x = self.x
#     self.rect.y = 50
  
#   def draw(self, window: pygame.Surface):
#     window.blit(self.img, (self.x, self.y))
    
#   def move(self):
#     self.x = 13
#     # Will make the bird flap
#     # May need to adjust speed.
#     if self.step_index >= 40:
#       self.step_index = 0
      
#     self.img = self.images[self.step_index // 20]
#     self.rect = self.img.get_rect()
#     self.rect.x = self.x
#     self.rect.y = self.y
#     self.step_index += 1
  
  # def collide(self):
    
class Tree:
  def __init__(self, speed = 10):
    # filepath, assetName_, number of images, size x, size y
    self.tree_images = load_sprites('Assets/trees/', 'tree_', 5,  160, 160)
    # Will make more trees later.
    self.tree_image_0, self.rect_0 = self.tree_images[0], self.tree_images[0].get_rect()
    self.tree_image_1, self.rect_1 = self.tree_images[1], self.tree_images[0].get_rect()
    # Render the bottom and left of the tree
    self.rect_0.bottom = GROUND_HEIGHT - 11
    self.rect_0.left = SCREEN_WIDTH
    # Where the bottom and left of the tree rect
    self.rect_1.bottom = GROUND_HEIGHT - 11
    self.rect_1.left = self.rect_0.right + int(SCREEN_WIDTH/2)
    # The speed in which the trees move
    self.speed = speed
    # speed
    self.range_0 = 240
    self.range_1 = 720
  # Tree and hitbox for collision checking in Chicken() class
  def get_tree(self):
    current_tree = [self.tree_image_0, self.tree_image_1]
    tree_rect = [self.rect_0, self.rect_1]
    
    return current_tree, tree_rect
  # Increase the speed of the trees
  def update_speed(self, speed):
    self.speed = speed
    self.range_0 += 1
    self.range_1 += 1
  # Blit the trees onto the screen  
  def draw(self):
    window.blit(self.tree_image_0, self.rect_0)
    window.blit(self.tree_image_1, self.rect_1)
  # Keep the trees moving
  def update(self):
    # Moves the t rees
    self.rect_0.left -= int(self.speed)
    self.rect_1.left -= int(self.speed)
    # Keeps placing and moving trees. Also randomly picks between tree images
    if self.rect_0.right < 0:
      temp_position = random.randrange(self.range_0, self.range_1)
      
      
      if temp_position > SCREEN_WIDTH:
        self.rect_0.left = temp_position
      else:
        self.rect_0.left = SCREEN_WIDTH
      
      self.tree_image_0 = self.tree_images[random.randrange(0, 5)]
      
    if self.rect_1.right < 0:
      temp_position = random.randrange(self.range_0, self.range_1)  
        
      if temp_position > SCREEN_WIDTH:
        self.rect_1.left = temp_position
      else:
        self.rect_1.left = SCREEN_WIDTH
      
      self.tree_image_1 = self.tree_images[random.randrange(0, 5)]
    
class Chicken:
  def __init__(self):
    # number of images, 220, 155, Can add more sprites for smoother animation
    self.idle_chicken = load_sprites('Assets/chicken/', 'idle_', 2, 220, 155)
    self.running_chicken = load_sprites('Assets/chicken/', 'run_', 2, 220, 155)
    self.jumping_chicken = load_sprites('Assets/chicken/', 'jump_', 2, 220, 155)
    
    self.rect = self.idle_chicken[0].get_rect()
    #bottom of the rectangle and left of chicken rectangle
    self.rect.bottom = GROUND_HEIGHT
    self.rect.left = 70
    #jump physics
    self.jump_limit = GROUND_HEIGHT - 290
    self.jump_speed = 50
    self.gravity_up = 4
    self.gravity_down = 2
    #indexes this keeps track of what image
    #the sprite is on
    self.idle_index = 0
    self.running_index = 0
    self.jumping_index = 0
    
    #idle physics
    self.idle = True
    self.running = False
    self.jumping = False
    self.falling = False
    # Checks the call count on the chicken sprites
    # During their animation
    self.call_count = 0
  # Need to check collision with hawk, still have unfinished hawk.
  def check_collision(self, all_tree):
    # Checks if the chicken is running, jumping or idle and loads the appropriate images
    # The mask takes the appropriate index of images from the loadsprites()
    # and the appropriate number from the index
    if self.running:
      chicken_mask = pygame.mask.from_surface(self.running_chicken[self.running_index])
    elif self.jumping:
      chicken_mask = pygame.mask.from_surface(self.jumping_chicken[self.jumping_index])
    else:
      chicken_mask = pygame.mask.from_surface(self.idle_chicken[self.idle_index])
    # Declaration of the trees and hitboxes
    current_tree, tree_rect = all_tree
    #  hitboxes
    offset_0 = (tree_rect[0].left - self.rect.left, tree_rect[0].top - self.rect.top)
    offset_1 = (tree_rect[1].left - self.rect.left, tree_rect[1].top - self.rect.top)
    # Defining if the chicken sprite overlaps with the tree hitboxes
    collide = chicken_mask.overlap(pygame.mask.from_surface(current_tree[0]), offset_0) or \
      chicken_mask.overlap(pygame.mask.from_surface(current_tree[1]), offset_1)
      
    return collide
  
  def draw(self):
    # Blits the appropriate chicken sprite to the string
    if self.running:
      window.blit(self.running_chicken[self.running_index], self.rect)
    elif self.jumping:
      window.blit(self.jumping_chicken[self.jumping_index], self.rect)
    elif self.idle:
      window.blit(self.idle_chicken[self.idle_index], self.rect)
  # does the animation using call count and some math to check if at end of image loop.
  # Math may/may not need to be changed if adding extra images to smooth animations
  def update(self):
    if self.running and self.call_count % 3 == 0:
      self.running_index = (self.running_index + 1) % 2
      # Chicken is jumping
    elif self.jumping:
      if not self.falling:
        self.rect.bottom -= self.jump_speed
        
        if self.jump_speed >= self.gravity_up:
          self.jump_speed -= self.gravity_up
          # Fall when you reach the jump limit
        if self.rect.bottom < self.jump_limit:
          self.jump_speed = 0
          self.falling = True
      # Fall damn you
      else:
        self.rect.bottom += self.jump_speed
        self.jump_speed += self.gravity_down
        # Chicken is running
        if self.rect.bottom > GROUND_HEIGHT:
          self.rect.bottom = GROUND_HEIGHT
          self.jump_speed = 50
          # Reset the indices
          self.jumping_index = 0
          self.running_index = 0
          # Run
          self.jumping = False
          self.falling = False
          self.running = True
      # Need index back to 0 to restart sprite
      if self.call_count % 2 == 0 or self.call_count % 3 == 0:
        self.jumping_index = (self.jumping_index + 1) % 2
    # Reset idle sprite    
    elif self.idle and self.call_count % 3 == 0:
      self.idle_index = (self.idle_index + 1) % 2
    # add to call count  
    self.call_count = self.call_count + 1
    
    
def Start_Game():
  # Booleans for loop
  run = True
  play_again = False
  game_over = False
  # Number of pixels the game moves
  game_speed = 15
  # Asset class declarations
  backgrounds = AllBackgrounds(game_speed)
  chicken = Chicken()
  tree = Tree(game_speed)
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
    # Event handling, possible pause here?
    if key[K_SPACE] or key[K_UP]:
      if game_over:
        play_again = True
        run = False
      elif not chicken.jumping:
        chicken.jumping = True
        chicken.running = False
        
        if chicken.idle:
          chicken.idle = False

    # Fill the window, and render the background, chicken, and trees.
    window.fill((0, 0, 0))
    backgrounds.draw()
    tree.draw()
    chicken.draw()
    # Game is over
    if game_over:
      game_over_modal.draw()
    else:
    # Run the game if the chicken is not idle
      if not chicken.idle:
        backgrounds.update()
        tree.update()
      chicken.update()
      # End the game if you hit a tree
      if chicken.check_collision(tree.get_tree()):
        game_over = True
        game_over_modal.draw()
        
    pygame.display.flip()
    
  return play_again

  # Will keep the main loop running as long as the player wants to play it.  
while PLAY_GAME:
  PLAY_GAME = Start_Game()
