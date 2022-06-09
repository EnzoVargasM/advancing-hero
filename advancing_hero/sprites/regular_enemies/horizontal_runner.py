import os
import random

from .regular_enemy import RegularEnemy
from .bat_attack import BatAttack
import pygame
import math


class HorizontalRunner(RegularEnemy):
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
        self.side = random.randint(0, 1)
        self.activated = False
        if self.side == 0:
            correct_position = (-50, position[1])
        else:
            correct_position = (screen.get_width() + 50, position[1])

        super().__init__(path=os.path.abspath(path),
                         position=correct_position,
                         screen=screen,
                         max_health=max_health)

    def update(self, player, stage):
        super().update()
        if self.current_health <= 0 or (
                (self.side == 0 and self.rect.x >= self.screen.get_width()+50) or
                (self.side == 1 and self.rect.x <= -100)
        ):
            self.spawn_random_potion()
            self.kill()

        self.rect.y += 1

        if self.activated:
            if self.side == 0:
                self.rect.x += 3
            else:
                self.rect.x -= 3
        else:
            if abs(player.rect.y - self.rect.y) <= 10:
                self.activated = True

        if self.frame_counter % self.animation_framerate == 0:
            temp_rect = self.rect
            self.image_frame = (self.image_frame + 1) % len(self.image_list)
            self.image = self.image_list[self.image_frame]
            self.rect = self.image.get_rect()
            self.rect.centerx = temp_rect.centerx
            self.rect.centery = temp_rect.centery

        self.health_bar.update()
        self.player_collision(player)

