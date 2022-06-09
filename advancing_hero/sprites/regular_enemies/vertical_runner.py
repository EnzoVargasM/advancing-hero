import os
from .regular_enemy import RegularEnemy
from .bat_attack import BatAttack
import pygame
import math


class VerticalRunner(RegularEnemy):
    """
    Represents a vertical runner
    """
    def __init__(
        self,
        position,
        screen,
        max_health: float = 100,
        path: str = 'advancing_hero/images/sprites/regular_enemies/bat/',
    ) -> None:
        super().__init__(path=os.path.abspath(path),
                         position=position,
                         screen=screen,
                         max_health=max_health)

    def update(self, player, stage):
        super().update()
        if self.current_health <= 0 or self.rect.colliderect(
                self.screen.get_rect()) == 0:
            self.spawn_random_potion()
            self.kill()

        self.rect.y += 3

        if self.frame_counter % self.animation_framerate == 0:
            temp_rect = self.rect
            self.image_frame = (self.image_frame + 1) % len(self.image_list)
            self.image = self.image_list[self.image_frame]
            self.rect = self.image.get_rect()
            self.rect.centerx = temp_rect.centerx
            self.rect.centery = temp_rect.centery

        self.health_bar.update()
        self.player_collision(player)

