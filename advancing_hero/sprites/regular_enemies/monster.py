import os
from .monster_attack import MonsterAttack
import pygame
import math
from .regular_enemy import RegularEnemy


class Monster(RegularEnemy):
    """
    Represents a Monster
    """

    def __init__(
            self,
            position,
            screen,
            max_health: float = 100,
            path: str = 'advancing_hero/images/sprites/regular_enemies/monster/',
    ) -> None:
        super().__init__(path=os.path.abspath(path),
                         position=position,
                         screen=screen,
                         max_health=max_health)
        self.attack_framerate = 180
        self.damage = 10

    def update(self, player, stage):
        super().update()
        if self.current_health <= 0 or self.rect.colliderect(
                self.screen.get_rect()) == 0:
            self.kill()
        self.rect.y += 1
        if self.frame_counter % self.animation_framerate == 0:
            temp_rect = self.rect
            self.image_frame = (self.image_frame + 1) % (len(self.image_list) -
                                                         1)
            self.image = self.image_list[self.image_frame]
            self.rect = self.image.get_rect()
            self.rect.centerx = temp_rect.centerx
            self.rect.centery = temp_rect.centery

        self.health_bar.update()
        self.player_collision(player)

        if (self.frame_counter + 12) % self.attack_framerate == 0:
            self.image = self.image_list[-1]

        if self.frame_counter % self.attack_framerate == 0:
            self.image = self.image_list[-1]
            delta_x = player.rect.centerx - self.rect.centerx
            delta_y = player.rect.centery - self.rect.centery
            direction_angle = -math.atan2(delta_y, delta_x)
            direction = pygame.math.Vector2.normalize(pygame.Vector2((delta_x, delta_y)))
            position = [self.rect.centerx, self.rect.centery]
            new_projectile = MonsterAttack(position, direction_angle, direction,
                                           (player.rect.centerx, player.rect.centery), self.screen)
            if self.alive():
                self.groups()[0].add(new_projectile)

