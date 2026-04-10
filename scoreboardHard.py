import pygame
import json
import os
from utils import resource_path


class ScoreboardHard:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.font = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 48)
        self.font_small = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 32)
        self.font_hover = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 42)
        self.back_rect = pygame.Rect(0, 0, 0, 0)
        self.scores = self.load_scores()

    def load_scores(self):
        if os.path.exists("scores_hard.json"):
            with open("scores_hard.json", "r") as f:
                return json.load(f)
        return []

    @staticmethod
    def save_score(score):
        """Appelé depuis Flappy après game over"""
        scores = []
        if os.path.exists("scores_hard.json"):
            with open("scores_hard.json", "r") as f:
                scores = json.load(f)
        scores.append(score)
        scores = sorted(scores, reverse=True)[:10]  # garde les 10 meilleurs
        with open("scores_hard.json", "w") as f:
            json.dump(scores, f)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_rect.collidepoint(event.pos):
                        return "menu"

            self.draw()
            self.clock.tick(60)

    def draw(self):
        self.screen.fill((144, 213, 255))
        mouse_pos = pygame.mouse.get_pos()

        # Titre
        title = self.font.render("Meilleurs Scores Hardcore", True, (0, 76, 153))
        self.screen.blit(title, (400 - title.get_width() // 2, 40))

        # Liste des scores
        for i, score in enumerate(self.scores):
            text = self.font_small.render(f"{i+1}.  {score}", True, (0, 0, 0))
            self.screen.blit(text, (400 - text.get_width() // 2, 120 + i * 40))

        # Bouton retour
        if self.back_rect.collidepoint(mouse_pos):
            back_text = self.font_hover.render("← Retour", True, (0, 76, 153))
        else:
            back_text = self.font_small.render("← Retour", True, (0, 0, 0))
        self.back_rect = back_text.get_rect(center=(400, 550))
        self.screen.blit(back_text, self.back_rect)

        pygame.display.flip()