
import pygame
# Tiejekeneir

class Inputman(object):
    def __init__(self, game):
        self.game = game




class PyGameInputman(Inputman):
#    def __init__(self, game):
#        super(Inputman, self).__init__()

    def process(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.quit()
                if event.key == pygame.K_UP:
                    self.game.move_paddle(0, 0)
                if event.key == pygame.K_DOWN:
                    self.game.move_paddle(0,480)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.game.stop_paddle(0,0)
