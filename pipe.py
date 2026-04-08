import pygame
from utils import resource_path

# Chargé UNE seule fois au démarrage
_pipe_top = None
_pipe_bottom = None
_mask_top = None
_mask_bottom = None

def _load_pipe_assets(width, height):
    global _pipe_top, _pipe_bottom, _mask_top, _mask_bottom
    if _pipe_top is None:
        img = pygame.image.load(resource_path('assets/images/pipe.png'))
        img = pygame.transform.scale(img, (width, height))
        _pipe_bottom = img
        _pipe_top = pygame.transform.rotate(img, 180)
        _mask_bottom = pygame.mask.from_surface(_pipe_bottom)
        _mask_top = pygame.mask.from_surface(_pipe_top)

class Pipe:
    def __init__(self, x, y, width, height, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.passed = False

        _load_pipe_assets(width, height)

        if direction == 180:
            self.image = _pipe_top
            self.mask = _mask_top
        else:
            self.image = _pipe_bottom
            self.mask = _mask_bottom

    def update(self, speed):
        self.x -= speed