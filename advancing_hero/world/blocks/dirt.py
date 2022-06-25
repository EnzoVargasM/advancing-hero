"""
Class of dirt block
"""
import os
from .block import Block


class Dirt(Block):
    """
    Represents the block of dirt
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/dirt.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.DIRT,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(0.6 * player.speed_base, 1)


class Dirt2(Block):
    """
    Represents the block of dirt
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/dirt2.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.DIRT,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(0.6 * player.speed_base, 1)


class Dirt3(Block):
    """
    Represents the block of dirt
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/dirt3.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.DIRT,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(0.6 * player.speed_base, 1)


class Dirt4(Block):
    """
    Represents the block of dirt
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/dirt4.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.DIRT,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(0.6 * player.speed_base, 1)

