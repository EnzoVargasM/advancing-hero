"""
Class of water block
"""
import os
from .block import Block
import math


class CurrentWaterRight(Block):
    """
    Represents the block of water
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/curwaterR.png',
    ):
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.WATER,
                         interactable=True)

    def player_interaction(self, player, *args, **kwargs):
        super().player_interaction(player)
        player.in_water = False
        player.speed = player.speed_base
        dx = 1
        dy = 0

        for tile in player.stage.tile_list:
            # Check only blocks which are on screen and are interactable
            if tile[1].bottom > 0 and tile[
                1].top < player.settings.screen_height and tile[
                2].is_interactable:

                # Then check if it's solid. We do it on that order in case
                # the block changes the player's speed.
                if tile[2].is_solid and (dx or dy):
                    # Check collision in x direction
                    delta_x = 1 * dx / math.sqrt(dx * dx + dy * dy)
                    delta_y = 1 * dy / math.sqrt(dx * dx + dy * dy)
                    if tile[1].colliderect(player.rect.x + delta_x, player.rect.y,
                                           player.rect.width, player.rect.height):
                        dx = 0
                    # Check for collision in y direction
                    if tile[1].colliderect(player.rect.x, player.rect.y + delta_y,
                                           player.rect.width, player.rect.height):
                        dy = 0

        if dx or dy:
            player.rect.x += 1 * dx / math.sqrt(dx * dx + dy * dy)
            player.rect.y += 1 * dy / math.sqrt(dx * dx + dy * dy)

        if player.rect.bottom > player.settings.screen_height:
            player.rect.bottom = player.settings.screen_height
        if player.rect.top < 0:
            player.rect.top = 0
        if player.rect.right > player.settings.screen_width:
            player.rect.right = player.settings.screen_width
        if player.rect.left < 0:
            player.rect.left = 0


class CurrentWaterLeft(Block):
    """
    Represents the block of water
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/curwaterL.png',
    ):
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.WATER,
                         interactable=True)

    def player_interaction(self, player, *args, **kwargs):
        super().player_interaction(player)
        player.in_water = False
        player.speed = player.speed_base
        dx = -1
        dy = 0

        for tile in player.stage.tile_list:
            # Check only blocks which are on screen and are interactable
            if tile[1].bottom > 0 and tile[
                1].top < player.settings.screen_height and tile[
                2].is_interactable:

                # Then check if it's solid. We do it on that order in case
                # the block changes the player's speed.
                if tile[2].is_solid and (dx or dy):
                    # Check collision in x direction
                    delta_x = 1 * dx / math.sqrt(dx * dx + dy * dy)
                    delta_y = 1 * dy / math.sqrt(dx * dx + dy * dy)
                    if tile[1].colliderect(player.rect.x + delta_x, player.rect.y,
                                           player.rect.width, player.rect.height):
                        dx = 0
                    # Check for collision in y direction
                    if tile[1].colliderect(player.rect.x, player.rect.y + delta_y,
                                           player.rect.width, player.rect.height):
                        dy = 0

        if dx or dy:
            player.rect.x += 1 * dx / math.sqrt(dx * dx + dy * dy)
            player.rect.y += 1 * dy / math.sqrt(dx * dx + dy * dy)

        if player.rect.bottom > player.settings.screen_height:
            player.rect.bottom = player.settings.screen_height
        if player.rect.top < 0:
            player.rect.top = 0
        if player.rect.right > player.settings.screen_width:
            player.rect.right = player.settings.screen_width
        if player.rect.left < 0:
            player.rect.left = 0


class CurrentWaterDown(Block):
    """
    Represents the block of water
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/curwaterD.png',
    ):
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.WATER,
                         interactable=True)

    def player_interaction(self, player, *args, **kwargs):
        super().player_interaction(player)
        player.in_water = False
        player.speed = player.speed_base
        dy = 1
        dx = 0

        for tile in player.stage.tile_list:
            # Check only blocks which are on screen and are interactable
            if tile[1].bottom > 0 and tile[
                1].top < player.settings.screen_height and tile[
                2].is_interactable:

                # Then check if it's solid. We do it on that order in case
                # the block changes the player's speed.
                if tile[2].is_solid and (dx or dy):
                    # Check collision in x direction
                    delta_x = 1 * dx / math.sqrt(dx * dx + dy * dy)
                    delta_y = 1 * dy / math.sqrt(dx * dx + dy * dy)
                    if tile[1].colliderect(player.rect.x + delta_x, player.rect.y,
                                           player.rect.width, player.rect.height):
                        dx = 0
                    # Check for collision in y direction
                    if tile[1].colliderect(player.rect.x, player.rect.y + delta_y,
                                           player.rect.width, player.rect.height):
                        dy = 0

        if dx or dy:
            player.rect.x += 1 * dx / math.sqrt(dx * dx + dy * dy)
            player.rect.y += 1 * dy / math.sqrt(dx * dx + dy * dy)

        if player.rect.bottom > player.settings.screen_height:
            player.rect.bottom = player.settings.screen_height
        if player.rect.top < 0:
            player.rect.top = 0
        if player.rect.right > player.settings.screen_width:
            player.rect.right = player.settings.screen_width
        if player.rect.left < 0:
            player.rect.left = 0


class CurrentWaterUp(Block):
    """
    Represents the block of water
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/curwaterU.png',
    ):
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.WATER,
                         interactable=True)

    def player_interaction(self, player, *args, **kwargs):
        super().player_interaction(player)
        player.in_water = False
        player.speed = player.speed_base
        dy = -1
        dx = 0

        for tile in player.stage.tile_list:
            # Check only blocks which are on screen and are interactable
            if tile[1].bottom > 0 and tile[
                1].top < player.settings.screen_height and tile[
                2].is_interactable:

                # Then check if it's solid. We do it on that order in case
                # the block changes the player's speed.
                if tile[2].is_solid and (dx or dy):
                    # Check collision in x direction
                    delta_x = 1 * dx / math.sqrt(dx * dx + dy * dy)
                    delta_y = 1 * dy / math.sqrt(dx * dx + dy * dy)
                    if tile[1].colliderect(player.rect.x + delta_x, player.rect.y,
                                           player.rect.width, player.rect.height):
                        dx = 0
                    # Check for collision in y direction
                    if tile[1].colliderect(player.rect.x, player.rect.y + delta_y,
                                           player.rect.width, player.rect.height):
                        dy = 0

        if dx or dy:
            player.rect.x += 1 * dx / math.sqrt(dx * dx + dy * dy)
            player.rect.y += 1 * dy / math.sqrt(dx * dx + dy * dy)

        if player.rect.bottom > player.settings.screen_height:
            player.rect.bottom = player.settings.screen_height
        if player.rect.top < 0:
            player.rect.top = 0
        if player.rect.right > player.settings.screen_width:
            player.rect.right = player.settings.screen_width
        if player.rect.left < 0:
            player.rect.left = 0