import math

import draftsman
import inputman
import pygame
import pygame.event
import pygame.time

SPEED = 10
# Pong

class Game(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.field = Field()
        self.draftsman = None
        self.inputman = None
        self.quit_game = False
        

    def run(self):
        while not self.quit_game:
            self.clock.tick(30)
            self.inputman.process()

            
            for item in self.field.items:
                item.update(self.clock.get_time())
                
            self.draftsman.draw(self.field.items)

    def quit(self):
        self.quit_game = True
        
    def move_paddle(self, x, y):
        print 'move', x, y
        paddle = self.field.get_paddle(1)
        paddle.speed = SPEED
        if paddle.y < y:
            paddle.direction = 270
        elif paddle.y > y:
            paddle.direction = 90
        else:
            paddle.speed = 0

    def stop_paddle(self, x, y):
        print 'stop', x, y
        paddle = self.field.get_paddle(1)
        paddle.speed = 0

class Field(object):
    def __init__(self):
        ball = Ball(0, 480, 40, SPEED, 45)
        paddle = Paddle(5, 25, 10, 50, 0, 90)
        self.items = []
        self.items.append(ball)
        self.items.append(paddle)
        self.paddles = {1:paddle}

    def get_paddle(self, paddle_id):
        return self.paddles[paddle_id]

class Item(object):
    def update(self, delta_time):
        radians = math.radians(self.direction)
        delta_x = math.cos(radians) * self.speed
        delta_y = math.sin(radians) * self.speed
        self.x += delta_x
        self.y -= delta_y

class Ball(Item):
    def __init__(self, x, y, radius, speed, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.direction = direction
        self.shape = 'circle'

class Paddle(Item):
    def __init__(self, x, y, width, height, speed, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = direction
        self.shape = 'rectangle'

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.speed = 10
    game.draftsman = draftsman.PyGameDraftsman(game)
    game.inputman = inputman.PyGameInputman(game)
    game.run()