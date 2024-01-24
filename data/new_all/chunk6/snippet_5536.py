# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63971808/attributeerror-int-object-has-no-attribute-after
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(341984)

except ImportError:
    pass
timer = 60
_l_(341985)
def startGame(event):
    _l_(341991)

    if _n_(341986, "timer", lambda: timer) == 60:
        _l_(341990)

        _c_(341988, _n_(341987, "countdown", lambda: countdown))
        _l_(341989)
def countdown():
    _l_(342009)

    global timer
    _l_(341992)
    if _n_(341993, "timer", lambda: timer) > 0:
        _l_(342008)

        timer -= 1
        _l_(341994)
        _c_(342000, _a_(341996, _n_(341995, "timeLabel", lambda: timeLabel), "config"), text='Time left:' + _c_(341999, _n_(341997, "str", lambda: str), _n_(341998, "timer", lambda: timer)))
        _l_(342001)
        _c_(342006, _a_(342003, _n_(342002, "timer", lambda: timer), "after"), 1000, _c_(342005, _n_(342004, "countdown", lambda: countdown)))
        _l_(342007)
window = _c_(342011, _n_(342010, "Tk", lambda: Tk))
_l_(342012)
timeLabel = _c_(342015, _n_(342013, "Label", lambda: Label), _n_(342014, "window", lambda: window), text='time = 60 sec')
_l_(342016)
entryBox = _c_(342019, _n_(342017, "Entry", lambda: Entry), _n_(342018, "window", lambda: window))
_l_(342020)
_c_(342023, _a_(342022, _n_(342021, "timeLabel", lambda: timeLabel), "pack"))
_l_(342024)
_c_(342027, _a_(342026, _n_(342025, "entryBox", lambda: entryBox), "pack"))
_l_(342028)
_c_(342032, _a_(342030, _n_(342029, "window", lambda: window), "bind"), '<Return>', _n_(342031, "startGame", lambda: startGame))
_l_(342033)
_a_(342035, _n_(342034, "entryBox", lambda: entryBox), "pack")
_l_(342036)
_c_(342039, _a_(342038, _n_(342037, "entryBox", lambda: entryBox), "focus_set"))
_l_(342040)
_c_(342043, _a_(342042, _n_(342041, "window", lambda: window), "mainloop"))
_l_(342044)