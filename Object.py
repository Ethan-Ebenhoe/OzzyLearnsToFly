import pygame

class Object:
    def __init__(self, vertices):
        self.vertices = vertices
    def show(self, surface):
        pygame.draw.polygon(surface, (0xff, 00, 00),self.vertices)