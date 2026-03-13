import pygame, sys
from settings import *

# Setup
pygame.init()
display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

# Game Loop
while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Delta Time
    dt = clock.tick() / 1000

    # Updates
    pygame.display.update()
