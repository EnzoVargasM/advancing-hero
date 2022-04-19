import os
from ..sprite import Sprite
import pygame


class FireBlast(Sprite):
    """
    Represents a Fire_Blast
    """

    def __init__(
            self,
            position,
            initial_direction,
            settings,
            path: str = 'advancing_hero/images/sprites/hero_weapons/heal_blast/',
    ) -> None:
        super().__init__(path=os.path.abspath(path), position=position)
        self.settings = settings
        temp_rect = self.rect
        self.image = pygame.transform.scale(self.image_list[self.image_frame], (70,70))
        self.animation_framerate = 10
        speed = 10
        if initial_direction == 1:
            self.speed = pygame.Vector2((0, -speed))
        elif initial_direction == 2:
            self.speed = pygame.Vector2((-speed, 0))
            self.image = pygame.transform.rotate(self.image, 90)
        elif initial_direction == 3:
            self.speed = pygame.Vector2((0, speed))
            self.image = pygame.transform.rotate(self.image, 180)
        else:
            self.speed = pygame.Vector2((speed, 0))
            self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.x = temp_rect.x
        self.rect.y = temp_rect.y
        self.damage = 25

    def update(self, stage, player1):
        super().update()
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

        self.hurt_enemies(stage, player1)

        if not self.rect.colliderect(pygame.Rect(0, 0, self.settings.screen_width,
                                                 self.settings.screen_height)):
            self.kill()

    def hurt_enemies(self, stage, player1):
        #for tile in stage.tile_list:
        #    if tile[1].bottom > 0 and tile[1].top < self.settings.screen_height and tile[2].is_solid:
        #        if tile[1].colliderect(self.rect):
        #            self.kill()
        if self.rect.colliderect(player1.rect):
            player1.heal(10)
            #self.play_music()
            self.kill()
