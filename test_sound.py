from Song import Sound

def test_sound__init__():
   a1 = Sound(r'C:\Users\Valentin\Music\1.wav', 1, 3)
   assert a1

def test__add__():
   a1 = Sound(r'C:\Users\Valentin\Music\1.wav', 0, 3)
   a2 = Sound(r'C:\Users\Valentin\Music\2.wav', 0, 4)
   assert (a1+a2).duration_seconds == 7.0
