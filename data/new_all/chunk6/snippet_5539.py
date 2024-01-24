# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63615461/how-to-fix-this-attributeerror-about-a-missing-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(347492)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(347494)

except ImportError:
    pass
try:
    from pygame import mixer
    _l_(347496)

except ImportError:
    pass


class MusicPlayer:
    _l_(347588)

    def __init__(self, window ):
        _l_(347548)

        _c_(347499, _a_(347498, _n_(347497, "window", lambda: window), "geometry"), '420x200'); _c_(347502, _a_(347501, _n_(347500, "window", lambda: window), "title"), 'MNote Player'); _c_(347505, _a_(347504, _n_(347503, "window", lambda: window), "resizable"), 0,0)
        _l_(347506)
        Load = _c_(347511, _n_(347507, "Button", lambda: Button), _n_(347508, "window", lambda: window), text = 'Load',  width = 10, font = ('Times', 10), command = _a_(347510, _n_(347509, "self", lambda: self), "load"))
        _l_(347512)
        Play = _c_(347517, _n_(347513, "Button", lambda: Button), _n_(347514, "window", lambda: window), text = 'Play',  width = 10,font = ('Times', 10), command = _a_(347516, _n_(347515, "self", lambda: self), "play"))
        _l_(347518)
        Pause = _c_(347523, _n_(347519, "Button", lambda: Button), _n_(347520, "window", lambda: window),text = 'Pause',  width = 10, font = ('Times', 10), command = _a_(347522, _n_(347521, "self", lambda: self), "pause"))
        _l_(347524)
        Stop = _c_(347529, _n_(347525, "Button", lambda: Button), _n_(347526, "window", lambda: window) ,text = 'Stop',  width = 10, font = ('Times', 10), command = _a_(347528, _n_(347527, "self", lambda: self), "stop"))
        _l_(347530)
        _c_(347533, _a_(347532, _n_(347531, "Load", lambda: Load), "place"), x=0,y=20);_c_(347536, _a_(347535, _n_(347534, "Play", lambda: Play), "place"), x=110,y=20);_c_(347539, _a_(347538, _n_(347537, "Pause", lambda: Pause), "place"), x=220,y=20);_c_(347542, _a_(347541, _n_(347540, "Stop", lambda: Stop), "place"), x=110,y=60) 
        _l_(347543) 
        _n_(347544, "self", lambda: self).music_file = False
        _l_(347545)
        _n_(347546, "self", lambda: self).playing_state = False
        _l_(347547)
    def load(self):
        _l_(347554)

        _n_(347549, "self", lambda: self).music_file = _c_(347552, _a_(347551, _n_(347550, "filedialog", lambda: filedialog), "askopenfilename"))
        _l_(347553)
    def play(self):
        _l_(347581)

        if _a_(347556, _n_(347555, "self", lambda: self), "music_file"):
            _l_(347580)

            _c_(347559, _a_(347558, _n_(347557, "mixer", lambda: mixer), "init"))
            _l_(347560)
            _c_(347566, _a_(347563, _a_(347562, _n_(347561, "mixer", lambda: mixer), "music"), "load"), _a_(347565, _n_(347564, "self", lambda: self), "music_file"))
            _l_(347567)
            _c_(347571, _a_(347570, _a_(347569, _n_(347568, "mixer", lambda: mixer), "music"), "play"))
            _l_(347572)
        else:
            _c_(347576, _a_(347575, _a_(347574, _n_(347573, "mixer", lambda: mixer), "music"), "unpause"))
            _l_(347577)
            _n_(347578, "self", lambda: self).playing_state = False
            _l_(347579)
    def stop(self):
        _l_(347587)

        _c_(347585, _a_(347584, _a_(347583, _n_(347582, "mixer", lambda: mixer), "music"), "stop"))
        _l_(347586)
root = _c_(347590, _n_(347589, "Tk", lambda: Tk))
_l_(347591)
app= _c_(347594, _n_(347592, "MusicPlayer", lambda: MusicPlayer), _n_(347593, "root", lambda: root))
_l_(347595)
_c_(347598, _a_(347597, _n_(347596, "root", lambda: root), "mainloop"))
_l_(347599)