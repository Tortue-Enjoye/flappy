
import pygame

from flappy import Flappy
from menu import Menu
from scoreboard import Scoreboard
from scoreboardHard import ScoreboardHard
from utils import resource_path


class Game:
    def __init__(self):
        pygame.init()

        import ctypes
        if hasattr(ctypes, 'windll'):
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("flappy.bird.game")

        icon = pygame.image.load(resource_path("assets/images/cloud.png"))
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Flappy Bird")
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.lives = 3
        self.menu = Menu(self.screen, self.clock)

    def run(self):
        current = "menu"

        while True:
            if current == "menu":
                result = self.menu.run()
                if result == True or result == 'hard':
                    self.lives = 1 if result == 'hard' else 3
                    current = "game"


                elif result == "score" or result == "score_hard":
                    current = "score_hard" if result == "score_hard" else "score"



                elif result == "hard":
                    if self.lives == 3:
                        self.lives = 1
                    else:
                        self.lives = 3
                    current = "menu"


                else:
                    break

            elif current == "game":
                result = Flappy(self.screen, self.clock,self.lives).run()
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
            elif current == "score_hard":
                result = ScoreboardHard(self.screen, self.clock).run()
                if result == "quit":
                    break
                else:
                    current = "menu"

        pygame.quit()