from .gamemode import GameMode
import pygame
import pygame.freetype
import os
import json


class JourneySelect(GameMode):
    def __init__(self, screen, settings):
        super().__init__(screen)
        self.settings = settings
        self.game_title = pygame.freetype.Font(self.font_path, 50)
        self.background_image = pygame.transform.scale(
            pygame.image.load(
                os.path.abspath('advancing_hero/images/backgrounds/TitleScreen.png')),
            self.settings.SIZE)
        self.selection_icon = pygame.transform.scale(
            pygame.image.load(os.path.abspath('advancing_hero/images/select_icon.png')), (40, 40))
        self.file_select = pygame.transform.scale(
            pygame.image.load(os.path.abspath('advancing_hero/images/file_select.png')), (300, 420))
        self.menu_font = pygame.freetype.Font(self.font_path, 25)
        self.commands_font = pygame.freetype.Font(self.font_path, 15)
        self.icon_position = 0
        self.file_selected = -1
        self.music_path = os.path.abspath('advancing_hero/musics/sawsquarenoise-Stage3.ogg')
        # Load database with save files
        with open('advancing_hero/world/journey_save_files.json') as save_files:
            self.json_data = json.load(save_files)
        save_files.close()
        self.save_files_data = self.json_data["saves"]
        # List of heroes' frames
        self.hero_list = [
            pygame.transform.scale(
                pygame.image.load(
                    os.path.abspath('advancing_hero/images/sprites/player/frame2.png')),
                (40, 64)),
            pygame.transform.scale(
                pygame.image.load(
                    os.path.abspath('advancing_hero/images/sprites/player_mage/frame2.png')),
                (40, 64)),
            pygame.transform.scale(
                pygame.image.load(
                    os.path.abspath('advancing_hero/images/sprites/player_monk/frame2.png')),
                (40, 64))
        ]

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_path)
        pygame.music.play(-1)

    def loop(self, events):
        # Print background
        self.screen.blit(self.background_image, (0, 0))
        # Print Screen Title
        self.game_title.render_to(self.screen,
                                  (self.settings.screen_width / 2 - 330,
                                   self.settings.screen_height / 2 - 256),
                                  "Journey Selection", self.settings.WHITE)
        menu_options = ["S1", "S2", "S3"]
        for i in range(0, 3):

            # Print file image
            file_y_start = 130
            self.screen.blit(self.file_select, (30 + i * self.settings.screen_width / 3, file_y_start))
            # Print Journey Number
            self.menu_font.render_to(self.screen, (85 + i * self.settings.screen_width / 3, file_y_start + 20),
                                     "Journey " + (i + 1).__str__(), self.settings.WHITE)

            # Print information of file
            if self.save_files_data[i][0] == 1:
                self.menu_font.render_to(self.screen, (43 + i * self.settings.screen_width / 3, file_y_start + 60),
                                         "Game Completion " + (self.save_files_data[i][1]).__str__() + " of 100",
                                         self.settings.WHITE, size=13)
                for j in range(0, 3):
                    self.menu_font.render_to(self.screen, (43 + i * self.settings.screen_width / 3, file_y_start+90+70*j),
                                             "Hero " + (j+1).__str__(),
                                             self.settings.WHITE, size=13)

                    if self.save_files_data[i][2][j] >= 0:
                        self.screen.blit(
                            self.hero_list[j],
                            (43 + 220 + i * self.settings.screen_width / 3, file_y_start + 90 + 70 * j))

                        if self.save_files_data[i][2][j] == 9:
                            self.menu_font.render_to(self.screen, (
                            43 + i * self.settings.screen_width / 3, file_y_start + 110 + 70 * j),
                                                     "Complete",
                                                     self.settings.WHITE, size=13)
                        else:
                            self.menu_font.render_to(self.screen, (43 + i * self.settings.screen_width / 3, file_y_start+110+70*j),
                                                     "In Progress: " + (self.save_files_data[i][2][j]).__str__() + " of 9",
                                                     self.settings.WHITE, size=13)
                    else:
                        self.menu_font.render_to(self.screen, (43 + i * self.settings.screen_width / 3, file_y_start+110 + 70 * j),
                                                 "Locked ", self.settings.WHITE, size=13)
            if self.save_files_data[i][0] == 0:
                self.menu_font.render_to(self.screen, (90 + i * self.settings.screen_width / 3, file_y_start+180),
                                         "New File", self.settings.WHITE)
        # Print Bottom Description
        self.commands_font.render_to(self.screen,
                                     (10, self.settings.screen_height - 30),
                                     "SPACE or ENTER: ENTER   W or UP: UP   S or DOWN: DOWN",
                                     self.settings.BLACK)
        if self.file_selected == -1:
            self.screen.blit(self.selection_icon, (30 + self.icon_position * self.settings.screen_width / 3, 130))
        else:
            self.screen.blit(self.selection_icon, (75 + 77 * self.icon_position +\
                                                   self.file_selected * self.settings.screen_width / 3, 475))
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.file_selected == -1:
                        pygame.time.wait(150)
                        pygame.event.post(
                            pygame.event.Event(pygame.USEREVENT,
                                               customType='title_screen'))
                    else:
                        self.icon_position = self.file_selected
                        self.file_selected = -1
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if self.icon_position > 0:
                        self.icon_position = (self.icon_position - 1) % 3
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if self.icon_position < 2:
                        self.icon_position = (self.icon_position + 1) % 3
                if event.key == pygame.K_BACKSPACE:
                    self.icon_position = self.file_selected
                    self.file_selected = -1
                if event.key == pygame.K_SPACE:
                    if self.file_selected == -1:
                        if self.icon_position == 0:
                            self.file_selected = 0
                            self.icon_position = 0
                            pygame.display.update()
                            pygame.time.wait(50)
                        elif self.icon_position == 1:
                            self.file_selected = 1
                            self.icon_position = 0
                        elif self.icon_position == 2:
                            self.file_selected = 2
                            self.icon_position = 0
                    else:
                        if self.icon_position == 0:  # Start file
                            with open('advancing_hero/world/journey_save_files.json', 'w') as outfile:
                                aux = self.json_data
                                aux["current_file"][0] = self.file_selected
                                aux["current_hero"][0] = 0
                                aux["current_level"][0] = 0
                                json.dump(aux, outfile)
                            outfile.close()
                            pygame.time.wait(50)
                            pygame.event.post(
                                pygame.event.Event(pygame.USEREVENT, customType='character_select'))
                        elif self.icon_position == 1:  # Copy file
                            with open('advancing_hero/world/journey_save_files.json', 'w') as outfile:
                                aux = self.json_data  # CHANGE JSON AUX for permanent changes
                                if aux["saves"][0][0] == 0:
                                    aux["saves"][0] = aux["saves"][self.file_selected]
                                elif aux["saves"][1][0] == 0:
                                    aux["saves"][1] = aux["saves"][self.file_selected]
                                elif aux["saves"][2][0] == 0:
                                    aux["saves"][2] = aux["saves"][self.file_selected]
                                json.dump(aux, outfile)
                                self.save_files_data = aux["saves"]
                            outfile.close()
                            self.icon_position = 0
                            self.file_selected = -1
                        elif self.icon_position == 2:  # Erase file
                            with open('advancing_hero/world/journey_save_files.json', 'w') as outfile:
                                aux = self.json_data  # CHANGE JSON AUX for permanent changes
                                aux["saves"][self.file_selected] = [0, 0, [0, 0, 0]]
                                json.dump(aux, outfile)
                                self.save_files_data = aux["saves"]
                            outfile.close()
                            self.icon_position = 0
                            self.file_selected = -1
