# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63615461/how-to-fix-this-attributeerror-about-a-missing-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(367521)

except ImportError:
    pass
try:
    from tkinter import filedialog
    _l_(367523)

except ImportError:
    pass
try:
    from pygame import mixer
    _l_(367525)

except ImportError:
    pass


class MusicPlayer:
    _l_(367617)

    def __init__(self, window ):
        _l_(367577)

        _c_(367528, _a_(367527, _n_(367526, "window", lambda: window), "geometry"), '420x200'); _c_(367531, _a_(367530, _n_(367529, "window", lambda: window), "title"), 'MNote Player'); _c_(367534, _a_(367533, _n_(367532, "window", lambda: window), "resizable"), 0,0)
        _l_(367535)
        Load = _c_(367540, _n_(367536, "Button", lambda: Button), _n_(367537, "window", lambda: window), text = 'Load',  width = 10, font = ('Times', 10), command = _a_(367539, _n_(367538, "self", lambda: self), "load"))
        _l_(367541)
        Play = _c_(367546, _n_(367542, "Button", lambda: Button), _n_(367543, "window", lambda: window), text = 'Play',  width = 10,font = ('Times', 10), command = _a_(367545, _n_(367544, "self", lambda: self), "play"))
        _l_(367547)
        Pause = _c_(367552, _n_(367548, "Button", lambda: Button), _n_(367549, "window", lambda: window),text = 'Pause',  width = 10, font = ('Times', 10), command = _a_(367551, _n_(367550, "self", lambda: self), "pause"))
        _l_(367553)
        Stop = _c_(367558, _n_(367554, "Button", lambda: Button), _n_(367555, "window", lambda: window) ,text = 'Stop',  width = 10, font = ('Times', 10), command = _a_(367557, _n_(367556, "self", lambda: self), "stop"))
        _l_(367559)
        _c_(367562, _a_(367561, _n_(367560, "Load", lambda: Load), "place"), x=0,y=20);_c_(367565, _a_(367564, _n_(367563, "Play", lambda: Play), "place"), x=110,y=20);_c_(367568, _a_(367567, _n_(367566, "Pause", lambda: Pause), "place"), x=220,y=20);_c_(367571, _a_(367570, _n_(367569, "Stop", lambda: Stop), "place"), x=110,y=60) 
        _l_(367572) 
        _n_(367573, "self", lambda: self).music_file = False
        _l_(367574)
        _n_(367575, "self", lambda: self).playing_state = False
        _l_(367576)
    def load(self):
        _l_(367583)

        _n_(367578, "self", lambda: self).music_file = _c_(367581, _a_(367580, _n_(367579, "filedialog", lambda: filedialog), "askopenfilename"))
        _l_(367582)
    def play(self):
        _l_(367610)

        if _a_(367585, _n_(367584, "self", lambda: self), "music_file"):
            _l_(367609)

            _c_(367588, _a_(367587, _n_(367586, "mixer", lambda: mixer), "init"))
            _l_(367589)
            _c_(367595, _a_(367592, _a_(367591, _n_(367590, "mixer", lambda: mixer), "music"), "load"), _a_(367594, _n_(367593, "self", lambda: self), "music_file"))
            _l_(367596)
            _c_(367600, _a_(367599, _a_(367598, _n_(367597, "mixer", lambda: mixer), "music"), "play"))
            _l_(367601)
        else:
            _c_(367605, _a_(367604, _a_(367603, _n_(367602, "mixer", lambda: mixer), "music"), "unpause"))
            _l_(367606)
            _n_(367607, "self", lambda: self).playing_state = False
            _l_(367608)
    def stop(self):
        _l_(367616)

        _c_(367614, _a_(367613, _a_(367612, _n_(367611, "mixer", lambda: mixer), "music"), "stop"))
        _l_(367615)
root = _c_(367619, _n_(367618, "Tk", lambda: Tk))
_l_(367620)
app= _c_(367623, _n_(367621, "MusicPlayer", lambda: MusicPlayer), _n_(367622, "root", lambda: root))
_l_(367624)
_c_(367627, _a_(367626, _n_(367625, "root", lambda: root), "mainloop"))
_l_(367628)