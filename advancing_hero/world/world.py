"""
Class that defines the World
"""
import json
import pygame
from . import blocks
from .. import sprites


class World:
    """
    Defines the state of the world in which
    our hero walks
    """

    def __init__(self, settings, level_data, screen, scroll_mode='Down') -> None:
        self.tile_list = []
        self.settings = settings
        self.scroll_mode = scroll_mode
        with open(level_data) as world_file:
            self.json_data = json.load(world_file)
        self.stage_data = self.json_data["block_data"]
        self.sprite_data = self.json_data["sprite_data"]
        #print(self.sprite_data)
        self.stage_data.reverse()

        self.blocks = {
            1: blocks.Grass,
            2: blocks.Dirt,
            3: blocks.Water,
            4: blocks.Brick,
            5: blocks.Asphalt,
            6: blocks.Lava,
            7: blocks.CurrentWaterLeft,
            8: blocks.CurrentWaterRight,
            9: blocks.CurrentWaterUp,
            10: blocks.CurrentWaterDown
        }

        self.sprites = {
            'bat_sprite': sprites.Bat,
            'monster_sprite': sprites.Monster,
            'potion_heal': sprites.PotionHeal,
            'ship_sprite': sprites.Ship,
            'boss': sprites.Boss,
            'win_stage': sprites.WinStage
        }

        self.true_scroll = 0.0
        self.screen = screen
        self.frame_counter = 0
        self.scroll_amount = 0

        for row_index, row_element in enumerate(self.stage_data):
            for column_index, tile in enumerate(row_element):
                block = self.blocks[tile](settings=self.settings)
                block.add_block_to_stage(
                    self.tile_list, column_index,
                    self.settings.SCREEN_ROWS - 1 - row_index)

        self.all_enemies = pygame.sprite.Group()

        # Spawn sprites which should be on screen already (i.e., position y <= screen.height
        for _, sprite_element in enumerate(reversed(self.sprite_data)):
            if sprite_element[2] <= self.settings.screen_height:
                new_sprite = self.sprites[sprite_element[0]](
                    position=(sprite_element[1], sprite_element[2]),
                    screen=screen)
                self.all_enemies.add(new_sprite)
                self.sprite_data.remove(sprite_element)

    def update(self, screen: any, player1, player2=None) -> None:
        """
        Draw the world according to the player position

            Args:

                screen: pygame screen
                :param screen:
                :param player:
        """
        self.scroll_amount = 0
        if player2 is not None:
            self.scroll_world(screen, player1, player2)
        else:
            self.scroll_world(screen, player1)

        self.all_enemies.update(player1, self)
        #if player2 is not None:
        #    self.all_enemies.update(player2, self)
        self.all_enemies.draw(self.screen)

        if self.settings.DEBUG:
            for sprite in self.all_enemies.sprites():
                outline = sprite.mask.outline()
                outline_image = pygame.Surface(sprite.rect.size).convert_alpha()
                outline_image.fill((0, 0, 0, 0))
                for point in outline:
                    outline_image.set_at(point, (255, 0, 0))
                self.screen.blit(outline_image, sprite.rect)
            print(len(self.all_enemies.sprites()))

        self.frame_counter += 1

    def scroll_world(self, screen, player1, player2=None):
        if self.scroll_mode == 'Down':
            if self.frame_counter % 2 == 0:
                prev_scroll = self.true_scroll
                if self.true_scroll <= \
                        (len(self.stage_data) - self.settings.SCREEN_ROWS) * self.settings.tile_size:
                    self.true_scroll += self.settings.WORLD_SPEED
                scroll = int(self.true_scroll)
                self.scroll_amount = scroll - prev_scroll
                player1.auto_scroll_down(self.scroll_amount)
                if player2 is not None:
                    player2.auto_scroll_down(self.scroll_amount)
            for tile in self.tile_list:
                if self.frame_counter % 2 == 0:
                    tile[1].y += self.scroll_amount
                screen.blit(tile[0], tile[1])
                if self.settings.DEBUG:
                    pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
        if self.scroll_mode == 'Left':
            if self.frame_counter % 2 == 0:
                prev_scroll = self.true_scroll
                if self.true_scroll <= \
                        (len(self.stage_data[0]) - self.settings.SCREEN_COLUMNS) * self.settings.tile_size:
                    self.true_scroll += self.settings.WORLD_SPEED
                scroll = int(self.true_scroll)
                self.scroll_amount = scroll - prev_scroll
                player1.auto_scroll_left(self.scroll_amount)
                if player2 is not None:
                    player2.auto_scroll_left(self.scroll_amount)
            for tile in self.tile_list:
                if self.frame_counter % 2 == 0:
                    tile[1].x -= self.scroll_amount
                screen.blit(tile[0], tile[1])
                if self.settings.DEBUG:
                    pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)



        # Check if we should spawn new sprites
        for _, sprite_element in enumerate(reversed(self.sprite_data)):
            if sprite_element[2] <= self.settings.screen_height + self.true_scroll:
                #print(sprite_element)
                new_sprite = self.sprites[sprite_element[0]](position=(
                    sprite_element[1], sprite_element[2] -
                    (self.settings.screen_height + self.true_scroll)),
                    screen=screen)
                self.all_enemies.add(new_sprite)
                self.sprite_data.remove(sprite_element)

    # Function specific for drawing the map while paused
    def paused_drawing(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
        self.all_enemies.draw(self.screen)
