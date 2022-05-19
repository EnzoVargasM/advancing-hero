TITLE = 'Advancing Hero'
SCREEN_ROWS = 9
SCREEN_COLUMNS = 16
SIZE = screen_width, screen_height = 64 * 16, 64 * 9
FPS = 60
tile_size = 64

current_file = 0
current_level = 0

## Speeds
WORLD_SPEED = 1
DEFAULT_PLAYER_SPEED = 5


## Block names
ASPHALT = 'black_rock'
BRICK = 'gray_rock'
GRASS = 'grass'
DIRT = 'sand'
WATER = 'water'
LAVA = 'lava'

# level_1 = 'advancing_hero/world/world.json'
levels = ['advancing_hero/world/level1.json',  # 1
          'advancing_hero/world/level2.json',
          'advancing_hero/world/level3.json',
          'advancing_hero/world/level4.json',
          'advancing_hero/world/level5.json',  # 5
          'advancing_hero/world/level5.json',
          'advancing_hero/world/level5.json',  # 7
          'advancing_hero/world/level5.json',
          'advancing_hero/world/level5.json'  # 9
          ]

levels_mode = ['Down',  # 1
               'Left',
               'Down',
               'Left',
               'Down',  # 5
               'Down',
               'Down',  # 7
               'Down',
               'Down'   # 9
               ]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## DEBUG
DEBUG = False
