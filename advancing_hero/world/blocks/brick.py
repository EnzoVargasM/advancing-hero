"""
Class of brick block
"""
import os
from .block import Block


class Brick(Block):
    """
    Represents the block of brick
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/brick.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.BRICK,
                         is_solid=True,
                         interactable=True)


class Brick2(Block):
    """
    Represents the block of brick
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/brick2.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.BRICK,
                         is_solid=True,
                         interactable=True)


class Brick3(Block):
    """
    Represents the block of brick
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/brick3.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.BRICK,
                         is_solid=True,
                         interactable=True)


class Brick4(Block):
    """
    Represents the block of brick
    """
    def __init__(
        self,
        settings: any,
        path: str = 'advancing_hero/images/blocks/brick4.png',
    ) -> None:
        super().__init__(os.path.abspath(path),
                         settings,
                         settings.BRICK,
                         is_solid=True,
                         interactable=True)
