import pygame

class Cloud:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.image = pygame.image.load('assets/images/cloud.png')
        self.image = pygame.transform.scale(self.image, (width, height))

    def update(self,speed):
        self.x -= speed
