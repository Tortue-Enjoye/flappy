# menu.py
import pygame
from utils import resource_path


class Menu:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.font = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 72)
        self.font_small = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 48)
        self.font_hover = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 64)

        self.image_bird = pygame.image.load(resource_path('assets/images/bird.png'))
        self.image_bird = pygame.transform.scale(self.image_bird, (100, 100))
        self.image_bird_inverted = pygame.transform.flip(self.image_bird, True, False)
        self.timer_anim = 0

        self.image_hard = pygame.image.load(resource_path('assets/images/health.png'))
        self.image_hard_origine = pygame.image.load(resource_path('assets/images/health.png'))
        self.image_hard2_origine = pygame.image.load(resource_path('assets/images/hard.png'))
        self.hardcore = False


        self.image_footer = pygame.image.load(resource_path('assets/images/cloud_footer.png'))

        self.play_rect = pygame.Rect(0, 0, 0, 0)
        self.score_rect = pygame.Rect(0, 0, 0, 0)
        self.quit_rect = pygame.Rect(0, 0, 0, 0)
        self.hard_rect = pygame.Rect(690, 495, 70, 65)

    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_rect.collidepoint(event.pos):
                        return 'hard' if self.hardcore else True
                    if self.quit_rect.collidepoint(event.pos):
                        return False
                    if self.score_rect.collidepoint(event.pos):
                        return 'score_hard' if self.hardcore else 'score'
                    if self.hard_rect.collidepoint(event.pos):
                        self.hardcore = not self.hardcore

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 'hard' if self.hardcore else True




            self.draw(mouse_pos)

            self.clock.tick(60)

    def draw(self,mouse_pos):

        self.screen.fill((144, 213, 255))
        self.timer_anim += 1

        # Titre
        title = self.font.render("Flappy Bird", True, (0, 76, 153))
        self.screen.blit(title, (400 - title.get_width() // 2, 100))

        # Bouton Jouer
        if self.play_rect.collidepoint(mouse_pos):
            play_text = self.font_hover.render("Jouer", True, (0, 76, 153))
        else:
            play_text = self.font_small.render("Jouer", True, (0, 0, 0))

        self.play_rect = play_text.get_rect(center=(400, 250))
        self.screen.blit(play_text, self.play_rect)

        # Bouton score
        if self.score_rect.collidepoint(mouse_pos):
            score_text = self.font_hover.render("Scores", True, (0, 76, 153))
        else:
            score_text = self.font_small.render("Scores", True, (0, 0, 0))

        self.score_rect = score_text.get_rect(center=(400, 320))
        self.screen.blit(score_text, self.score_rect)

        # Bouton Quitter
        if self.quit_rect.collidepoint(mouse_pos):
            quit_text = self.font_hover.render("Quitter", True, (0, 76, 153))
        else:
            quit_text = self.font_small.render("Quitter", True, (0, 0, 0))

        self.quit_rect = quit_text.get_rect(center=(400, 390))
        self.screen.blit(quit_text, self.quit_rect)

        # Footer
        self.screen.blit(self.image_footer, (-20, 300))

        # Bird rotate
        if (self.timer_anim // 45) % 2 == 0:
            self.draw_bird(self.image_bird,0,0,0)
            self.draw_bird(self.image_bird_inverted,0,690,0)

        else :
            self.draw_bird(self.image_bird,45,-10,0)
            self.draw_bird(self.image_bird_inverted,-45,670,0)

        # Hardcore mode
        if self.hardcore == False:
            if self.hard_rect.collidepoint(mouse_pos):
                self.image_hard = self.image_hard_origine
                self.image_hard = pygame.transform.scale(self.image_hard, (70, 65))
                self.screen.blit(self.image_hard, (690,495))
            else:
                self.image_hard = self.image_hard_origine
                self.image_hard = pygame.transform.scale(self.image_hard_origine, (50, 45))
                self.screen.blit(self.image_hard, (700, 500))

        elif self.hardcore == True:
            if self.hard_rect.collidepoint(mouse_pos):
                self.image_hard = self.image_hard2_origine
                self.image_hard = pygame.transform.scale(self.image_hard2_origine, (70, 65))
                self.screen.blit(self.image_hard, (690, 495))
            else:
                self.image_hard = self.image_hard2_origine
                self.image_hard = pygame.transform.scale(self.image_hard2_origine, (50, 45))
                self.screen.blit(self.image_hard, (700, 500))



        pygame.display.flip()

    def draw_bird(self,image,angle,x,y):
        rotated = pygame.transform.rotate(image, angle)
        self.screen.blit(rotated, (x, y))

