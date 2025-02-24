import pygame
import pickle
from os import path
import json

pygame.init()

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
pygame.display.set_caption('Level Editor')

# block_quantity = 7
block_type = 0

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
right_tiks = 0

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
with open('../scripts/world.json') as world_file:
    existant_world = json.load(world_file)
aux = existant_world
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
            if world_data[rows - 1 - row - up_ticks][col + right_tiks] > 0:
                for i in range(1, block_quantity):
                    if world_data[rows - 1 - row - up_ticks][col + right_tiks] == i:
                        img = pygame.transform.scale(img_list[i-1], (tile_size, tile_size))
                        screen.blit(img, (col * tile_size, (screen_rows - 1 - row) * tile_size))



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

    #text showing current level
    draw_text(f'Up: {up_ticks}, Right: {right_tiks}', font, white, tile_size, screen_height - 80)
    draw_text('Press UP, DOWN, LEFT and RIGHT to change level', font, white, tile_size,
              screen_height - 60)
    draw_text('Block Type:', font, white, tile_size,
              screen_height - 40)
    draw_text('Types: Q - Floor, W - Wall, E - Water ...', font, white, 250,
              screen_height - 40)
    img = pygame.transform.scale(img_list[block_type - 1], (tile_size/2, tile_size/2))
    screen.blit(img, (170, screen_height - 40))

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            with open('world.json', 'w') as outfile:
                aux['block_data'] = world_data
                json.dump(aux, outfile)
            run = False
        #mouseclicks to change tiles
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
            pos = pygame.mouse.get_pos()
            x = pos[0] // tile_size
            y = pos[1] // tile_size
            y = screen_rows - 1 - y
            y1 = rows - 1 - y - up_ticks
            x1 = x + right_tiks

            #check that the coordinates are within the tile area
            if x1 < cols and y1 < rows:
                #update tile value
                if pygame.mouse.get_pressed()[0] == 1:
                    world_data[y1][x1] = block_type

        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        #up and down key presses to change level number
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and up_ticks <= rows - 1 - screen_rows:
                up_ticks += 1
            elif event.key == pygame.K_DOWN and up_ticks > 0:
                up_ticks -= 1
            elif event.key == pygame.K_RIGHT and right_tiks <= cols - 1 - screen_cols:
                right_tiks += 1
            elif event.key == pygame.K_LEFT and right_tiks > 0:
                right_tiks -= 1
            elif event.key == pygame.K_a:
                block_type = (block_type - 1) % block_quantity
            elif event.key == pygame.K_d:
                block_type = (block_type + 1) % block_quantity

            #print(level)

    ## update scrollbar
    #update game display window

    pygame.display.update()

pygame.quit()
