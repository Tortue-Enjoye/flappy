# menu.py
import pygame

class Menu:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.font = pygame.font.SysFont(None, 72)
        self.font_small = pygame.font.SysFont(None, 36)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_rect.collidepoint(event.pos):
                        return True
                    if self.quit_rect.collidepoint(event.pos):
                        return False

            self.draw()
            self.clock.tick(60)

    def draw(self):
        self.screen.fill((144, 213, 255))

        # Titre
        title = self.font.render("Flappy Bird", True, (255, 255, 255))
        self.screen.blit(title, (400 - title.get_width() // 2, 150))

        # Bouton Joueur
        play_text = self.font_small.render("Jouer", True, (255, 255, 255))
        self.play_rect = play_text.get_rect(center=(400, 320))
        self.screen.blit(play_text, self.play_rect)

        # Bouton Quitter
        quit_text = self.font_small.render("Quitter", True, (255, 255, 255))
        self.quit_rect = quit_text.get_rect(center=(400, 390))
        self.screen.blit(quit_text, self.quit_rect)

        pygame.display.flip()