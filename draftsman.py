
import pygame
# Tiejekeneir

class Draftsman(object):
    def __init__(self, game):
        self.game = game

        


class PyGameDraftsman(Draftsman):
    black    = (   0,   0,   0)
    white    = ( 255, 255, 255)

    def __init__(self, game):
        super(Draftsman, self).__init__()

        self.surface = pygame.display.set_mode((640,480))

    def draw(self, items):
        self.surface.fill(self.white)
        for item in items:
            self.draw_item(self.surface,item)
        pygame.display.flip()
        

    def draw_item(self, surface,item):
        if item.shape == 'circle':
            pygame.draw.circle(surface,self.black,(int(item.x),int(item.y)),item.radius,0)
        elif item.shape == 'rectangle':
            x = item.x - item.width/2
            y = item.y - item.height/2
            pygame.draw.rect(surface, self.black, (x,y,item.width,item.height), 0)
        else:
            print 'You are in bad shape.'