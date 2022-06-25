## Editor for enemies in the game :)
import pygame
import math
import pickle
from os import path
import json
##### ENEMIES - ÚNICA PARTE EDITÁVEL DO CÓDIGO ###########
enemy_name = 'bat_sprite'
enemy_list = ['bat_sprite', 'monster_sprite', 'ship_sprite', 'potion_heal', 'boss', 'win_stage',
              'vertical_runner', 'horizontal_runner', 'chaser', 'chaser_explosive', 'potion_speed',
              'potion_speed_down', 'potion_small', 'potion_big', 'chaser_big_explosive']
enemies_available = {
    'bat_sprite':
    pygame.image.load(
        path.abspath('../advancing_hero/images/sprites/regular_enemies/bat/frame1.png')),
    'monster_sprite':
    pygame.image.load(
        path.abspath('../advancing_hero/images/sprites/regular_enemies/monster/frame1.png')),
    'potion_heal':
    pygame.image.load(
        path.abspath(
            '../advancing_hero/images/sprites/potions/potion_heal/red_potion.png')),
    'ship_sprite':
    pygame.image.load(
        path.abspath('../advancing_hero/images/sprites/regular_enemies/ship/frame1.png')),
    'boss':
        pygame.image.load(
            path.abspath('../advancing_hero/images/sprites/boss_enemies/boss/a.png')),
    'win_stage':
        pygame.image.load(
            path.abspath(
                '../advancing_hero/images/sprites/win_stage/win_stage1.png')),
    'vertical_runner':
        pygame.image.load(
            path.abspath(
                '../advancing_hero/images/sprites/regular_enemies/vertical_runner/a.png')),
    'horizontal_runner':
            pygame.image.load(
                path.abspath(
                    '../advancing_hero/images/sprites/regular_enemies/horizontal_runner/a.png')),
    'chaser':
        pygame.image.load(
            path.abspath(
                '../advancing_hero/images/sprites/regular_enemies/chaser/a.png')),
    'chaser_explosive':
        pygame.image.load(
            path.abspath(
                '../advancing_hero/images/sprites/regular_enemies/chaser_explosive/a.png')),
    'potion_speed':
            pygame.image.load(
                path.abspath(
                    '../advancing_hero/images/sprites/potions/potion_speed/speedup_item.png')),
    'potion_speed_down':
                pygame.image.load(
                    path.abspath(
                        '../advancing_hero/images/sprites/potions/potion_speed_down/speedown_item.png')),
    'potion_small':
                pygame.image.load(
                    path.abspath(
                        '../advancing_hero/images/sprites/potions/potion_small/potion_small.png')),
    'potion_big':
                pygame.image.load(
                    path.abspath(
                        '../advancing_hero/images/sprites/potions/potion_big/potion_big.png')),
    'chaser_big_explosive':
                pygame.image.load(
                    path.abspath(
                        '../advancing_hero/images/sprites/regular_enemies/chaser_big_explosive/a.png')),

}
###########################################################

pygame.init()
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
fps = 30

#game window
tile_size = 64
screen_cols = 16
screen_rows = 9
cols = 16
rows = 150
screen_width = tile_size * screen_cols
screen_height = (tile_size * screen_rows)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Enemies Level Editor')

#load images
grass_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/grass.png'))
dirt_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/dirt.png'))
water_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/water.png'))
brick_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/brick.png'))
asphalt_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/asphalt.png'))
lava_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/lava.png'))

CuWaterLeft_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/curwaterL.png'))
CuWaterRight_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/curwaterR.png'))
CuWaterUp_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/curwaterU.png'))
CuWaterDown_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/curwaterD.png'))

grass_2_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/grass8.png'))

asph2_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/asphalt2.png'))
asph3_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/asphalt3.png'))
asph4_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/asphalt4.png'))
asph5_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/asphalt5.png'))
asph6_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/asphalt6.png'))

brick2_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/brick2.png'))
brick3_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/brick3.png'))
brick4_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/brick4.png'))

dirt2_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/dirt2.png'))
dirt3_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/dirt3.png'))
dirt4_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/dirt4.png'))

grass2_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/grass2.png'))
grass3_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/grass3.png'))
grass4_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/grass4.png'))
grass5_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/grass5.png'))

water2_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/water2.png'))
water3_img = pygame.image.load(path.abspath('../advancing_hero/images/blocks/water3.png'))

img_list = [grass_img, dirt_img, water_img, brick_img, asphalt_img, lava_img, CuWaterLeft_img, CuWaterRight_img, CuWaterUp_img, CuWaterDown_img, grass_2_img,
            asph2_img, asph3_img, asph4_img, asph5_img, asph6_img,
            brick2_img, brick3_img, brick4_img,
            dirt2_img, dirt3_img, dirt4_img,
            grass2_img, grass3_img, grass4_img, grass5_img,
            water2_img, water3_img]
block_quantity = len(img_list)+1

#define game variables
clicked = False
up_ticks = 0
right_ticks = 0
enemy_number=0

#define colours
white = (255, 255, 255)
green = (144, 201, 120)
gray = (197, 194, 197)

font = pygame.font.SysFont('Futura', 24)

## Create world data and try to load existent world
world_data = []
for row in range(rows):
    r = [0] * cols
    world_data.append(r)
## Load existant world
#./advancing_hero/world
with open('../scripts/world.json') as world_file:
    existant_world = json.load(world_file)
aux = existant_world
enemies = existant_world['sprite_data']
existant_world = existant_world['block_data']

existant_world.reverse()
for row_index, row in enumerate(existant_world):
    for col_index, data in enumerate(row):
        if col_index < cols and row_index < rows:
            world_data[rows - row_index - 1][col_index] = data

#print(world_data)


#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_grid():
    ## drawn horizontal lines
    for i in range(rows + 2):
        pygame.draw.line(screen, white, (0, i * tile_size),
                         (screen_width, i * tile_size))
    ## drawn vertical lines
    for i in range(cols + 2):
        pygame.draw.line(screen, white, (i * tile_size, 0),
                         (i * tile_size, screen_height))


def draw_world():
    for row in range(screen_rows):
        for col in range(screen_cols):
            if world_data[rows - 1 - row - up_ticks][col] > 0:
                for i in range(1, block_quantity):
                    if world_data[rows - 1 - row - up_ticks][col + right_ticks] == i:
                        img = pygame.transform.scale(img_list[i-1], (tile_size, tile_size))
                        screen.blit(img, (col * tile_size, (screen_rows - 1 - row) * tile_size))


def draw_enemies():
    #print(len(enemies))
    for _, sprite_element in enumerate(reversed(enemies)):
        d = screen_height - sprite_element[2] + up_ticks * 64

        if 0 <= d <= screen_height:
            img = enemies_available[sprite_element[0]]
            aux = sprite_element[2]
            if sprite_element[2] > screen_height:
                aux = (screen_height - sprite_element[2])
            screen.blit(img, (sprite_element[1], aux + up_ticks * 64))
            pygame.draw.circle(screen, BLUE, (sprite_element[1], aux + up_ticks * 64), 10)


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


#main game loop
run = True
while run:

    clock.tick(fps)

    #draw background
    screen.fill(green)

    #show the grid and draw the level tiles
    draw_grid()
    draw_world()
    draw_enemies()

    #text showing current level
    draw_text(f'Up: {up_ticks}, Right: {right_ticks}', font, white, tile_size, screen_height - 60)
    draw_text('Press UP or DOWN to change level', font, white, tile_size,
              screen_height - 40)

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            with open('world.json', 'w') as outfile:
                aux['block_data'] = world_data
                aux['sprite_data'] = enemies
                json.dump(aux, outfile)
            run = False
        #mouseclicks to change tiles
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            new_y = y + up_ticks * 64
            new_x = x + right_ticks * 64

            if new_y > screen_height:
                new_y = screen_height - y + up_ticks * 64


            print(y)
            print(new_y)
            print(x)
            print(new_x)
            a = []
            for index, enemy in enumerate(enemies):
                if math.dist([new_x, new_y], [enemy[1], enemy[2]]) < 10:
                    continue
                else:
                    a.append(enemy)

            if len(a) == len(enemies):
                a.append([enemy_name, new_x, new_y])
            enemies = a.copy()
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        #up and down key presses to change level number
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and up_ticks <= rows - 1 - screen_rows:
                up_ticks += 1
            elif event.key == pygame.K_DOWN and up_ticks > 0:
                up_ticks -= 1
            elif event.key == pygame.K_RIGHT and right_ticks <= cols - 1 - screen_cols:
                right_ticks += 1
            elif event.key == pygame.K_LEFT and right_ticks > 0:
                right_ticks -= 1
            elif event.key == pygame.K_a:
                enemy_number=(enemy_number-1) % len(enemy_list)
                enemy_name=enemy_list[enemy_number]
            elif event.key == pygame.K_d:
                enemy_number = (enemy_number + 1) % len(enemy_list)
                enemy_name = enemy_list[enemy_number]

    pygame.display.update()

pygame.quit()