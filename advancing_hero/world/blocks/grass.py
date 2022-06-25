"""
Class of grass block
"""
import os
from .block import Block


class Grass(Block):
    """
    Represents the block of grass
    """
    def __init__(
        self,
        settings,
        path: str = 'advancing_hero/images/blocks/grass.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.GRASS,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(player.speed_base, 1)


class Grass_2(Block):
    """
    Represents the block of grass
    """
    def __init__(
        self,
        settings,
        path: str = 'advancing_hero/images/blocks/grass1.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.GRASS,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(player.speed_base, 1)


class Grass2(Block):
    """
    Represents the block of grass
    """
    def __init__(
        self,
        settings,
        path: str = 'advancing_hero/images/blocks/grass2.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.GRASS,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(player.speed_base, 1)


class Grass3(Block):
    """
    Represents the block of grass
    """
    def __init__(
        self,
        settings,
        path: str = 'advancing_hero/images/blocks/grass3.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.GRASS,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(player.speed_base, 1)


class Grass4(Block):
    """
    Represents the block of grass
    """
    def __init__(
        self,
        settings,
        path: str = 'advancing_hero/images/blocks/grass4.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.GRASS,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(player.speed_base, 1)


class Grass5(Block):
    """
    Represents the block of grass
    """
    def __init__(
        self,
        settings,
        path: str = 'advancing_hero/images/blocks/grass5.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.GRASS,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(player.speed_base, 1)
