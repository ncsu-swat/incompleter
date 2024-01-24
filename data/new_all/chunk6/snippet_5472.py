# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/26673926/attributeerror-object-has-no-attribute-velx
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame,sys
    _l_(344292)

except ImportError:
    pass
try:
    from classes import *
    _l_(344294)

except ImportError:
    pass

_c_(344297, _a_(344296, _n_(344295, "pygame", lambda: pygame), "init"))
_l_(344298)
WIDTH,HEIGHT = 640, 360
_l_(344299)
screen = _c_(344305, _a_(344302, _a_(344301, _n_(344300, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(344303, "WIDTH", lambda: WIDTH),_n_(344304, "HEIGHT", lambda: HEIGHT)),0,32)
_l_(344306)
img_pokemon = _c_(344310, _a_(344309, _a_(344308, _n_(344307, "pygame", lambda: pygame), "image"), "load"), "pokemon.png")
_l_(344311)

#colours
clr1 = (22,122,211)
_l_(344312)
clr2 = (0,44,166)
_l_(344313)
clr3 = (34,55,245)
_l_(344314)
clrvar = 1
_l_(344315)
spritemovex = 1
_l_(344316)
spritemovey = 1
_l_(344317)

#clock
clock = _c_(344321, _a_(344320, _a_(344319, _n_(344318, "pygame", lambda: pygame), "time"), "Clock"))
_l_(344322)
FPS = 24
_l_(344323)
fivesecondinterval = _n_(344324, "FPS", lambda: FPS) * 5
_l_(344325)
totalframes = 0
_l_(344326)

pokemon = _c_(344328, _n_(344327, "Pokemon", lambda: Pokemon), 0, 100, 40, 30, "pokemon.png")
_l_(344329)

while True:
    _l_(344391)

    #processes
    for event in _c_(344333, _a_(344332, _a_(344331, _n_(344330, "pygame", lambda: pygame), "event"), "get")):
        _l_(344347)

        if _a_(344335, _n_(344334, "event", lambda: event), "type") == _a_(344337, _n_(344336, "pygame", lambda: pygame), "QUIT"):
            _l_(344346)

            _c_(344340, _a_(344339, _n_(344338, "pygame", lambda: pygame), "quit"))
            _l_(344341)
            _c_(344344, _a_(344343, _n_(344342, "sys", lambda: sys), "exit"))
            _l_(344345)

    _c_(344351, _a_(344350, _a_(344349, _n_(344348, "pygame", lambda: pygame), "display"), "flip"))
    _l_(344352)

    _c_(344356, _a_(344354, _n_(344353, "clock", lambda: clock), "tick"), _n_(344355, "FPS", lambda: FPS))
    _l_(344357)

    #logic
    _c_(344360, _a_(344359, _n_(344358, "pokemon", lambda: pokemon), "motion"))
    _l_(344361)

    totalframes += 1
    _l_(344362)
    clrvar +=3
    _l_(344363)
    if _n_(344364, "clrvar", lambda: clrvar) > 255:
        _l_(344366)

        clrvar = 1
        _l_(344365)

    spritemovex += 2
    _l_(344367)
    spritemovey += 2
    _l_(344368)
    if _n_(344369, "spritemovex", lambda: spritemovex) > _n_(344370, "WIDTH", lambda: WIDTH):
        _l_(344373)

        spritemovex %= _n_(344371, "WIDTH", lambda: WIDTH)
        _l_(344372)
    if _n_(344374, "spritemovey", lambda: spritemovey) > _n_(344375, "HEIGHT", lambda: HEIGHT):
        _l_(344378)

        spritemovey %= _n_(344376, "HEIGHT", lambda: HEIGHT)
        _l_(344377)
    #draw
    _c_(344382, _a_(344380, _n_(344379, "screen", lambda: screen), "fill"), (90,_n_(344381, "clrvar", lambda: clrvar),180) )
    _l_(344383)
    _c_(344389, _a_(344385, _n_(344384, "screen", lambda: screen), "blit"), _n_(344386, "img_pokemon", lambda: img_pokemon), (_n_(344387, "spritemovex", lambda: spritemovex),_n_(344388, "spritemovey", lambda: spritemovey)))
    _l_(344390)