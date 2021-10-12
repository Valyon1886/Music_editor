from pydub import AudioSegment


class Sound(object):
    """Class - wave-file init"""
    def __init__(self, path, begin_time, end_time):
        """Constructor"""
        self.path = path
        self.begin_time = begin_time
        self.end_time = end_time


    def __add__(self, other):
        """a+b=simple"""
        sound1 = AudioSegment.from_wav(self.path)
        sound2 = AudioSegment.from_wav(other.path)
        sound1 = sound1[int(self.begin_time)*1000:int(self.end_time)*1000]
        sound2 = sound2[int(other.begin_time)*1000:int(other.end_time)*1000]
        return  sound1 + sound2
