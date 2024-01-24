# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41974709/typeerror-module-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(684479)

except ImportError:
    pass
try:
    from settings import *
    _l_(684481)

except ImportError:
    pass
try:
    from loading import *
    _l_(684483)

except ImportError:
    pass

class game():
    _l_(684563)

    def __init__(self):
        _l_(684506)

        _n_(684484, "self", lambda: self).screen = _c_(684490, _a_(684487, _a_(684486, _n_(684485, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(684488, "displayWidth", lambda: displayWidth), _n_(684489, "displayHeight", lambda: displayHeight)))
        _l_(684491)
        _c_(684496, _a_(684494, _a_(684493, _n_(684492, "pygame", lambda: pygame), "display"), "set_caption"), _n_(684495, "title", lambda: title))
        _l_(684497)
        _n_(684498, "self", lambda: self).clock = _c_(684502, _a_(684501, _a_(684500, _n_(684499, "pygame", lambda: pygame), "time"), "Clock"))
        _l_(684503)
        _n_(684504, "self", lambda: self).gameRunning = True
        _l_(684505)

    def loop(self):
        _l_(684519)

        for event in _c_(684510, _a_(684509, _a_(684508, _n_(684507, "pygame", lambda: pygame), "event"), "get")):
            _l_(684518)

            if _a_(684512, _n_(684511, "event", lambda: event), "type") == _a_(684514, _n_(684513, "pygame", lambda: pygame), "QUIT"):
                _l_(684517)

                _n_(684515, "self", lambda: self).gameRunning = False
                _l_(684516)

    def gameLoop(self):
        _l_(684538)

        _c_(684524, _a_(684522, _a_(684521, _n_(684520, "self", lambda: self), "clock"), "tick"), _n_(684523, "fps", lambda: fps))
        _l_(684525)
        _c_(684528, _a_(684527, _n_(684526, "self", lambda: self), "loop"))
        _l_(684529)
        _c_(684532, _a_(684531, _n_(684530, "self", lambda: self), "loadMap"))
        _l_(684533)
        _c_(684536, _a_(684535, _n_(684534, "self", lambda: self), "editScreen"))
        _l_(684537)

    def editScreen(self):
        _l_(684551)

        _c_(684544, _a_(684541, _a_(684540, _n_(684539, "self", lambda: self), "screen"), "blit"), _a_(684543, _n_(684542, "self", lambda: self), "map_img"), (0,0))
        _l_(684545)
        _c_(684549, _a_(684548, _a_(684547, _n_(684546, "pygame", lambda: pygame), "display"), "update"))
        _l_(684550)

    def loadMap(self):
        _l_(684562)

        _n_(684552, "self", lambda: self).map = _c_(684554, _n_(684553, "tiledMap", lambda: tiledMap))
        _l_(684555)
        _n_(684556, "self", lambda: self).map_img = _c_(684560, _a_(684559, _a_(684558, _n_(684557, "self", lambda: self), "map"), "makeSurface"))
        _l_(684561)

playGame = _c_(684565, _n_(684564, "game", lambda: game))
_l_(684566)
while _a_(684568, _n_(684567, "playGame", lambda: playGame), "gameRunning") == True:
    _l_(684573)

    _c_(684571, _a_(684570, _n_(684569, "playGame", lambda: playGame), "gameLoop"))
    _l_(684572)