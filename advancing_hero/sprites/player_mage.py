import os
import math
from . import Player
from .hero_weapons.mega_blast import MegaBlast
from .hero_weapons.regular_blast import RegularBlast
import pygame

weapons = {'regular_blast': RegularBlast, 'mega_blast': MegaBlast}


class PlayerMage(Player):

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
            path=os.path.abspath('advancing_hero/images/sprites/player_mage/'),
            max_health=100,
        )
        self.special_attack_cooldown = 0
        self.current_weapon = 'regular_blast'
        self.time_charging = -15
        # Cooldowns unique to this hero
        self.attack_cooldown_heal = 0
        self.attack_cooldown_mega = 0
        self.speed_buff_cooldown = 0
        # Last cooldowns applied to keep track of recharge
        self.last_attack_cooldown = -1
        self.last_attack_cooldown_heal = -1
        self.last_attack_cooldown_mega = -1

        self.cooldown_img = pygame.transform.scale2x(pygame.image.load(
            os.path.abspath('advancing_hero/images/sprites/hero_weapons/weapon_slot/weapon_cooldown_shadow.png')
        ))

        self.star_fx = pygame.image.load(
            os.path.abspath('advancing_hero/images/sprites/effects/star_fx.png')
        )

    def handle_weapon(self):

        key = pygame.key.get_pressed()
        if key[pygame.K_c]:
            if self.current_weapon == 'regular_blast' and self.attack_cooldown == 0 and len(
                    self.projectiles.sprites()) < 2:
                if self.time_charging > 60:
                    if self.time_charging > 120:
                        if self.time_charging >= 150:
                            pass
                        else:
                            if self.frame_counter % 15 == 0:
                                self.time_charging += 1
                    else:
                        if self.frame_counter % 5 == 0:
                            self.time_charging += 1
                else:
                    self.time_charging += 1
                print(self.time_charging)
                tmp = self.time_charging
                if tmp < 0:
                    tmp = 0
                star_new_img = pygame.transform.scale(self.star_fx, (17 * (tmp / 25), 17 * (tmp / 25)))
                self.screen.blit(star_new_img,
                                 (self.rect.x + self.rect.width / 2 - round(9 * (tmp / 25)), self.rect.y - 18))

            if self.current_weapon == 'mega_blast' and self.attack_cooldown_mega == 0 and len(
                    self.projectiles.sprites()) < 2:
                if self.time_charging > 60:
                    if self.time_charging > 120:
                        if self.frame_counter % 15 == 0:
                            self.time_charging += 1
                    else:
                        if self.frame_counter % 5 == 0:
                            self.time_charging += 1
                else:
                    self.time_charging += 1
                print(self.time_charging)
                tmp = self.time_charging
                if tmp < 0:
                    tmp = 0
                star_new_img = pygame.transform.scale(self.star_fx, (17 * (tmp / 25), 17 * (tmp / 25)))
                self.screen.blit(star_new_img,
                                 (self.rect.x + self.rect.width / 2 - round(9 * (tmp / 25)), self.rect.y - 18))

            if self.current_weapon == 'heal' and self.attack_cooldown_heal == 0:
                if self.time_charging > 60:
                    if self.time_charging > 120:
                        if self.frame_counter % 15 == 0:
                            self.time_charging += 1
                    else:
                        if self.frame_counter % 5 == 0:
                            self.time_charging += 1
                else:
                    self.time_charging += 1
                print(self.time_charging)
                tmp = self.time_charging
                if tmp < 0:
                    tmp = 0
                star_new_img = pygame.transform.scale(self.star_fx, (17 * (tmp / 25), 17 * (tmp / 25)))
                self.screen.blit(star_new_img,
                                 (self.rect.x + self.rect.width / 2 - round(9 * (tmp / 25)), self.rect.y - 18))

        if not key[pygame.K_c] and self.time_charging > 0:
            if self.current_weapon == 'regular_blast':
                self.attack_cooldown += self.time_charging
                self.last_attack_cooldown = self.time_charging
                self.weapon = weapons[self.current_weapon]((self.rect.centerx, self.rect.centery),
                                                           self.moving_direction, self.settings, self.time_charging)
                self.projectiles.add(self.weapon)
                # Play SFX
                sfx = os.path.abspath('advancing_hero/songs/blast.mp3')
                sound = pygame.mixer.Sound(sfx)
                sound.set_volume(0.5)
                pygame.mixer.Channel(8).play(sound)

            elif self.current_weapon == 'mega_blast':
                self.attack_cooldown_mega += self.time_charging * 4
                self.last_attack_cooldown_mega = self.time_charging * 4
                self.weapon = weapons[self.current_weapon]((self.rect.centerx, self.rect.centery),
                                                           self.moving_direction, self.settings, self.time_charging)
                self.projectiles.add(self.weapon)
                # Play SFX
                sfx = os.path.abspath('advancing_hero/songs/mega_blast.wav')
                sound = pygame.mixer.Sound(sfx)
                sound.set_volume(0.5)
                pygame.mixer.Channel(8).play(sound)

            elif self.current_weapon == 'heal':
                self.attack_cooldown_heal += self.time_charging * 5
                self.last_attack_cooldown_heal = self.time_charging * 5
                # Buffs
                self.heal(self.time_charging / 10)
                self.speed_base += self.time_charging / 10
                self.speed_buff_cooldown = 60
                print(self.time_charging / 10)

                # Play SFX
                sfx = os.path.abspath('advancing_hero/songs/heal.mp3')
                sound = pygame.mixer.Sound(sfx)
                sound.set_volume(1)
                pygame.mixer.Channel(8).play(sound)

            self.time_charging = -15
        if key[pygame.K_v] and self.changing_weapon_cooldown == 0:
            if self.current_weapon == 'regular_blast':
                self.current_weapon = 'mega_blast'
            elif self.current_weapon == 'mega_blast':
                self.current_weapon = 'heal'
            elif self.current_weapon == 'heal':
                self.current_weapon = 'regular_blast'
            self.changing_weapon_cooldown += 15

    def update_cooldown(self):
        if self.changing_weapon_cooldown > 0:
            self.changing_weapon_cooldown -= 1
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.attack_cooldown_heal > 0:
            self.attack_cooldown_heal -= 1
        if self.attack_cooldown_mega > 0:
            self.attack_cooldown_mega -= 1
        if self.speed_buff_cooldown > 0:
            self.speed_buff_cooldown -= 1
        if self.speed_buff_cooldown == 1:
            self.speed_base = self.hero_base_speed

        if self.current_weapon == 'regular_blast':

            ratio = self.attack_cooldown / self.last_attack_cooldown
            self.screen.blit(self.cooldown_img, (8, 70 + round(40 * (1 - ratio))),
                             (0, 0, 43, (round(40 * ratio))))
        elif self.current_weapon == 'heal':
            ratio = self.attack_cooldown_heal / self.last_attack_cooldown_heal
            self.screen.blit(self.cooldown_img, (8, 70 + round(40 * (1 - ratio))),
                             (0, 0, 43, (round(40 * ratio))))
        elif self.current_weapon == 'mega_blast':
            ratio = self.attack_cooldown_mega / self.last_attack_cooldown_mega
            self.screen.blit(self.cooldown_img, (8, 70 + round(40 * (1 - ratio))),
                             (0, 0, 43, (round(40 * ratio))))

    def handle_movement(self):
        dx = 0
        dy = 0
        moving_flag = False  # Handles multiple key presses
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.walk_animation(7, 1)
            moving_flag = True
            dy -= 1
        if key[pygame.K_a]:
            if not moving_flag:
                self.walk_animation(4, 2)
            moving_flag = True
            dx -= 1
        if key[pygame.K_d]:
            if not moving_flag:
                self.walk_animation(4, 4, flip=True)
            dx += 1
            moving_flag = True
        if key[pygame.K_s]:
            if not moving_flag:
                self.walk_animation(1, 3)
            dy += 1

        if dx == 0 and dy == 0:
            self.walking_framerate = 0
            # If we were walking and stopped, keep looking to
            # the direction we were looking before
            if self.moving_direction == 1:
                self.image_frame = 7
                self.update_rect()
            if self.moving_direction == 2:
                self.image_frame = 4
                self.update_rect()
            if self.moving_direction == 3:
                self.image_frame = 1
                self.update_rect()
            if self.moving_direction == 4:
                self.image_frame = 4
                self.update_rect(flip=True)

        for tile in self.stage.tile_list:
            # Check only blocks which are on screen and are interactable
            if tile[1].bottom > 0 and tile[
                1].top < self.settings.screen_height and tile[
                2].is_interactable:

                # First run block interaction code. The collision is checked with
                # the player's standing point
                if tile[1].colliderect(self.rect.x,
                                       self.rect.y + 3 * self.rect.height / 4,
                                       self.rect.width, self.rect.height / 4):
                    tile[2].player_interaction(self)

                # Then check if it's solid. We do it on that order in case
                # the block changes the player's speed.
                if tile[2].is_solid and (dx or dy):
                    # Check collision in x direction
                    delta_x = self.speed * dx / math.sqrt(dx * dx + dy * dy)
                    delta_y = self.speed * dy / math.sqrt(dx * dx + dy * dy)
                    if tile[1].colliderect(self.rect.x + delta_x, self.rect.y,
                                           self.rect.width, self.rect.height):
                        dx = 0
                    # Check for collision in y direction
                    if tile[1].colliderect(self.rect.x, self.rect.y + delta_y,
                                           self.rect.width, self.rect.height):
                        dy = 0

        if dx or dy:
            self.rect.x += self.speed * dx / math.sqrt(dx * dx + dy * dy)
            self.rect.y += self.speed * dy / math.sqrt(dx * dx + dy * dy)

        if self.rect.bottom > self.settings.screen_height:
            self.rect.bottom = self.settings.screen_height
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > self.settings.screen_width:
            self.rect.right = self.settings.screen_width
        if self.rect.left < 0:
            self.rect.left = 0

