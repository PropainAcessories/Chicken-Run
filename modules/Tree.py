from main import load_sprites, GROUND_HEIGHT

class Tree:
  def __init__(self, image_path, speed = 10):
    self.tree_images = load_sprites('Assets/trees/Trees.png')