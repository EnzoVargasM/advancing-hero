import os
from .sprite import Sprite
from .hero_weapons.boomerang import Boomerang
from .status_bars.healthbar import HealthBar
from .status_bars.oxygenbar import OxygenBar
from .hero_weapons.arrow import Arrow
import pygame
import math

#DOWN = 1
#SIDE = 4
#UP = 7

weapons = {'boomerang': Boomerang, 'arrow': Arrow}


class Player(Sprite):
    """
    Represents a sprite test
    """
    def __init__(
        self,
        position,
        settings,
        stage,
        screen,
        max_health: float = 100,
        max_oxygen: float = 100,
        path: str = 'advancing_hero/images/sprites/player/',
    ) -> None:
        super().__init__(
            path=os.path.abspath(path),
            position=position,
            max_health=max_health,
        )
        self.hero_base_speed = settings.DEFAULT_PLAYER_SPEED  # Standard speed for each type of hero
        self.speed_base = settings.DEFAULT_PLAYER_SPEED  # Base speed for modifying hero speed through buffs
        self.speed = self.speed_base  # Actual speed calculated after block interaction
        self.screen = screen
        self.settings = settings
        self.stage = stage
        self.image_frame = 1
        self.update_rect()
        self.walking_framerate = 0
        self.moving_direction = 3
        self.current_weapon = 'boomerang'
        self.weapon_slot = pygame.transform.scale(pygame.image.load(
            os.path.abspath('advancing_hero/images/sprites/hero_weapons/weapon_slot/weapon_slot.png')), (60, 60))
        self.weapon_or_ability_icon = pygame.transform.scale2x(pygame.image.load(
            os.path.abspath('advancing_hero/images/sprites/hero_weapons/boomerang/frame2.png')))
        self.changing_weapon_cooldown = 0
        self.weapon = weapons[self.current_weapon]
        self.attack_cooldown = 0
        self.projectiles = pygame.sprite.Group()
        self.timer_fast_player = 0
        self.health_bar = HealthBar(screen=screen,
                                    parent_sprite=self,
                                    offset=(0, -38),
                                    position='Left-Top')
        self.oxygen_bar = OxygenBar(
            screen=screen,
            parent_sprite=self,
        )
        self.max_oxygen = max_oxygen
        self.current_oxygen = max_oxygen
        self.have_oxygen = True
        self.in_water = False
        self.alive = True
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())
        self.invicibility_frames = 0
        self.regular_font = pygame.freetype.Font(os.path.abspath('advancing_hero/fonts/zerovelo.ttf'), 12)

    def update(self):
        super().update()
        self.check_oxygen()
        self.check_alive()
        self.in_water = False
        self.handle_movement()
        self.handle_breathing()
        self.handle_weapon()
        self.draw_slot_and_weapons()
        self.update_cooldown()
        self.projectiles.update(self.stage)
        self.projectiles.draw(self.screen)
        self.health_bar.update()
        self.oxygen_bar.update()
        if self.invicibility_frames > 0:
            self.invicibility_frames -= 1
        # Testing speed up effect (TSUE)
        #if self.timer_fast_player > 0:  # Potion heal speed up player test
        #    self.timer_fast_player -= 1
        #    if self.timer_fast_player == 0:
        #        self.speed_base = self.settings.DEFAULT_PLAYER_SPEED
        #        self.speed = self.speed_base

    def handle_breathing(self):
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
        if self.in_water:
            self.current_oxygen = max(self.current_oxygen - 0.25, 0)
        else:
            self.current_oxygen = min(self.current_oxygen + 1, self.max_oxygen)

    def handle_weapon(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_v] and self.changing_weapon_cooldown == 0:
            if self.current_weapon == 'boomerang':
                self.current_weapon = 'arrow'
            elif self.current_weapon == 'arrow':
                self.current_weapon = 'boomerang'
            self.changing_weapon_cooldown += 15
        if key[pygame.K_c]:
            if self.current_weapon == 'boomerang':
                if not self.projectiles.has(self.weapon):  # Make sure only one boomerang exists

                    if self.moving_direction == 1:
                        direction = pygame.Vector2((0, -1))
                    elif self.moving_direction == 2:
                        direction = pygame.Vector2((-1, 0))
                    elif self.moving_direction == 3:
                        direction = pygame.Vector2((0, 1))
                    else:
                        direction = pygame.Vector2((1, 0))

                    self.weapon = weapons[self.current_weapon](
                        (self.rect.centerx, self.rect.centery), direction,
                        self, self.settings)
                    self.projectiles.add(self.weapon)

            if self.current_weapon == 'arrow' and self.attack_cooldown == 0 and len(
                    self.projectiles.sprites()) < 3:
                self.attack_cooldown += 15
                self.weapon = weapons[self.current_weapon](
                    (self.rect.centerx, self.rect.centery),
                    self.moving_direction, self.settings)
                self.projectiles.add(self.weapon)

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

    def auto_scroll_down(self, scroll):
        self.rect.y += scroll
        if self.rect.bottom > self.settings.screen_height:
            self.rect.bottom = self.settings.screen_height
            for tile in self.stage.tile_list:
                # Check only blocks which are on screen and are interactable
                if tile[1].bottom > 0 and tile[
                        1].top < self.settings.screen_height and tile[
                            2].is_interactable:
                    # Check if it's solid:
                    if tile[2].is_solid:
                        # Player is scrolled before the blocks, so we check collision with block's rect
                        # + scroll, or, equivalently, player - scroll, now that we have already fixed player's position
                        # in case he was next to screen's bottom.
                        if tile[1].colliderect(self.rect.x,
                                               self.rect.y - scroll,
                                               self.rect.width,
                                               self.rect.height):
                            pygame.event.post(pygame.event.Event(pygame.USEREVENT, customType='world_map'))

    def auto_scroll_left(self, scroll):
        self.rect.x -= scroll
        if self.rect.left < 0:
            self.rect.left = 0
            for tile in self.stage.tile_list:
                # Check only blocks which are on screen and are interactable
                if tile[1].left > 0 and tile[1].right < self.settings.screen_width and tile[2].is_interactable:
                    # Check if it's solid:
                    if tile[2].is_solid:
                        # Player is scrolled before the blocks, so we check collision with block's rect
                        # + scroll, or, equivalently, player - scroll, now that we have already fixed player's position
                        # in case he was next to screen's bottom.
                        if tile[1].colliderect(self.rect.x + scroll,
                                               self.rect.y,
                                               self.rect.width,
                                               self.rect.height):
                            pygame.event.post(
                                pygame.event.Event(pygame.USEREVENT,
                                                   customType='end_game'))

    def update_cooldown(self):
        if self.changing_weapon_cooldown > 0:
            self.changing_weapon_cooldown -= 1
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

    def draw_slot_and_weapons(self):
        self.screen.blit(self.weapon_slot, (0, 60))
        if self.current_weapon == 'boomerang':
            self.weapon_or_ability_icon = pygame.transform.scale2x(pygame.image.load(
                os.path.abspath('advancing_hero/images/sprites/hero_weapons/boomerang/frame2.png')
                ))
            self.screen.blit(self.weapon_or_ability_icon, (10, 75))
        elif self.current_weapon == 'arrow':
            self.weapon_or_ability_icon = pygame.transform.scale2x(pygame.image.load(
                os.path.abspath('advancing_hero/images/sprites/hero_weapons/arrow/arrow.png')))
            self.screen.blit(self.weapon_or_ability_icon, (25, 75))
            self.regular_font.render_to(self.screen, (35, 110), (3 - len(self.projectiles.sprites())).__str__()+"X",
                                        self.settings.BLACK)
        elif self.current_weapon == 'regular_blast':
            self.weapon_or_ability_icon = pygame.transform.scale(pygame.image.load(
                os.path.abspath('advancing_hero/images/sprites/hero_weapons/regular_blast/regular_blast1.png')), (45, 45))
            self.screen.blit(self.weapon_or_ability_icon, (6, 67))
        elif self.current_weapon == 'mega_blast':
            self.weapon_or_ability_icon = pygame.transform.scale(pygame.image.load(
                os.path.abspath('advancing_hero/images/sprites/hero_weapons/mega_blast/blast1.png')), (50, 50))
            self.screen.blit(self.weapon_or_ability_icon, (9, 64))
        elif self.current_weapon == 'heal':
            self.weapon_or_ability_icon = pygame.transform.scale2x(pygame.image.load(
                os.path.abspath('advancing_hero/images/sprites/hero_weapons/heal/heal.png')))
            self.screen.blit(self.weapon_or_ability_icon, (15, 75))
        elif self.current_weapon == 'circle_lissajous':
            self.weapon_or_ability_icon = pygame.transform.scale(pygame.image.load(
                os.path.abspath('advancing_hero/images/sprites/hero_weapons/energy_ball/as_a_weapon/circle_mode.png')), (90, 90))
            self.screen.blit(self.weapon_or_ability_icon, (-15, 47))
        elif self.current_weapon == 'infinity_lissajous':
            self.weapon_or_ability_icon = pygame.transform.scale(pygame.image.load(
                os.path.abspath('advancing_hero/images/sprites/hero_weapons/energy_ball/as_a_weapon/infinity_mode.png')), (90, 90))
            self.screen.blit(self.weapon_or_ability_icon, (-15, 47))
        elif self.current_weapon == 'powerful_lissajous':
            self.weapon_or_ability_icon = pygame.transform.scale(pygame.image.load(
                os.path.abspath('advancing_hero/images/sprites/hero_weapons/energy_ball/as_a_weapon/especial_mode.png')), (90, 90))
            self.screen.blit(self.weapon_or_ability_icon, (-15, 47))

    def draw(self):
        surface_to_blit = self.image
        if self.invicibility_frames > 0 and self.invicibility_frames % 2 == 0:
            surface_to_blit = pygame.Surface([self.image.get_width(), self.image.get_height()], pygame.SRCALPHA)
        self.screen.blit(surface_to_blit, self.rect)
        if self.settings.DEBUG:
            pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)
        # Drawing health bar, oxygen bar and other images while paused (COPY from UPDATE)
        self.health_bar.update()
        self.oxygen_bar.update()
        self.draw_slot_and_weapons()

    def walk_animation(self, still_frame, direction, flip=False):
        if self.walking_framerate == 0:
            self.image_frame = still_frame - 1
            self.update_rect(flip)
        elif self.walking_framerate == 15 or self.walking_framerate == 45:
            self.image_frame = still_frame
            self.update_rect(flip)
        elif self.walking_framerate == 30:
            self.image_frame = still_frame + 1
            self.update_rect(flip)
        self.moving_direction = direction
        self.walking_framerate = (self.walking_framerate + 1) % 60

    def update_rect(self, flip=False):
        temp_rect = self.rect
        self.image = self.image_list[self.image_frame]
        self.image = pygame.transform.scale2x(self.image)
        if flip:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = temp_rect.x
        self.rect.y = temp_rect.y

    def hurt(self, damage):
        if self.invicibility_frames == 0:
            self.current_health = max(self.current_health - damage, 0)
            self.invicibility_frames = 60
        return True

    def heal(self, heal):
        self.current_health = min(self.current_health + heal, self.max_health)
        # Testing speed up effect (TSUE)
        #self.timer_fast_player = 600
        #self.speed_base = self.speed_base * 5
        #self.speed = self.speed_base
        return True

    def check_oxygen(self):
        if self.current_oxygen == 0:
            self.current_health = max(self.current_health - 0.5, 0)

    def check_alive(self):
        if self.current_health == 0:
            self.alive = False
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, customType='world_map'))

    def push(self):
        pass
