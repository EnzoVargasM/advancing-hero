import os
from .regular_enemy import RegularEnemy
from .bat_attack import BatAttack
import pygame
import math


class Chaser(RegularEnemy):
    """
    Represents a bat
    """
    def __init__(
        self,
        position,
        screen,
        max_health: float = 100,
        path: str = 'advancing_hero/images/sprites/regular_enemies/chaser/',
    ) -> None:
        super().__init__(path=os.path.abspath(path),
                         position=position,
                         screen=screen,
                         max_health=max_health)
        self.xpos = position[0]
        self.ypos = position[1]
        self.speed = 2

    def update(self, player, stage):
        super().update()

        self.rect.centerx = int(self.xpos)
        self.rect.centery = int(self.ypos)

        if self.current_health <= 0 or self.rect.colliderect(
                self.screen.get_rect()) == 0:
            self.spawn_random_potion()
            self.kill()

        if self.frame_counter % self.animation_framerate == 0:
            temp_rect = self.rect
            self.image_frame = (self.image_frame + 1) % len(self.image_list)
            self.image = self.image_list[self.image_frame]
            self.rect = self.image.get_rect()
            self.rect.centerx = temp_rect.centerx
            self.rect.centery = temp_rect.centery

        self.health_bar.update()
        self.player_collision(player)

        delta_x = player.rect.centerx - self.rect.centerx
        delta_y = player.rect.centery - self.rect.centery
        dir_tmp = pygame.Vector2((delta_x, delta_y))
        if dir_tmp.magnitude() == 0:
            return
        direction = pygame.math.Vector2.normalize(dir_tmp)
        self.xpos += direction.x * self.speed
        self.ypos += direction.y * self.speed

