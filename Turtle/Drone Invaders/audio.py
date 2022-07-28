import pygame
from pygame import mixer


class Audio:
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
        Audio.laser_sound = 0.0
        Audio.explosion_sound = 0.0
        Audio.change_level_sound = 0.0
        Audio.game_lost_sound = 0.0
        Audio.game_won_sound = 0.0
        Audio.music_volume = 5
        Audio.sfx_volume = 10

    @staticmethod
    def load_music():
        # global music_volume
        mixer.music.load('sounds/mixed_themes.ogg')
        mixer.music.set_volume(Audio.music_volume / 100)

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
        Audio.laser_sound = mixer.Sound('sounds/laser.wav')
        Audio.laser_sound.set_volume(Audio.sfx_volume / 100)
        Audio.explosion_sound = mixer.Sound('sounds/explosion.wav')
        Audio.explosion_sound.set_volume(Audio.sfx_volume / 100)
        Audio.change_level_sound = mixer.Sound('sounds/change_levels.wav')
        Audio.change_level_sound.set_volume(Audio.sfx_volume / 100)
        Audio.game_lost_sound = mixer.Sound('sounds/game_lost_sound.wav')
        Audio.game_lost_sound.set_volume(Audio.sfx_volume / 100)
        Audio.game_won_sound = mixer.Sound('sounds/game_won_sound.wav')
        Audio.game_won_sound.set_volume(Audio.sfx_volume / 100)

    @staticmethod
    def play_laser_sound():
        Audio.laser_sound.play()

    @staticmethod
    def play_explosion_sound():
        Audio.explosion_sound.play()

    @staticmethod
    def play_change_level_sound():
        Audio.change_level_sound.play()

    @staticmethod
    def play_game_lost_sound():
        Audio.game_lost_sound.play()

    @staticmethod
    def play_game_won_sound():
        Audio.game_won_sound.play()

    @staticmethod
    def change_sfx_volume(delta_volume):
        # global laser_sound, explosion_sound, change_level_sound, sfx_volume
        Audio.sfx_volume += delta_volume
        if Audio.sfx_volume > 100:
            Audio.sfx_volume = 100
        elif Audio.sfx_volume < 0:
            Audio.sfx_volume = 0
        Audio.laser_sound.set_volume(Audio.sfx_volume / 100)
        Audio.explosion_sound.set_volume(Audio.sfx_volume / 100)
        Audio.change_level_sound.set_volume(Audio.sfx_volume / 100)
        print(Audio.sfx_volume)

    @staticmethod
    def change_music_volume(delta_volume):
        # global music_volume
        Audio.music_volume += delta_volume
        if Audio.music_volume > 100:
            Audio.music_volume = 100
        elif Audio.music_volume < 0:
            Audio.music_volume = 0
        mixer.music.set_volume(Audio.music_volume / 100)
        print(Audio.music_volume)
