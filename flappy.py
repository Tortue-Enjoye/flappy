import pygame

import random
from collections import deque
from utils import resource_path


from bird import Bird
from pipe import Pipe
from cloud import Cloud
from scoreboard import Scoreboard

class Flappy():
    def __init__(self,screen,clock):
        self.screen = screen
        self.clock = clock

        # Gestion joueur
        self.bird_co = (100, 0)
        self.bird = Bird(self.bird_co)
        self.c_cooldown = 60

        # Gestion tuyau
        self.pipe_contener = []
        self.pipe_timer = 0
        self.pipe_interval = 90
        self.pipe_contener = deque()


        # Gestion des nuages
        self.cloud_contener = []
        self.cloud_timer = 0
        self.interval = random.randint(90, 120)
        self.cloud_contener = deque()

        # Gestion de la vie
        self.health = 3
        self.health_image = pygame.image.load(resource_path('assets/images/health.png'))
        self.health_image = pygame.transform.scale(self.health_image, (50, 45))

        # Gestion jeu
        self.gravity = 0.5
        self.speed = 5
        self.game_over_image = pygame.image.load(resource_path('assets/images/GameOver.png'))
        self.game_over_image = pygame.transform.scale(self.game_over_image, (300, 150))
        self.frozen_screen = None

        # Gestion du score
        self.score = 0
        self.score_font = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 48)
        self.scores = Scoreboard(self.screen,self.clock).load_scores()
        if self.scores == []:
            self.scores.append(0)

        self.score_font2 = pygame.font.Font(resource_path("assets/fonts/NotoEmoji-Bold.ttf"),32)
        self.text_c = self.score_font2.render("👑", True, (239, 191, 4))
        self._cached_score = -1
        self._cached_score_surface = None
        self._cached_best = -1
        self._cached_best_surface = None




    def update(self):
        self.screen.fill((144, 213, 255))
        if self.health > 0:
            self.update_cloud()

            #Joueur
            if self.c_cooldown >=60:
                self.update_joueur()
            else:
                if (self.c_cooldown // 5) % 2 == 0:  # clignote toutes les 5 frames
                    self.update_joueur()
                else:
                    self.bird.velocity += self.gravity
                    self.bird.update()

            # Tuyaux
            self.update_pipes()

            self.collision()

            self.health_bar()

            self.draw_score()



            self.c_cooldown += 1
        else:
            self.game_over()

        pygame.display.flip()

    def update_joueur(self):
        self.bird.velocity += self.gravity
        self.bird.update()
        self.screen.blit(self.bird.image, (self.bird.x, self.bird.y))

    def update_pipes(self):
        self.pipe_timer += 1
        if self.pipe_timer >= self.pipe_interval:
            self.pipe_timer = 0

            gap = 325
            pipe_y = random.randint(0, 250)

            self.pipe_contener.append(Pipe(800, pipe_y-gap, 75, 400,180))  # collé en haut
            self.pipe_contener.append(Pipe(800, pipe_y+gap, 75, 400,0))  # collé en bas

        for pipe in self.pipe_contener:
            if not pipe.passed and pipe.x + 75 < self.bird.x and pipe.direction == 0:
                pipe.passed = True
                self.score += 1

                if self.speed < 25 and self.score % 20 == 0:
                    self.speed += 1
                    self.pipe_interval = int(90 * (5 / self.speed))

            pipe.update(self.speed)
            self.screen.blit(pipe.image, (pipe.x, pipe.y))

        # Supprimer les tuyaux sortis de l'écran
        while self.pipe_contener and self.pipe_contener[0].x <= -200:
            self.pipe_contener.popleft()

    def update_cloud(self):
        self.cloud_timer += 1
        if self.cloud_timer >= self.interval:
            self.interval = random.randint(90, 120)
            y = random.randint(0, 250)
            width = random.randint(150, 200)
            self.cloud_timer = 0
            self.cloud_contener.append(Cloud(800,y,width,100))

        for cloud in self.cloud_contener:
            cloud.update(self.speed)
            self.screen.blit(cloud.image, (cloud.x, cloud.y))

        while self.cloud_contener and self.cloud_contener[0].x <= -200:
            self.cloud_contener.popleft()

    def collision(self):
        for pipe in self.pipe_contener:
            offset = (int(pipe.x - self.bird.x), int(pipe.y - self.bird.y))
            if self.bird.mask.overlap(pipe.mask, offset) and self.c_cooldown >= 60:
                self.health -= 1
                self.c_cooldown = 0
                if self.health == 0:
                    self.frozen_screen = self.screen.copy()
                    Scoreboard.save_score(self.score)

    def health_bar(self):
        for i in range (0,self.health):
            self.screen.blit(self.health_image,(625+i*55,20))


    def game_over(self):
        self.screen.blit(self.frozen_screen, (0, 0))
        self.screen.blit(self.game_over_image, (250, 200))

        text = self.score_font.render(f"Score : {self.score}", True, (255, 255, 255))
        self.screen.blit(text, (400 - text.get_width() // 2, 370))

    def draw_score(self):
        best = max(self.scores[0], self.score)

        # Score actuel
        if self.score != self._cached_score:
            self._cached_score = self.score
            self._cached_score_surface = self.score_font.render(str(self.score), True, (0, 76, 153))
        self.screen.blit(self._cached_score_surface, (50 - self._cached_score_surface.get_width() // 2, 30))

        # Meilleur score
        if best != self._cached_best:
            self._cached_best = best
            self._cached_best_surface = self.score_font.render(str(best), True, (239, 191, 4))
        self.screen.blit(self._cached_best_surface, (200 + self._cached_best_surface.get_width() // 2, 30))

        # Couronne
        self.screen.blit(self.text_c, (150 + self.text_c.get_width() // 2, 43))


    def reset(self):

        # Gestion joueur
        self.bird_co = (100, 0)
        self.bird = Bird(self.bird_co)
        self.c_cooldown = 60

        # Gestion tuyau
        self.pipe_contener = []
        self.pipe_timer = 0
        self.pipe_interval = 90
        self.pipe_contener = deque()

        # Gestion des nuages
        self.cloud_contener = []
        self.cloud_timer = 0
        self.interval = random.randint(90, 120)
        self.cloud_contener = deque()

        # Gestion de la vie
        self.health = 3
        self.health_image = pygame.image.load(resource_path('assets/images/health.png'))
        self.health_image = pygame.transform.scale(self.health_image, (50, 45))

        # Gestion jeu
        self.gravity = 0.5
        self.speed = 5
        self.game_over_image = pygame.image.load(resource_path('assets/images/GameOver.png'))
        self.game_over_image = pygame.transform.scale(self.game_over_image, (300, 150))
        self.frozen_screen = None

        # Gestion du score
        self.score = 0
        self.score_font = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Bold.ttf"), 48)
        self.scores = Scoreboard(self.screen, self.clock).load_scores()
        if self.scores == []:
            self.scores.append(0)

        self.score_font2 = pygame.font.Font(resource_path("assets/fonts/NotoEmoji-Bold.ttf"), 32)
        self.text_c = self.score_font2.render("👑", True, (239, 191, 4))
        self._cached_score = -1
        self._cached_score_surface = None
        self._cached_best = -1
        self._cached_best_surface = None

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.health > 0:
                        self.bird.move()
                    else:
                        return "menu"
                elif event.type == pygame.KEYDOWN: # Ajout de la touche espace pour les sauts
                    if event.key == pygame.K_SPACE:
                        if self.health > 0:
                            self.bird.move()
                        else:
                            return "menu"
                    if event.key == pygame.K_r:
                        self.reset()

            self.update()
            self.clock.tick(60)