# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63971808/attributeerror-int-object-has-no-attribute-after
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(370469)

except ImportError:
    pass
timer = 60
_l_(370470)
def startGame(event):
    _l_(370476)

    if _n_(370471, "timer", lambda: timer) == 60:
        _l_(370475)

        _c_(370473, _n_(370472, "countdown", lambda: countdown))
        _l_(370474)
def countdown():
    _l_(370494)

    global timer
    _l_(370477)
    if _n_(370478, "timer", lambda: timer) > 0:
        _l_(370493)

        timer -= 1
        _l_(370479)
        _c_(370485, _a_(370481, _n_(370480, "timeLabel", lambda: timeLabel), "config"), text='Time left:' + _c_(370484, _n_(370482, "str", lambda: str), _n_(370483, "timer", lambda: timer)))
        _l_(370486)
        _c_(370491, _a_(370488, _n_(370487, "timer", lambda: timer), "after"), 1000, _c_(370490, _n_(370489, "countdown", lambda: countdown)))
        _l_(370492)
window = _c_(370496, _n_(370495, "Tk", lambda: Tk))
_l_(370497)
timeLabel = _c_(370500, _n_(370498, "Label", lambda: Label), _n_(370499, "window", lambda: window), text='time = 60 sec')
_l_(370501)
entryBox = _c_(370504, _n_(370502, "Entry", lambda: Entry), _n_(370503, "window", lambda: window))
_l_(370505)
_c_(370508, _a_(370507, _n_(370506, "timeLabel", lambda: timeLabel), "pack"))
_l_(370509)
_c_(370512, _a_(370511, _n_(370510, "entryBox", lambda: entryBox), "pack"))
_l_(370513)
_c_(370517, _a_(370515, _n_(370514, "window", lambda: window), "bind"), '<Return>', _n_(370516, "startGame", lambda: startGame))
_l_(370518)
_a_(370520, _n_(370519, "entryBox", lambda: entryBox), "pack")
_l_(370521)
_c_(370524, _a_(370523, _n_(370522, "entryBox", lambda: entryBox), "focus_set"))
_l_(370525)
_c_(370528, _a_(370527, _n_(370526, "window", lambda: window), "mainloop"))
_l_(370529)