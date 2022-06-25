"""
Class of water block
"""
import os
from .block import Block


class Water(Block):
    """
    Represents the block of water
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/water.png',
    ):
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.WATER,
                         interactable=True)

    def player_interaction(self, player, *args, **kwargs):
        super().player_interaction(player)
        player.speed = max(0.5 * player.speed_base, 1)
        player.in_water = True


class Water2(Block):
    """
    Represents the block of water
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/water2.png',
    ):
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.WATER,
                         interactable=True)

    def player_interaction(self, player, *args, **kwargs):
        super().player_interaction(player)
        player.speed = max(0.4 * player.speed_base, 1)
        player.in_water = True


class Water3(Block):
    """
    Represents the block of water
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/water3.png',
    ):
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.WATER,
                         interactable=True)

    def player_interaction(self, player, *args, **kwargs):
        super().player_interaction(player)
        player.speed = max(0.4 * player.speed_base, 1)
        player.in_water = True
