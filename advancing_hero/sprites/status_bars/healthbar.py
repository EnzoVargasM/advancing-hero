import os
from ..sprite import Sprite
import pygame


class HealthBar(Sprite):
    """
    Represents a generic health bar
    """
    def __init__(
        self,
        offset,
        parent_sprite,
        screen,
        position='Monster',
        path: str = 'advancing_hero/images/sprites/status_bars/healthbar/',
    ) -> None:
        super().__init__(path=os.path.abspath(path), position=(0, 0))
        if position == 'Monster':
            self.initial_width = parent_sprite.rect.width
            self.height = 10
        elif position == 'Left-Top':
            self.initial_width = 300
            self.height = 30
        elif position == 'Right-Top':
            self.initial_width = 300
            self.height = 30
        self.image = pygame.transform.scale(self.image, (self.initial_width, self.height))
        if position == 'Monster':
            self.image = pygame.transform.scale(
                pygame.image.load(
                    os.path.abspath('advancing_hero/images/sprites/status_bars/healthbar/healthbar_enemies.png')),
                (self.initial_width, self.height))
        self.rect = self.image.get_rect()
        self.parent_sprite = parent_sprite
        self.offset = offset
        self.rect.x = self.parent_sprite.rect.x+self.offset[0]
        self.rect.y = self.parent_sprite.rect.y+self.offset[1]
        self.screen = screen
        self.position = position

    def update(self):
        super().update()
        current_health = self.parent_sprite.current_health
        max_health = self.parent_sprite.max_health
        self.rect.centerx = self.parent_sprite.rect.centerx - self.offset[0]
        self.rect.centery = self.parent_sprite.rect.centery + self.offset[1]

        if self.position == 'Monster':
            self.screen.blit(self.image, (self.rect.x, self.rect.y),
                             (0, 0, (round(self.initial_width * current_health / max_health)), self.height))
        elif self.position == 'Left-Top':
            self.screen.blit(self.image, (0, 0),
                             (0, 0, (round(self.initial_width * current_health / max_health)), self.height))
        elif self.position == 'Right-Top':
            self.screen.blit(self.image, (self.parent_sprite.settings.screen_width - 300, 0),
                             (0, 0, (round(self.initial_width * current_health / max_health)), self.height))
