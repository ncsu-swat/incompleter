# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59475230/attributeerror-module-pygame-event-has-no-attribute-type
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(698851)

except ImportError:
    pass
try:
    from pygame import *
    _l_(698853)

except ImportError:
    pass
_c_(698856, _a_(698855, _n_(698854, "pygame", lambda: pygame), "init"))
_l_(698857)
WINDOW_WIDTH = 900
_l_(698858)
WINDOW_HEIGHT = 400
_l_(698859)
WINDOW_RES = (_n_(698860, "WINDOW_WIDTH", lambda: WINDOW_WIDTH), _n_(698861, "WINDOW_HEIGHT", lambda: WINDOW_HEIGHT))
_l_(698862)
GAME_WINDOW = _c_(698866, _a_(698864, _n_(698863, "display", lambda: display), "set_mode"), _n_(698865, "WINDOW_RES", lambda: WINDOW_RES))
_l_(698867)
_c_(698870, _a_(698869, _n_(698868, "display", lambda: display), "set_caption"), 'Attack of the Vampire Pizzas!')
_l_(698871)
game_running = True
_l_(698872)
while _n_(698873, "game_running", lambda: game_running):
    _l_(698888)

    for events in _c_(698877, _a_(698876, _a_(698875, _n_(698874, "pygame", lambda: pygame), "event"), "get")):
        _l_(698883)

        if _a_(698879, _n_(698878, "event", lambda: event), "type") == _n_(698880, "QUIT", lambda: QUIT):
            _l_(698882)

            game_running = False
            _l_(698881)

    _c_(698886, _a_(698885, _n_(698884, "display", lambda: display), "update"))
    _l_(698887)
_c_(698891, _a_(698890, _n_(698889, "pygame", lambda: pygame), "quit"))
_l_(698892)