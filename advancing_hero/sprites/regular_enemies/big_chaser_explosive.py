import os
from .regular_enemy import RegularEnemy
from .bat_attack import BatAttack
import pygame
import math


class ChaserBigExplosive(RegularEnemy):
    """
    Represents a bat
    """
    def __init__(
        self,
        position,
        screen,
        max_health: float = 100,
        path: str = 'advancing_hero/images/sprites/regular_enemies/chaser_big_explosive/',
    ) -> None:
        super().__init__(path=os.path.abspath(path),
                         position=position,
                         screen=screen,
                         max_health=max_health)
        self.xpos = position[0]
        self.ypos = position[1]
        self.speed = 1
        self.music_path = os.path.abspath('advancing_hero/songs/explosion.wav')
        self.explosion_frame = len(self.image_list)-5
        self.explosion_duration = 10
        self.collide_player = False

    def update(self, player, stage):
        super().update()

        if self.collide_player:
            if self.explosion_frame == len(self.image_list):
                self.kill()
            elif self.explosion_frame % self.explosion_duration != 0:
                self.image = self.image_list[self.explosion_frame]
                self.explosion_frame += 1
            return

        self.rect.centerx = int(self.xpos)
        self.rect.centery = int(self.ypos)

        if self.current_health <= 0 or self.rect.colliderect(
                self.screen.get_rect()) == 0:
            self.spawn_random_potion()
            self.collide_player = True

        if self.frame_counter % self.animation_framerate == 0:
            temp_rect = self.rect
            self.image_frame = (self.image_frame + 1) % 1
            self.image = self.image_list[self.image_frame]
            self.rect = self.image.get_rect()
            self.rect.centerx = temp_rect.centerx
            self.rect.centery = temp_rect.centery

        self.health_bar.update()
        self.player_collision(player)

        delta_x = player.rect.centerx - self.rect.centerx
        delta_y = player.rect.centery - self.rect.centery
        direction = pygame.math.Vector2.normalize(pygame.Vector2((delta_x, delta_y)))
        self.xpos += direction.x * self.speed
        self.ypos += direction.y * self.speed

    def player_collision(self, player):
        if pygame.sprite.collide_mask(self, player) and not self.collide_player:
            self.collide_player = True
            self.play_music()
            self.image = self.image_list[-5]
            player.hurt(49)

    def hurt(self, damage):
        self.current_health = max(self.current_health - 1, 0)
        return True

    def play_music(self):
        sound = pygame.mixer.Sound(self.music_path)
        sound.set_volume(0.05)
        pygame.mixer.Channel(4).play(sound)
