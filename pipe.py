import pygame

class Pipe:
    def __init__(self,x,y,width,height,direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.passed = False

        self.image = pygame.image.load('assets/images/pipe.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image= pygame.transform.rotate(self.image, self.direction)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    def update(self,speed):
        self.x -= speed
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

