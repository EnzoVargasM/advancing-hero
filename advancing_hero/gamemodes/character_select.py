from .gamemode import GameMode
import pygame
import pygame.freetype
import os
import json

'''Ideas for different heros:
Mage who load FIRE BALL to GROW infinitely and infinite cooldown
Tank who is big and slow and has big shield, attack near
Fast Monk who do not attack but is rodiated by balls of power
Spirited away warrior, his spirit is the one who attack and is faster but do not take damage. Ability to pull spirit
Bomber who can trow bombs in any direction with mouse click 
Healer who trows heal like an arrow and heal/damage a circle around ability 2
'''


class CharacterSelectScreen(GameMode):
    def __init__(self, screen, settings):
        super().__init__(screen)
        self.settings = settings
        self.game_title = pygame.freetype.Font(self.font_path, 50)
        self.background_image = pygame.transform.scale(
            pygame.image.load(
                os.path.abspath('advancing_hero/images/backgrounds/TitleScreen.png')),
            self.settings.SIZE)
        self.selection_icon = pygame.transform.scale(
            pygame.image.load(
                os.path.abspath('advancing_hero/images/select_icon.png')),
            (40, 40))
        self.menu_font = pygame.freetype.Font(self.font_path, 25)
        self.commands_font = pygame.freetype.Font(self.font_path, 15)
        self.icon_position = 0
        self.music_path = os.path.abspath('advancing_hero/musics/sawsquarenoise-Stage3.ogg')
        self.hero_list = [
            pygame.transform.scale(
                pygame.image.load(
                    os.path.abspath('advancing_hero/images/sprites/player/frame2.png')),
                (50, 80)),
            pygame.transform.scale(
                pygame.image.load(
                    os.path.abspath('advancing_hero/images/sprites/player2/frame2.png')),
                (50, 80)),
            pygame.transform.scale(
                pygame.image.load(
                    os.path.abspath('advancing_hero/images/sprites/player3/frame2.png')),
                (50, 80))
        ]
        self.tick = 0  # artificial timer
        self.icon_frame = 12  # Keep control of frame changes
        with open('advancing_hero/world/journey_save_files.json') as save_files:
            self.json_data = json.load(save_files)
        save_files.close()

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_path)
        pygame.music.play(-1)

    def loop(self, events):
        self.screen.blit(self.background_image, (0, 0))
        self.game_title.render_to(self.screen,
                                  (self.settings.screen_width / 2 - 350,
                                   self.settings.screen_height / 2 - 256),
                                  "Select Your Hero", self.settings.BLACK)


        self.commands_font.render_to(self.screen,
                                 (10, self.settings.screen_height - 30),
                                 "SPACE or ENTER: ENTER   W or UP: UP   S or DOWN: DOWN",
                                 self.settings.BLACK)

        for i in range(len(self.hero_list)):
            self.screen.blit(
                self.hero_list[i],
                (self.settings.screen_width / 2 - 150,
                 self.settings.screen_height / 2 - 170 + i * 80))
            self.menu_font.render_to(self.screen,
                                     (self.settings.screen_width / 2 - 350,
                                      self.settings.screen_height / 2 - 150 + i * 80),
                                     f"Class {i+1}", self.settings.BLACK)

        self.screen.blit(
            self.selection_icon,
            (self.settings.screen_width / 2 - 400,
             self.settings.screen_height / 2 - 150 + self.icon_position * 80))

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
        self.selection_icon2 = pygame.transform.scale(
            pygame.image.load(
                os.path.abspath(f'advancing_hero/images/sprites/player/frame{int(self.icon_frame / 10)}.png')),
            (100, 160))
        self.screen.blit(
            self.selection_icon2,
            (600, 300))

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if self.icon_position > 0:
                        self.icon_position = self.icon_position - 1
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if self.icon_position < len(self.hero_list)-1:
                        self.icon_position = self.icon_position + 1
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if 0 <= self.icon_position <= 2:
                        # Update current hero in global database
                        with open('advancing_hero/world/journey_save_files.json', 'w') as outfile:
                            aux = self.json_data
                            aux["current_hero"][0] = self.icon_position
                            json.dump(aux, outfile)
                        outfile.close()
                        pygame.time.wait(150)
                        pygame.event.post(
                            pygame.event.Event(pygame.USEREVENT,
                                               customType='world_map'))
                if event.key == pygame.K_ESCAPE:
                    pygame.time.wait(150)
                    pygame.event.post(
                        pygame.event.Event(pygame.USEREVENT,
                                           customType='journey_select'))
