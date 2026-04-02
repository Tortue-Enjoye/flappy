import pygame

class Pipe:
    def __init__(self,x,y,width,height,direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.image = pygame.image.load('assets/images/pipe.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image= pygame.transform.rotate(self.image, self.direction)

    def update(self,speed):
        self.x -= speed
