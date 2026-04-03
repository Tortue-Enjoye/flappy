import pygame
from utils import resource_path


class Cloud:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.image = pygame.image.load(resource_path('assets/images/cloud.png'))
        self.image = pygame.transform.scale(self.image, (width, height))

    def update(self,speed):
        self.x -= speed
