import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((50, 50))
        self.image.fill("red")
        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)

        # float Based movment
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direcetion = pygame.math.Vector2()
        self.speed = 200

    def move(self, dt):
        # Normalize a vector -> the length of a vector is going to be 1
        if self.direcetion.magnitude() != 0:
            self.direcetion = self.direcetion.normalize()
        self.pos += self.direcetion * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def input(self, keys):
        # Movement on The Vertical
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direcetion.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direcetion.y = 1
        else:
            self.direcetion.y = 0

        # Movement on Horizontal
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direcetion.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direcetion.x = -1
        else:
            self.direcetion.x = 0

    def update(self, keys, dt):
        self.input(keys)
        self.move(dt)
