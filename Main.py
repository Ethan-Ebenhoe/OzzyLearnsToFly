import pygame
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF, pygame.HWSURFACE)
pygame.display.set_caption("Ozzy Learns To Fly")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()