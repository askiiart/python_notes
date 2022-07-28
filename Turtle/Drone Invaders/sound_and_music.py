import pygame
from pygame import mixer


class SoundAndMusic:
    laser_sound = 0
    explosion_sound = 0
    change_level_sound = 0
    music_volume = 0
    sfx_volume = 0
    game_lost_sound = 0
    game_won_sound = 0

    @staticmethod
    def start_pygame():
        # global laser_sound, explosion_sound, change_level_sound, music_volume, sfx_volume
        pygame.init()
        SoundAndMusic.laser_sound = 0.0
        SoundAndMusic.explosion_sound = 0.0
        SoundAndMusic.change_level_sound = 0.0
        SoundAndMusic.game_lost_sound = 0.0
        SoundAndMusic.game_won_sound = 0.0
        SoundAndMusic.music_volume = 5
        SoundAndMusic.sfx_volume = 10

    @staticmethod
    def load_music():
        # global music_volume
        mixer.music.load('sounds/mixed_themes.ogg')
        mixer.music.set_volume(SoundAndMusic.music_volume / 100)

    @staticmethod
    def play_music():
        mixer.music.play(loops=-1)

    @staticmethod
    def pause_music():
        mixer.music.pause()

    @staticmethod
    def unpause_music():
        mixer.music.unpause()

    @staticmethod
    def stop_music():
        mixer.music.stop()

    @staticmethod
    def load_sounds():
        # global sfx_volume, laser_sound, explosion_sound, change_level_sound
        SoundAndMusic.laser_sound = mixer.Sound('sounds/laser.wav')
        SoundAndMusic.laser_sound.set_volume(SoundAndMusic.sfx_volume / 100)
        SoundAndMusic.explosion_sound = mixer.Sound('sounds/explosion.wav')
        SoundAndMusic.explosion_sound.set_volume(SoundAndMusic.sfx_volume / 100)
        SoundAndMusic.change_level_sound = mixer.Sound('sounds/change_levels.wav')
        SoundAndMusic.change_level_sound.set_volume(SoundAndMusic.sfx_volume / 100)
        SoundAndMusic.game_lost_sound = mixer.Sound('sounds/game_lost_sound.wav')
        SoundAndMusic.game_lost_sound.set_volume(SoundAndMusic.sfx_volume / 100)
        SoundAndMusic.game_won_sound = mixer.Sound('sounds/game_won_sound.wav')
        SoundAndMusic.game_won_sound.set_volume(SoundAndMusic.sfx_volume / 100)

    @staticmethod
    def play_laser_sound():
        SoundAndMusic.laser_sound.play()

    @staticmethod
    def play_explosion_sound():
        SoundAndMusic.explosion_sound.play()

    @staticmethod
    def play_change_level_sound():
        SoundAndMusic.change_level_sound.play()

    @staticmethod
    def play_game_lost_sound():
        SoundAndMusic.game_lost_sound.play()

    @staticmethod
    def play_game_won_sound():
        SoundAndMusic.game_won_sound.play()

    @staticmethod
    def change_sfx_volume(delta_volume):
        # global laser_sound, explosion_sound, change_level_sound, sfx_volume
        SoundAndMusic.sfx_volume += delta_volume
        if SoundAndMusic.sfx_volume > 100:
            SoundAndMusic.sfx_volume = 100
        elif SoundAndMusic.sfx_volume < 0:
            SoundAndMusic.sfx_volume = 0
        SoundAndMusic.laser_sound.set_volume(SoundAndMusic.sfx_volume / 100)
        SoundAndMusic.explosion_sound.set_volume(SoundAndMusic.sfx_volume / 100)
        SoundAndMusic.change_level_sound.set_volume(SoundAndMusic.sfx_volume / 100)
        print(SoundAndMusic.sfx_volume)

    @staticmethod
    def change_music_volume(delta_volume):
        # global music_volume
        SoundAndMusic.music_volume += delta_volume
        if SoundAndMusic.music_volume > 100:
            SoundAndMusic.music_volume = 100
        elif SoundAndMusic.music_volume < 0:
            SoundAndMusic.music_volume = 0
        mixer.music.set_volume(SoundAndMusic.music_volume / 100)
        print(SoundAndMusic.music_volume)
