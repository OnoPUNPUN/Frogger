import pygame, sys
from Player import *
from settings import *

# Setup
pygame.init()
display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

# Player
all_sprites = pygame.sprite.Group()
player = Player((WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), all_sprites)

# Game Loop
while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick() / 1000

    keys = pygame.key.get_pressed()

    # Update time
    all_sprites.update(keys, dt)

    # Delta Time
    dt = clock.tick() / 1000
    display_surf.fill("black")
    # Updates
    all_sprites.draw(display_surf)

    pygame.display.update()
