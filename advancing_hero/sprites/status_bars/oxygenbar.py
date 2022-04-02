import os
from ..sprite import Sprite
import pygame


class OxygenBar(Sprite):
    """
    Represents a generic health bar
    """
    def __init__(
            self,
            parent_sprite,
            screen,
            position='L',
            path: str = 'advancing_hero/images/sprites/status_bars/oxygenbar/',
    ) -> None:
        super().__init__(path=os.path.abspath(path), position=(0, 0))
        self.initial_width = 300
        self.height = 15
        self.image = pygame.transform.scale(self.image, (self.initial_width, self.height))
        self.initial_image = pygame.transform.scale(self.image, (self.initial_width, self.height))
        self.rect = self.image.get_rect()
        self.parent_sprite = parent_sprite
        self.rect.x = 2
        self.rect.y = 0
        self.screen = screen
        self.position = position

    def update(self):
        super().update()
        current_oxygen = self.parent_sprite.current_oxygen
        max_oxygen = self.parent_sprite.max_oxygen

        if self.position == 'L':
            self.screen.blit(self.image, (0, 30),
                             (0, 0, round(self.initial_width * current_oxygen / max_oxygen), self.height))
        else:
            self.screen.blit(self.image, (self.parent_sprite.settings.screen_width - 300, 30),
                             (0, 0,
                              round(self.initial_width * current_oxygen / max_oxygen), self.height))
