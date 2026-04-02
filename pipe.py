import pygame

class Pipe:
    def __init__(self,x,y,width,height,direction):
        self.x = x
        self.y = y
        self.direction = direction

        self.image = pygame.image.load('assets/images/pipe.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        if direction == 180:
            self.image = pygame.transform.flip(self.image, False, True)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self,speed):
        self.x -= speed
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
