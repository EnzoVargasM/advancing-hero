import os
from .sprite import Sprite
import math
import pygame


class BatAttack(Sprite):
    """
    Represents a bat
    """
    def __init__(
        self,
        position,
        direction_angle,
        direction,
        max_health: float = 100,
        path: str = 'advancing_hero/images/sprites/bat_attack/',
    ) -> None:
        super().__init__(path=os.path.abspath(path),
                         position=position,
                         max_health=max_health)
        self.direction = direction
        self.angle = direction_angle - math.pi / 2
        self.image = pygame.transform.rotate(self.image,
                                             180 * self.angle / math.pi)
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.speed = 5
        self.position = position
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.damage = 7
        self.music_path = os.path.abspath(
            'advancing_hero/songs/bat_attack.wav')

    def update(self, player, stage):
        super().update()
        self.position[0] += self.speed * self.direction.x
        self.position[1] += self.speed * self.direction.y
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        self.player_collision(player)
        for tile in stage.tile_list:
            if tile[1].bottom > 0 and tile[
                    1].top < stage.settings.screen_height and tile[2].is_solid:
                if tile[1].colliderect(self.rect):
                    self.kill()

    def player_collision(self, player):
        if self.rect.colliderect(player.rect):
            player.hurt(self.damage)
            self.play_music()
            self.kill()

    def play_music(self):
        sound = pygame.mixer.Sound(self.music_path)
        pygame.mixer.Channel(3).play(sound)
