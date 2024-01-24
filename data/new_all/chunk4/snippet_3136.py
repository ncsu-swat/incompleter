# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41909280/gamedisplay-fillwhite-nameerror-name-white-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(619390)

except ImportError:
    pass

_c_(619393, _a_(619392, _n_(619391, "pygame", lambda: pygame), "init"))
_l_(619394)

display_width = 800
_l_(619395)
display_height = 600
_l_(619396)

gameDisplay = _c_(619402, _a_(619399, _a_(619398, _n_(619397, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(619400, "display_width", lambda: display_width),_n_(619401, "display_height", lambda: display_height)))
_l_(619403)
_c_(619407, _a_(619406, _a_(619405, _n_(619404, "pygame", lambda: pygame), "display"), "set_caption"), 'Ninja Game')
_l_(619408)
clock = _c_(619412, _a_(619411, _a_(619410, _n_(619409, "pygame", lambda: pygame), "time"), "Clock"))
_l_(619413)

carImg = _c_(619417, _a_(619416, _a_(619415, _n_(619414, "pygame", lambda: pygame), "image"), "load"), 'car.png')
_l_(619418)

def car(x,y):
    _l_(619426)

    _c_(619424, _a_(619420, _n_(619419, "gameDisplay", lambda: gameDisplay), "blit"), _n_(619421, "carImg", lambda: carImg),(_n_(619422, "x", lambda: x),_n_(619423, "y", lambda: y)))
    _l_(619425)

x = (_n_(619427, "display_width", lambda: display_width) * 0.45)
_l_(619428)
y = (_n_(619429, "display_height", lambda: display_height) * 0.8)
_l_(619430)

crashed = False
_l_(619431)

while not _n_(619432, "crashed", lambda: crashed):
    _l_(619463)


    for event in _c_(619436, _a_(619435, _a_(619434, _n_(619433, "pygame", lambda: pygame), "event"), "get")):
        _l_(619443)

        if _a_(619438, _n_(619437, "event", lambda: event), "type") == _a_(619440, _n_(619439, "pygame", lambda: pygame), "QUIT"):
            _l_(619442)

            crashed = True
            _l_(619441)

    _c_(619447, _a_(619445, _n_(619444, "gameDisplay", lambda: gameDisplay), "fill"), _n_(619446, "white", lambda: white))    # here
    _l_(619448)    # here
    _c_(619452, _n_(619449, "car", lambda: car), _n_(619450, "x", lambda: x),_n_(619451, "y", lambda: y))
    _l_(619453)

    _c_(619457, _a_(619456, _a_(619455, _n_(619454, "pygame", lambda: pygame), "display"), "update"))
    _l_(619458)
    _c_(619461, _a_(619460, _n_(619459, "clock", lambda: clock), "tick"), 60)
    _l_(619462)

_c_(619466, _a_(619465, _n_(619464, "pygame", lambda: pygame), "quit"))
_l_(619467)
_c_(619469, _n_(619468, "quit", lambda: quit))
_l_(619470)