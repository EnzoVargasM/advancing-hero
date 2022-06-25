import os
import random

from ..sprite import Sprite
from ..status_bars.healthbar import HealthBar
from ..collectable.potion_heal import PotionHeal
from ..collectable.potion_speed import PotionSpeed
from ..collectable.potion_speed_down import PotionSpeedDown
from ..collectable.potion_small import PotionSmall

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

    def spawn_random_potion(self):
        rng = random.randint(1, 100)
        rng_type = random.randint(1, 10)

        if 1 <= rng <= 20:
            if 1 <= rng_type <= 5:
                new_projectile = PotionHeal((self.rect.x, self.rect.y), self.screen)
            elif 6 <= rng_type <= 7:
                new_projectile = PotionSpeed((self.rect.x, self.rect.y), self.screen)
            elif 8 <= rng_type <= 8:
                new_projectile = PotionSpeedDown((self.rect.x, self.rect.y), self.screen)
            elif 9 <= rng_type <= 10:
                new_projectile = PotionSmall((self.rect.x, self.rect.y), self.screen)
            if self.alive():
                self.groups()[0].add(new_projectile)

