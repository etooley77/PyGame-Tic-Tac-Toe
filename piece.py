import pygame

from constants import *

class Piece(pygame.sprite.Sprite):
    def __init__(self, color, pos):
        super().__init__()

        # Create surface object
        self.surface = pygame.Surface((piece_width, piece_width), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, color, ((piece_width / 2), (piece_width / 2)), (piece_width / 2))
        self.rect = self.surface.get_rect(center = pos)