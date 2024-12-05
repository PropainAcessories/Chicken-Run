
# #Score functions; will need to be fine tuned later
# class Score:
#   def _init_(self):
#     self.score = 0
#     self.font = pygame.font.Font(None,0) 
#     self.color = (0,0,0) #black font color
  
#   def update(self, speed):
#     self.score += speed #Increase the score the longer you play
#     return self.score
  
#   def display(self, screen):
#     score_surface = self.font.render(f"Score: {self.score}", True, self .color)
#     score_rect = score_surface.get_rect(center=(100, 50))
#     screen.blit(score_surface, score_rect)