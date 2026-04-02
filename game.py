import pygame
import random

from bird import Bird
from pipe import Pipe
from cloud import Cloud

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.clock = pygame.time.Clock()

        #Gestion joueur
        self.bird_co = (0, 0)
        self.bird = Bird(self.bird_co)

        #Gestion tuyau
        self.pipe_contener = []
        self.pipe_timer = 0
        self.pipe_interval = 90

        #Gestion des nuages
        self.cloud_contener = []
        self.cloud_timer = 0


        #Gestion jeu
        self.gravity = 0.5
        self.speed = 5


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.bird.move()

            self.update()
            self.clock.tick(60)

        pygame.quit()

    def update(self):
        self.screen.fill((144, 213, 255))

        self.update_cloud()

        #Joueur
        self.update_joueur()

        # Tuyaux
        self.update_pipes()

        self.collision()


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

            print(pipe_y+350)


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
            if self.bird.mask.overlap(pipe.mask, offset):
                print('Touche')