from .gamemode import GameMode
import pygame
import pygame.freetype
import os
import json


class WorldMap(GameMode):
    def __init__(self, screen, settings):
        super().__init__(screen)
        self.settings = settings
        self.game_title = pygame.freetype.Font(self.font_path, 50)
        self.background_image = pygame.transform.scale(
            pygame.image.load(
                os.path.abspath('advancing_hero/images/backgrounds/WorldMapTest.png')),
            self.settings.SIZE)
        self.selection_icon = pygame.transform.scale(
            pygame.image.load(
                os.path.abspath('advancing_hero/images/sprites/player/frame2.png')),
            (25, 40))
        self.menu_font = pygame.freetype.Font(self.font_path, 25)
        self.commands_font = pygame.freetype.Font(self.font_path, 15)
        self.tick = 0  # artificial timer
        self.icon_frame = 12  # Keep control of frame changes
        self.stage_positions = [(40, 224),
                                (178, 370),
                                (206, 470),
                                (478, 499),
                                (790, 420),
                                (558, 320),
                                (746, 200),
                                (539, 97),
                                (300, 50)]
        self.stage_closed_color = (255, 255, 255)
        self.stage_clear_color = (255, 255, 255)
        self.color_change = 0  # Tick for color change acording to timer
        self.music_path = os.path.abspath('advancing_hero/musics/sawsquarenoise-Stage3.ogg')
        with open('advancing_hero/world/journey_save_files.json') as save_files:
            self.json_data = json.load(save_files)
        save_files.close()
        aux = self.json_data
        if aux["current_level"][0] > aux["saves"][aux["current_file"][0]][2][aux["current_hero"][0]]-1:
            self.icon_position = aux["saves"][aux["current_file"][0]][2][aux["current_hero"][0]]-1
        else:
            self.icon_position = aux["current_level"][0]

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_path)
        pygame.music.play(-1)

    def loop(self, events):
        # Handle Stages Color in World Map
        self.color_change = (self.color_change + 2) % 256
        c = min(self.color_change, 255 - self.color_change)
        self.stage_closed_color = (220-int(c/4), 220-int(c/4), 220-int(c/4))
        c_limited = min(c * int(408/128), 204)
        self.stage_clear_color = (c_limited, 204 - c_limited, 204 - c_limited)

        # Handle character movement in World Map
        self.tick = self.tick + 1
        if self.tick > 20:
            self.tick = 0  # reset timer
            # Change hero frame
            if self.icon_frame == 12:
                self.icon_frame = 23
            elif self.icon_frame == 21:
                self.icon_frame = 12
            elif self.icon_frame == 23:
                self.icon_frame = 32
            elif self.icon_frame == 32:
                self.icon_frame = 21


        self.screen.blit(self.background_image, (0, 0))
        self.game_title.render_to(self.screen,
                                  (self.settings.screen_width / 2 - 130,
                                   self.settings.screen_height / 2 - 256),
                                  "World", self.stage_closed_color, style=3)
        aux = self.json_data
        stages_cleared_number = aux["saves"][aux["current_file"][0]][2][aux["current_hero"][0]]
        for i in range(len(self.stage_positions)):
            if i < stages_cleared_number:
                self.menu_font.render_to(self.screen,
                                         self.stage_positions[i],
                                         str(i+1), self.stage_clear_color, style=3)
            else:
                self.menu_font.render_to(self.screen,
                                         self.stage_positions[i],
                                         str(i+1), self.stage_closed_color, style=3)

        self.commands_font.render_to(self.screen,
                                     (10, self.settings.screen_height - 30),
                                     "Press Left and Right to Select Stage",
                                     self.settings.BLACK)

        self.selection_icon = pygame.transform.scale(
            pygame.image.load(
                os.path.abspath(f'advancing_hero/images/sprites/player/frame{int(self.icon_frame/10)}.png')),
            (25, 40))
        self.screen.blit(
            self.selection_icon,
            self.stage_positions[self.icon_position])

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if self.icon_position > 0:
                        self.icon_position = self.icon_position - 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if self.icon_position < stages_cleared_number - 1:
                        self.icon_position = self.icon_position + 1
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if 0 <= self.icon_position <= 8:
                        with open('advancing_hero/world/journey_save_files.json', 'w') as outfile:
                            aux = self.json_data
                            aux["current_level"][0] = self.icon_position
                            json.dump(aux, outfile)
                        outfile.close()
                        pygame.event.post(
                            pygame.event.Event(pygame.USEREVENT,
                                               customType='init_level',
                                               level=self.settings.levels[self.icon_position],
                                               scroll_mode=self.settings.levels_mode[self.icon_position]))

                if event.key == pygame.K_ESCAPE:
                    pygame.display.update()
                    pygame.time.wait(100)
                    pygame.event.post(
                        pygame.event.Event(pygame.USEREVENT,
                                           customType='character_select'))
