"""
Class of asplaht block
"""
import os
from .block import Block


class Asphalt(Block):
    """
    Represents the block of asphalt
    """

    def __init__(
            self,
            settings: any,
            path: str = 'advancing_hero/images/blocks/asphalt.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.ASPHALT,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(player.speed_base, 1)


class Asphalt2(Block):
    """
    Represents the block of asphalt
    """

    def __init__(
            self,
            settings: any,
            path: str = 'advancing_hero/images/blocks/asphalt2.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.ASPHALT,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(player.speed_base, 1)


class Asphalt3(Block):
    """
    Represents the block of asphalt
    """

    def __init__(
            self,
            settings: any,
            path: str = 'advancing_hero/images/blocks/asphalt3.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.ASPHALT,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(player.speed_base, 1)


class Asphalt4(Block):
    """
    Represents the block of asphalt
    """

    def __init__(
            self,
            settings: any,
            path: str = 'advancing_hero/images/blocks/asphalt4.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.ASPHALT,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(player.speed_base, 1)


class Asphalt5(Block):
    """
    Represents the block of asphalt
    """

    def __init__(
            self,
            settings: any,
            path: str = 'advancing_hero/images/blocks/asphalt5.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.ASPHALT,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(player.speed_base, 1)


class Asphalt6(Block):
    """
    Represents the block of asphalt
    """

    def __init__(
            self,
            settings: any,
            path: str = 'advancing_hero/images/blocks/asphalt6.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.ASPHALT,
                         interactable=True)

    def player_interaction(self, player):
        super().player_interaction(player)
        player.speed = max(player.speed_base, 1)
