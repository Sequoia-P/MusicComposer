import StdAudio

class noteSound:
    def __init__(self, note):
        StdAudio.playFile("../sounds/" + note)
