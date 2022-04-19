import cmath
import os
from .. sprite import Sprite
import pygame
import math


class EnergyBall(Sprite):
    """
    Represents a sprite test
    """
    def __init__(
        self,
        position,
        settings,
        player,
        phase: float = 0.0,
        path: str = 'advancing_hero/images/sprites/hero_weapons/energy_ball/',
    ) -> None:
        super().__init__(path=os.path.abspath(path), position=position)
        self.settings = settings
        self.phase = phase
        self.player = player
        self.image = pygame.transform.scale2x(
            self.image_list[self.image_frame])
        self.animation_framerate = 10
        self.rect = self.image.get_rect()
        self.damage = 1

        self.radius = 200
        self.angle = phase
        self.feq_x = 1
        self.feq_y = 1

        self.ang_vel = 1

        self.origin = pygame.Vector2((self.player.rect.centerx, self.player.rect.centery))
        self.true_position = self.origin + pygame.Vector2((
            self.radius * math.cos(self.feq_x * self.angle * math.pi / 180),
            self.radius * math.sin(self.feq_y * self.angle * math.pi / 180)))

    def update(self, stage):
        super().update()
        self.hurt_enemies(stage)

        self.angle += self.ang_vel

        self.origin = pygame.Vector2((self.player.rect.centerx, self.player.rect.centery))
        self.true_position = self.origin + pygame.Vector2((
            self.radius * math.cos(self.feq_x * self.angle * math.pi / 180),
            self.radius * math.sin(self.feq_y * self.angle * math.pi / 180)))
        self.rect.centerx = int(self.true_position.x)
        self.rect.centery = int(self.true_position.y)


    def hurt_enemies(self, stage):
        for enemy in stage.all_enemies.sprites():
            if self.rect.colliderect(enemy.rect):
                enemy.hurt(self.damage)
