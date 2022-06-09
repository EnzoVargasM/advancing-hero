from .gamemode import GameMode
from advancing_hero.world import World
from advancing_hero.sprites import Player, PlayerMonk, PlayerMage
import pygame
import os
import json


class LevelGameMode(GameMode):
    def __init__(self, screen, level_file, settings, scroll_mode="Down"):
        super().__init__(screen)
        self.level_file = level_file
        self.settings = settings
        self.stage = World(settings, self.level_file, screen, scroll_mode)
        # Load specific type of Player
        with open('advancing_hero/world/journey_save_files.json') as save_files:
            self.json_data = json.load(save_files)
        save_files.close()
        if self.json_data["current_hero"][0] == 0:
            self.player1 = Player((512, 288), settings, self.stage, self.screen)
        elif self.json_data["current_hero"][0] == 1:
            self.player1 = PlayerMage((512, 288), settings, self.stage, self.screen)
        elif self.json_data["current_hero"][0] == 2:
            self.player1 = PlayerMonk((512, 288), settings, self.stage, self.screen)
        #self.player2 = Player2((612, 288), settings, self.stage, self.screen)
        self.helper_font = pygame.freetype.Font(self.font_path, 23)
        self.game_state = "Running"
        self.selection_icon = pygame.transform.scale(
            pygame.image.load(
                os.path.abspath('advancing_hero/images/select_icon.png')),
            (40, 40))
        self.icon_position = 0

    def loop(self, events):
        if self.game_state == "Running":
            self.stage.update(self.screen, self.player1)
            self.player1.draw()
            #self.player2.draw()
            self.player1.update()
            #self.player2.update(self.player1)
            # Changing State to Paused if ESC pressed
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_state = "Pause"
        if self.game_state == "Pause":
            self.stage.paused_drawing(self.screen)
            self.player1.draw()
            # Print Information PAUSE Menu
            self.helper_font.render_to(
                self.screen, (5, self.settings.screen_height - 30),
                "WASD:P1 MOVEMENT     C:ATTACK     V:CHANGE WEAPON",
                self.settings.BLACK)
            menu_options = ["Resume Game", "Return World Map", "Return Initial Menu", "Quit Game"]
            for i in range(0, 4):
                self.helper_font.render_to(self.screen,
                                         (self.settings.screen_width / 2 - 160,
                                          self.settings.screen_height / 2 - 100 + 50 * i),
                                         menu_options[i], self.settings.BLACK)
            self.screen.blit(
                self.selection_icon,
                (self.settings.screen_width / 2 - 210,
                 self.settings.screen_height / 2 - 110 + self.icon_position * 50))
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if self.icon_position > 0:
                            self.icon_position = (self.icon_position - 1) % 4
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if self.icon_position < 3:
                            self.icon_position = (self.icon_position + 1) % 4
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        if self.icon_position == 0:
                            self.game_state = "Running"
                        elif self.icon_position == 1:
                            pygame.time.wait(150)
                            # Change ost
                            ost = os.path.abspath('advancing_hero/songs/title_screen_song.mp3')
                            pygame.mixer.music.load(ost)
                            pygame.mixer.music.set_volume(0.7)
                            pygame.mixer.music.play(-1)

                            pygame.event.post(pygame.event.Event(pygame.USEREVENT, customType='world_map'))
                        elif self.icon_position == 2:
                            pygame.time.wait(150)
                            pygame.event.post(
                                pygame.event.Event(pygame.USEREVENT, customType='title_screen'))
                        elif self.icon_position == 3:
                            pygame.time.wait(150)
                            pygame.event.post(pygame.event.Event(pygame.QUIT))


