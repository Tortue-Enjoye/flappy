# menu.py
import pygame

class Menu:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.font = pygame.font.Font("assets/fonts/JetBrainsMono-Bold.ttf", 72)
        self.font_small = pygame.font.Font("assets/fonts/JetBrainsMono-Bold.ttf", 48)
        self.font_hover = pygame.font.Font("assets/fonts/JetBrainsMono-Bold.ttf", 64)

        self.play_rect = pygame.Rect(0, 0, 0, 0)
        self.quit_rect = pygame.Rect(0, 0, 0, 0)

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

        mouse_pos = pygame.mouse.get_pos()

        # Titre
        title = self.font.render("Flappy Bird", True, (0, 76, 153))
        self.screen.blit(title, (400 - title.get_width() // 2, 150))

        # Bouton Jouer
        if self.play_rect.collidepoint(mouse_pos):
            play_text = self.font_hover.render("Jouer", True, (0, 76, 153))
        else:
            play_text = self.font_small.render("Jouer", True, (0, 0, 0))

        self.play_rect = play_text.get_rect(center=(400, 320))
        self.screen.blit(play_text, self.play_rect)

        # Bouton Quitter
        if self.quit_rect.collidepoint(mouse_pos):
            quit_text = self.font_hover.render("Quitter", True, (0, 76, 153))
        else:
            quit_text = self.font_small.render("Quitter", True, (0, 0, 0))

        self.quit_rect = quit_text.get_rect(center=(400, 390))
        self.screen.blit(quit_text, self.quit_rect)

        pygame.display.flip()