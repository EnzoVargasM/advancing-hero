import os
from ..sprite import Sprite
from ..status_bars.healthbar import HealthBar


class RegularEnemy(Sprite):
    """
    Represents a regular enemy
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
                         max_health=max_health)
        self.animation_framerate = 8
        self.attack_framerate = 90
        self.health_bar = HealthBar(screen=screen,
                                    parent_sprite=self,
                                    offset=(0, -32))
        self.screen = screen
        self.damage = 5

    def update(self, *args, **kwargs):
        super().update()
        pass

    def player_collision(self, player):
        if self.rect.colliderect(player.rect):
            player.hurt(self.damage)
            player.push()

    def hurt(self, damage):
        self.current_health = max(self.current_health - damage, 0)
        return True
