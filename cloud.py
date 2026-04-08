import pygame
from utils import resource_path

_cloud_cache = {}


class Cloud:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y

        if width not in _cloud_cache:
            img = pygame.image.load(resource_path('assets/images/cloud.png'))
            _cloud_cache[width] = pygame.transform.scale(img, (width, height))

        self.image = _cloud_cache[width]

    def update(self, speed):
        self.x -= speed