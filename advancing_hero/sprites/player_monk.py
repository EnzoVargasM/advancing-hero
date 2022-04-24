import os
from . import Player
from .hero_weapons.energy_ball import EnergyBall
import pygame
from .. import settings


class PlayerMonk(Player):

    def __init__(
            self,
            position,
            settings,
            stage,
            screen,
    ) -> None:
        super().__init__(
            position=position,
            settings=settings,
            stage=stage,
            screen=screen,
            path=os.path.abspath('advancing_hero/images/sprites/player_monk/'),
            max_health=100,
        )
        self.energy_ball_1 = EnergyBall(position, settings, self, 0)
        self.energy_ball_2 = EnergyBall(position, settings, self, 180)
        self.projectiles.add(self.energy_ball_1)
        self.projectiles.add(self.energy_ball_2)
        self.special_attack_cooldown = 0
        self.current_weapon = 'circle_lissajous'
        self.hero_base_speed = settings.DEFAULT_PLAYER_SPEED * 3/2
        self.speed_base = self.hero_base_speed

    def handle_weapon(self):
        key = pygame.key.get_pressed()
        self.special_attack_cooldown = max(0, self.special_attack_cooldown - 1)

        if self.special_attack_cooldown == 1:
            self.speed_base = self.hero_base_speed
            self.current_weapon = 'circle_lissajous'
            self.energy_ball_1.feq_x = 1
            self.energy_ball_1.feq_y = 1
            self.energy_ball_2.feq_x = 1
            self.energy_ball_2.feq_y = 1
            self.energy_ball_1.damage = 2
            self.energy_ball_2.damage = 2
            self.energy_ball_1.ang_vel = 1
            self.energy_ball_2.ang_vel = 1

        if key[pygame.K_v] and self.changing_weapon_cooldown == 0:
            if self.current_weapon == 'circle_lissajous':
                self.current_weapon = 'infinity_lissajous'
                self.energy_ball_1.feq_x = 1
                self.energy_ball_1.feq_y = 2
                self.energy_ball_2.feq_x = 1
                self.energy_ball_2.feq_y = 2
                self.energy_ball_1.damage = 2
                self.energy_ball_2.damage = 2
                self.energy_ball_1.ang_vel = 1
                self.energy_ball_2.ang_vel = 1
                self.changing_weapon_cooldown += 15
            elif self.current_weapon == 'infinity_lissajous':
                self.current_weapon = 'circle_lissajous'
                self.energy_ball_1.feq_x = 1
                self.energy_ball_1.feq_y = 1
                self.energy_ball_2.feq_x = 1
                self.energy_ball_2.feq_y = 1
                self.energy_ball_1.damage = 2
                self.energy_ball_2.damage = 2
                self.energy_ball_1.ang_vel = 1
                self.energy_ball_2.ang_vel = 1
                self.changing_weapon_cooldown += 15
        if key[pygame.K_c] and self.changing_weapon_cooldown == 0 and self.special_attack_cooldown == 0:
            self.speed_base = self.hero_base_speed / 6  # Slowest velocity possible 1px
            self.current_weapon = 'powerful_lissajous'
            self.changing_weapon_cooldown += 300
            self.special_attack_cooldown += 300
            self.energy_ball_1.feq_x = 3
            self.energy_ball_1.feq_y = 2
            self.energy_ball_2.feq_x = 3
            self.energy_ball_2.feq_y = 2
            self.energy_ball_1.damage = 10
            self.energy_ball_2.damage = 10
            self.energy_ball_1.ang_vel = 5
            self.energy_ball_2.ang_vel = 5

