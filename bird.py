import pygame

class Bird():
    def __init__(self, bird_co):
        self.image = pygame.image.load('assets/images/bird.png')
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.x = bird_co[0]
        self.y = bird_co[1]

        self.velocity = 0

    def move(self):
        self.velocity = -15


    def update(self):
        self.y += self.velocity

        if self.y < 1:
            self.y = 2
            self.velocity = -self.velocity*0.3

        if self.y > 530:
            self.y = 529
            self.velocity = -15*0.7