import os
import pygame
from os import walk


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.import_assts()
        self.frame_index = 0
        self.status = "up"
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)

        # float Based movment
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direcetion = pygame.math.Vector2()
        self.speed = 200

    def import_assts(self):
        base_path = "assets/player"
        self.animations = {}
        for folder_path, _, file_names in walk(base_path):
            if folder_path == base_path:
                continue

            key = os.path.basename(folder_path)
            self.animations[key] = []

            for file_name in sorted(
                file_names, key=lambda name: int(os.path.splitext(name)[0])
            ):
                file_path = os.path.join(folder_path, file_name)
                surf = pygame.image.load(file_path).convert_alpha()
                self.animations[key].append(surf)

    def animate(self, dt):
        current_animation = self.animations[self.status]

        if self.direcetion.magnitude() != 0:
            self.frame_index += 8 * dt
            if self.frame_index >= len(current_animation):
                self.frame_index = 0
        else:
            self.frame_index = 0
        self.image = self.image = current_animation[int(self.frame_index)]

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
            self.status = "up"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direcetion.y = 1
            self.status = "down"
        else:
            self.direcetion.y = 0

        # Movement on Horizontal
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direcetion.x = 1
            self.status = "right"
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direcetion.x = -1
            self.status = "left"
        else:
            self.direcetion.x = 0

    def update(self, keys, dt):
        self.input(keys)
        self.move(dt)
        self.animate(dt)
