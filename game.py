
import pygame

from flappy import Flappy
from menu import Menu
from scoreboard import Scoreboard
from utils import resource_path


class Game:
    def __init__(self):
        pygame.init()

        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("flappy.bird.game")

        icon = pygame.image.load(resource_path("assets/images/cloud.png"))
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Flappy Bird")
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