import os
from ..sprite import Sprite
import pygame


class RegularBlast(Sprite):
    """
    Represents a Blast
    """

    def __init__(
            self,
            position,
            initial_direction,
            settings,
            charging_quantity,
            path: str = 'advancing_hero/images/sprites/hero_weapons/regular_blast/',
    ) -> None:
        super().__init__(path=os.path.abspath(path), position=position)
        self.settings = settings

        self.charging_quantity = charging_quantity

        self.temp_rect = self.rect
        self.blast_lenght = 30 + self.charging_quantity
        self.image = pygame.transform.scale(self.image_list[self.image_frame], (self.blast_lenght, self.blast_lenght))
        self.animation_framerate = 10
        self.speed_abs = 8 + self.charging_quantity*8/200
        self.initial_direction = initial_direction
        if initial_direction == 1:
            self.speed = pygame.Vector2((0, -self.speed_abs))
        elif initial_direction == 2:
            self.speed = pygame.Vector2((-self.speed_abs, 0))
            self.image = pygame.transform.rotate(self.image, 90)
        elif initial_direction == 3:
            self.speed = pygame.Vector2((0, self.speed_abs))
            self.image = pygame.transform.rotate(self.image, 180)
        else:
            self.speed = pygame.Vector2((self.speed_abs, 0))
            self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.x = self.temp_rect.x - self.blast_lenght/3
        self.rect.y = self.temp_rect.y - self.blast_lenght/3
        self.damage = self.charging_quantity * 2

    def update(self, stage):
        super().update()
        if self.frame_counter % 10 == 0:
            self.image_frame = (self.image_frame + 3) % len(self.image_list)
            self.image = pygame.transform.scale(self.image_list[self.image_frame], (self.blast_lenght, self.blast_lenght))
            if self.initial_direction == 1:
                self.speed = pygame.Vector2((0, -self.speed_abs))
            elif self.initial_direction == 2:
                self.speed = pygame.Vector2((-self.speed_abs, 0))
                self.image = pygame.transform.rotate(self.image, 90)
            elif self.initial_direction == 3:
                self.speed = pygame.Vector2((0, self.speed_abs))
                self.image = pygame.transform.rotate(self.image, 180)
            else:
                self.speed = pygame.Vector2((self.speed_abs, 0))
                self.image = pygame.transform.rotate(self.image, 270)

        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

        self.hurt_enemies(stage)
        if not self.rect.colliderect(pygame.Rect(0, 0, self.settings.screen_width,
                                                 self.settings.screen_height)):
            self.kill()

    def hurt_enemies(self, stage):
        for enemy in stage.all_enemies.sprites():
            if self.rect.colliderect(enemy.rect):
                hit = enemy.hurt(self.damage)  # Interactable enemies must return true
                # That is done so the projectiles don't interact with the player's attacks
                if hit:
                    self.kill()
