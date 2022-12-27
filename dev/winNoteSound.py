import winsound

class noteSound:
    def __init__(self, note):
        filename = str(note + ".wav")
        winsound.PlaySound(filename, winsound.SND_FILENAME)
