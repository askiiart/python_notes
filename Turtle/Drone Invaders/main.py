from droneinvaders import DroneInvaders
from sound_and_music import SoundAndMusic

SoundAndMusic.start_pygame()
SoundAndMusic.load_music()
SoundAndMusic.play_music()
SoundAndMusic.load_sounds()

if __name__ == '__main__':
    di = DroneInvaders(-1, 1, -1, 1)
    di.play()
