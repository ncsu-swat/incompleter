# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/26673926/attributeerror-object-has-no-attribute-velx
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame,sys
    _l_(356614)

except ImportError:
    pass
try:
    from classes import *
    _l_(356616)

except ImportError:
    pass

_c_(356619, _a_(356618, _n_(356617, "pygame", lambda: pygame), "init"))
_l_(356620)
WIDTH,HEIGHT = 640, 360
_l_(356621)
screen = _c_(356627, _a_(356624, _a_(356623, _n_(356622, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(356625, "WIDTH", lambda: WIDTH),_n_(356626, "HEIGHT", lambda: HEIGHT)),0,32)
_l_(356628)
img_pokemon = _c_(356632, _a_(356631, _a_(356630, _n_(356629, "pygame", lambda: pygame), "image"), "load"), "pokemon.png")
_l_(356633)

#colours
clr1 = (22,122,211)
_l_(356634)
clr2 = (0,44,166)
_l_(356635)
clr3 = (34,55,245)
_l_(356636)
clrvar = 1
_l_(356637)
spritemovex = 1
_l_(356638)
spritemovey = 1
_l_(356639)

#clock
clock = _c_(356643, _a_(356642, _a_(356641, _n_(356640, "pygame", lambda: pygame), "time"), "Clock"))
_l_(356644)
FPS = 24
_l_(356645)
fivesecondinterval = _n_(356646, "FPS", lambda: FPS) * 5
_l_(356647)
totalframes = 0
_l_(356648)

pokemon = _c_(356650, _n_(356649, "Pokemon", lambda: Pokemon), 0, 100, 40, 30, "pokemon.png")
_l_(356651)

while True:
    _l_(356713)

    #processes
    for event in _c_(356655, _a_(356654, _a_(356653, _n_(356652, "pygame", lambda: pygame), "event"), "get")):
        _l_(356669)

        if _a_(356657, _n_(356656, "event", lambda: event), "type") == _a_(356659, _n_(356658, "pygame", lambda: pygame), "QUIT"):
            _l_(356668)

            _c_(356662, _a_(356661, _n_(356660, "pygame", lambda: pygame), "quit"))
            _l_(356663)
            _c_(356666, _a_(356665, _n_(356664, "sys", lambda: sys), "exit"))
            _l_(356667)

    _c_(356673, _a_(356672, _a_(356671, _n_(356670, "pygame", lambda: pygame), "display"), "flip"))
    _l_(356674)

    _c_(356678, _a_(356676, _n_(356675, "clock", lambda: clock), "tick"), _n_(356677, "FPS", lambda: FPS))
    _l_(356679)

    #logic
    _c_(356682, _a_(356681, _n_(356680, "pokemon", lambda: pokemon), "motion"))
    _l_(356683)

    totalframes += 1
    _l_(356684)
    clrvar +=3
    _l_(356685)
    if _n_(356686, "clrvar", lambda: clrvar) > 255:
        _l_(356688)

        clrvar = 1
        _l_(356687)

    spritemovex += 2
    _l_(356689)
    spritemovey += 2
    _l_(356690)
    if _n_(356691, "spritemovex", lambda: spritemovex) > _n_(356692, "WIDTH", lambda: WIDTH):
        _l_(356695)

        spritemovex %= _n_(356693, "WIDTH", lambda: WIDTH)
        _l_(356694)
    if _n_(356696, "spritemovey", lambda: spritemovey) > _n_(356697, "HEIGHT", lambda: HEIGHT):
        _l_(356700)

        spritemovey %= _n_(356698, "HEIGHT", lambda: HEIGHT)
        _l_(356699)
    #draw
    _c_(356704, _a_(356702, _n_(356701, "screen", lambda: screen), "fill"), (90,_n_(356703, "clrvar", lambda: clrvar),180) )
    _l_(356705)
    _c_(356711, _a_(356707, _n_(356706, "screen", lambda: screen), "blit"), _n_(356708, "img_pokemon", lambda: img_pokemon), (_n_(356709, "spritemovex", lambda: spritemovex),_n_(356710, "spritemovey", lambda: spritemovey)))
    _l_(356712)