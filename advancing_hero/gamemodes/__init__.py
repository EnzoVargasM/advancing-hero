"""
Init file for gamemodes module
"""
from .level import LevelGameMode
from .titlescreen import TitleScreen
from .endgame import EndGame
from .wingame import WinGame
from .journey_select import JourneySelect
from .character_select import CharacterSelectScreen
from .worldmap import WorldMap

modes = {
    'title_screen': TitleScreen,
    'level_main': LevelGameMode,
    'journey_select': JourneySelect,
    'character_select': CharacterSelectScreen,
    'world_map': WorldMap,
    'end_game': EndGame,
    'win_game': WinGame,

}