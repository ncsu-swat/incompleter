# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46157257/pygame-choose-color-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(668962)

except ImportError:
    pass
_c_(668965, _a_(668964, _n_(668963, "pygame", lambda: pygame), "init"))
_l_(668966)
screen = _c_(668970, _a_(668969, _a_(668968, _n_(668967, "pygame", lambda: pygame), "display"), "set_mode"), (640,480))
_l_(668971)
_c_(668975, _a_(668974, _a_(668973, _n_(668972, "pygame", lambda: pygame), "display"), "set_caption"), "Snake")
_l_(668976)


gameExit = False
_l_(668977)
while not _n_(668978, "gameExit", lambda: gameExit):
    _l_(669000)

    for event in _c_(668982, _a_(668981, _a_(668980, _n_(668979, "pygame", lambda: pygame), "event"), "get")):
        _l_(668989)

        if _a_(668984, _n_(668983, "event", lambda: event), "type") == _a_(668986, _n_(668985, "pygame", lambda: pygame), "QUIT"):
            _l_(668988)

            gameExit = True
            _l_(668987)

    _c_(668993, _a_(668991, _n_(668990, "screen", lambda: screen), "fill"), _n_(668992, "white", lambda: white))
    _l_(668994)
    _c_(668998, _a_(668997, _a_(668996, _n_(668995, "pygame", lambda: pygame), "display"), "update"))
    _l_(668999)


_c_(669003, _a_(669002, _n_(669001, "pygame", lambda: pygame), "quit"))
_l_(669004)