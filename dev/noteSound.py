# Plays a sound from a file given a note(str) on various operating systems
# Author: Sequoia Pflug
# Original Version: 12-26-2022

from sys import platform

class noteSound:
    def __init__(self, note):
        if platform == "linux" or platform == "linux2" or platform == "darwin":
            import StdAudio
            StdAudio.playFile("../sounds/" + note)

        elif platform == "win32":
            import winsound
            filename = str("../sounds/" + note + ".wav")
            winsound.PlaySound(filename, winsound.SND_FILENAME)
