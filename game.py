import pygame

from flappy import Flappy


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.clock = pygame.time.Clock()
        self.flap = Flappy(self.screen,self.clock)


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.flap.bird.move()

            self.flap.update()
            self.clock.tick(60)

        pygame.quit()

