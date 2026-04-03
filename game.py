
import pygame

from flappy import Flappy
from menu import Menu
from scoreboard import Scoreboard

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

    def run(self):
        current = "menu"

        while True:
            if current == "menu":
                result = Menu(self.screen, self.clock).run()
                if result == True:
                    current = "game"
                elif result == "score":
                    current = "score"
                else:
                    break

            elif current == "game":
                result = Flappy(self.screen, self.clock).run()
                if result == "quit":
                    break
                else:
                    current = "menu"

            elif current == "score":
                result = Scoreboard(self.screen, self.clock).run()
                if result == "quit":
                    break
                else:
                    current = "menu"

        pygame.quit()