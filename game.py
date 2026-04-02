import pygame
from bird import Bird

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.clock = pygame.time.Clock()

        #Gestion joueur
        self.bird_co = (0, 0)
        self.bird = Bird(self.bird_co)


        #Gestion jeu
        self.gravity = 0.5


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.bird.move()

            self.update()
            self.clock.tick(60)

        pygame.quit()

    def update(self):
        self.screen.fill((100, 100, 100))

        self.bird.velocity += self.gravity
        self.bird.update()

        self.screen.blit(self.bird.image, (self.bird.x, self.bird.y))
        pygame.display.flip()