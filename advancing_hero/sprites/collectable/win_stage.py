import os
from ..sprite import Sprite
import pygame
import json


class WinStage(Sprite):
    """
    Represents a the element in the end of Stage to complete stage
    """
    def __init__(
        self,
        position,
        screen,
        path: str = 'advancing_hero/images/sprites/win_stage/',
    ) -> None:
        super().__init__(path=os.path.abspath(path), position=position)

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.position = position
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.music_path = os.path.abspath('advancing_hero/songs/item.wav')
        self.screen = screen
        with open('advancing_hero/world/journey_save_files.json') as save_files:
            self.json_data = json.load(save_files)
        save_files.close()

    def update(self, player, stage):
        super().update()
        self.rect.y += stage.scroll_amount
        self.player_collision(player)
        if self.rect.colliderect(self.screen.get_rect()) == 0:
            self.kill()
        for tile in stage.tile_list:
            if tile[1].bottom > 0 and tile[
                    1].top < stage.settings.screen_height and tile[2].is_solid:
                if tile[1].colliderect(self.rect):
                    self.kill()

    def player_collision(self, player):
        if self.rect.colliderect(player.rect):
            player.image = player.image_list[7]
            if self.frame_counter % 30 == 0:
                # self.play_music()
                self.image_frame = (self.image_frame + 1) % len(self.image_list)
                self.image = self.image_list[self.image_frame]
            if self.frame_counter % 60 == 0:
                # Save in database this stage was cleared
                aux = self.json_data
                if aux["saves"][aux["current_file"][0]][2][aux["current_hero"][0]] != 9:  # is not last stage
                    if aux["current_level"][0] == aux["saves"][aux["current_file"][0]][2][aux["current_hero"][0]] - 1:
                        aux["saves"][aux["current_file"][0]][2][aux["current_hero"][0]] = aux["current_level"][0] + 2
                        with open('advancing_hero/world/journey_save_files.json', 'w') as outfile:
                            json.dump(aux, outfile)
                        outfile.close()

                pygame.event.post(pygame.event.Event(pygame.USEREVENT, customType='world_map'))

    def play_music(self):
        sound = pygame.mixer.Sound(self.music_path)
        sound.set_volume(0.4)
        pygame.mixer.Channel(4).play(sound)
