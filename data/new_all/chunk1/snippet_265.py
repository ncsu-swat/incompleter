# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/11825053/pygame-typeerror-int-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(377680)

except ImportError:
    pass
try:
    import sys
    _l_(377682)

except ImportError:
    pass

_c_(377685, _a_(377684, _n_(377683, "pygame", lambda: pygame), "init"))
_l_(377686)
screen = _c_(377690, _a_(377689, _a_(377688, _n_(377687, "pygame", lambda: pygame), "display"), "set_mode"), (600,400))
_l_(377691)
bg = _c_(377695, _a_(377694, _a_(377693, _n_(377692, "pygame", lambda: pygame), "image"), "load"), 'bg.jpg')
_l_(377696)
player = _c_(377700, _a_(377699, _a_(377698, _n_(377697, "pygame", lambda: pygame), "image"), "load"), 'player.jpg')
_l_(377701)
pos = _c_(377704, _a_(377703, _n_(377702, "player", lambda: player), "get_rect"))
_l_(377705)

while True:
    _l_(377738)

    for i in _c_(377709, _a_(377708, _a_(377707, _n_(377706, "pygame", lambda: pygame), "event"), "get")):
        _l_(377720)

        if _c_(377712, _a_(377711, _n_(377710, "i", lambda: i), "type")) == _a_(377714, _n_(377713, "pygame", lambda: pygame), "QUIT"):
            _l_(377719)

            _c_(377717, _a_(377716, _n_(377715, "sys", lambda: sys), "exit"))
            _l_(377718)
    _c_(377724, _a_(377722, _n_(377721, "screen", lambda: screen), "blit"), _n_(377723, "bg", lambda: bg),(0,0))
    _l_(377725)
    _c_(377731, _a_(377727, _n_(377726, "screen", lambda: screen), "blit"), _n_(377728, "player", lambda: player),(_n_(377729, "i", lambda: i),_n_(377730, "i", lambda: i)))
    _l_(377732)
    _c_(377736, _a_(377735, _a_(377734, _n_(377733, "pygame", lambda: pygame), "display"), "update"))
    _l_(377737)