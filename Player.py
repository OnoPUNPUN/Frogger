import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((50, 50))
        self.image.fill("red")
        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)

    def input(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            print("Up")
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            print("Down")
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            print("Right")
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            print("Left")

    def update(self, keys):
        self.input(keys)
