import pygame

import random

from bird import Bird
from pipe import Pipe
from cloud import Cloud

class Flappy():
    def __init__(self,screen,clock):
        self.screen = screen
        self.clock = clock

        # Gestion joueur
        self.bird_co = (0, 0)
        self.bird = Bird(self.bird_co)
        self.c_cooldown = 60

        # Gestion tuyau
        self.pipe_contener = []
        self.pipe_timer = 0
        self.pipe_interval = 90

        # Gestion des nuages
        self.cloud_contener = []
        self.cloud_timer = 0

        # Gestion de la vie
        self.health = 3
        self.health_image = pygame.image.load('assets/images/health.png')
        self.health_image = pygame.transform.scale(self.health_image, (50, 45))

        # Gestion jeu
        self.gravity = 0.5
        self.speed = 5
        self.game_over_image = pygame.image.load('assets/images/GameOver.png')
        self.game_over_image = pygame.transform.scale(self.game_over_image, (300, 150))
        self.frozen_screen = self.screen.copy()


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
            pipe.update(self.speed)
            self.screen.blit(pipe.image, (pipe.x, pipe.y))

        # Supprimer les tuyaux sortis de l'écran
        self.pipe_contener = [p for p in self.pipe_contener if p.x > -200]

    def update_cloud(self):
        interval = random.randint(90, 120)
        self.cloud_timer += 1
        if self.cloud_timer >= interval:
            y = random.randint(0, 250)
            width = random.randint(150, 200)
            height = random.randint(50, 100)
            self.cloud_timer = 0
            self.cloud_contener.append(Cloud(800,y,width,100))
            self.cloud_contener.append(Cloud(800,y,width,100))


        for cloud in self.cloud_contener:
            cloud.update(self.speed)
            self.screen.blit(cloud.image, (cloud.x, cloud.y))

        self.cloud_contener = [c for c in self.cloud_contener if c.x > -200]


    def collision(self):
        for pipe in self.pipe_contener:
            offset = (int(pipe.x - self.bird.x), int(pipe.y - self.bird.y))
            if self.bird.mask.overlap(pipe.mask, offset) and self.c_cooldown >= 60:
                self.health -= 1
                self.c_cooldown = 0
                if self.health == 0:
                    self.frozen_screen = self.screen.copy()

    def health_bar(self):
        for i in range (0,self.health):
            self.screen.blit(self.health_image,(625+i*55,20))


    def game_over(self):
        self.screen.blit(self.frozen_screen, (0, 0))
        self.screen.blit(self.game_over_image, (250, 200))