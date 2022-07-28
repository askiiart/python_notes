from droneinvaders import DroneInvaders
from audio import Audio

Audio.start_pygame()
Audio.load_music()
Audio.play_music()
Audio.load_sounds()

if __name__ == '__main__':
    di = DroneInvaders(-1, 1, -1, 1)
    di.play()
