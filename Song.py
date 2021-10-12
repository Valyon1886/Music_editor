import pydub

class Song(object):
    """Class - wave-file init"""

    def __init__(self, path, begin_time, end_time):
        """Constructor"""
        self.path = path
        self.begin_time = begin_time
        self.end_time = end_time