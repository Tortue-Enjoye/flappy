
import pygame

from flappy import Flappy
from menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            menu = Menu(self.screen, self.clock)
            if not menu.run():
                break

            flap = Flappy(self.screen, self.clock)
            result = flap.run()

            if result == "quit":
                break

            if result == "score":


        pygame.quit()

        pygame.quit()