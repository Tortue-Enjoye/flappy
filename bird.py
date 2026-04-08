import pygame
from utils import resource_path


class Bird():
    def __init__(self, bird_co):
        self.x = bird_co[0]
        self.y = bird_co[1]

        self.image = pygame.image.load(resource_path('assets/images/bird.png'))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


        self.velocity = 0

    def move(self):
        self.velocity = -13.5


    def update(self):
        self.y += self.velocity
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        if self.y < 1:
            self.y = 2
            self.velocity = -self.velocity*0.3

        if self.y > 530:
            self.y = 529
            self.velocity = -14*0.7