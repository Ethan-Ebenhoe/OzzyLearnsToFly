import pygame
from Object import *
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF, pygame.HWSURFACE)
pygame.display.set_caption("Ozzy Learns To Fly")
object = Object(1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0xff, 0xff, 0xff))
    pygame.draw.rect(screen, (0xcf, 0xcf, 0xcf), pygame.Rect(50, 50, 100, 100), 100)
    object.show(screen)
    pygame.display.flip()
pygame.quit()