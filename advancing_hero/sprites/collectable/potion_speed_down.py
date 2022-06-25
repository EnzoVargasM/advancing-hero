import os
from ..sprite import Sprite
import pygame


class PotionSpeedDown(Sprite):
    """
    Represents a potion to heal the hero
    """
    def __init__(
        self,
        position,
        screen,
        path: str = 'advancing_hero/images/sprites/potions/potion_speed_down',
    ) -> None:
        super().__init__(path=os.path.abspath(path), position=position)

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.position = position
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.music_path = os.path.abspath('advancing_hero/songs/item.wav')
        self.screen = screen
        self.caught = False
        self.buff_duration = 0

    def update(self, player, stage):
        super().update()
        if self.caught:
            if self.buff_duration > 0:
                self.buff_duration -= 1
            else:
                player.speed_base = player.hero_base_speed
                self.kill()
            return
        self.rect.y += stage.scroll_amount
        self.player_collision(player)
        if self.rect.colliderect(self.screen.get_rect()) == 0 and not self.caught:
            self.kill()

    def player_collision(self, player):
        if self.rect.colliderect(player.rect) and not self.caught:
            self.play_music()
            self.image.set_alpha(0)
            self.caught = True
            self.buff_duration = 300
            player.speed_base -= 5

    def play_music(self):
        sound = pygame.mixer.Sound(self.music_path)
        sound.set_volume(0.4)
        pygame.mixer.Channel(7).play(sound)
