# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70082191/pygame-not-blitting-image-instead-spitting-out-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(536545)

except ImportError:
    pass

#Initialize pygame module
_c_(536548, _a_(536547, _n_(536546, "pygame", lambda: pygame), "init"))
_l_(536549)

#Create Screen
screen = _c_(536553, _a_(536552, _a_(536551, _n_(536550, "pygame", lambda: pygame), "display"), "set_mode"), (1000, 600))
_l_(536554)

#Title and Icon
_c_(536558, _a_(536557, _a_(536556, _n_(536555, "pygame", lambda: pygame), "display"), "set_caption"), "Jungle Invader")
_l_(536559)
icon = _c_(536563, _a_(536562, _a_(536561, _n_(536560, "pygame", lambda: pygame), "image"), "load"), 'fox-sitting.png')
_l_(536564)
_c_(536569, _a_(536567, _a_(536566, _n_(536565, "pygame", lambda: pygame), "display"), "set_icon"), _n_(536568, "icon", lambda: icon))
_l_(536570)

# Player
player = _c_(536574, _a_(536573, _a_(536572, _n_(536571, "pygame", lambda: pygame), "image"), "load"), 'cat.png')
_l_(536575)
playerX = 300
_l_(536576)
playerY = 500
_l_(536577)

def player():
    _l_(536585)

    _c_(536583, _a_(536579, _n_(536578, "screen", lambda: screen), "blit"), _n_(536580, "player", lambda: player), (_n_(536581, "playerX", lambda: playerX), _n_(536582, "playerY", lambda: playerY)))
    _l_(536584)


#Main loop
running = True
_l_(536586)
while _n_(536587, "running", lambda: running):
    _l_(536611)

    _c_(536591, _a_(536590, _a_(536589, _n_(536588, "pygame", lambda: pygame), "display"), "update"))
    _l_(536592)

    for event in _c_(536596, _a_(536595, _a_(536594, _n_(536593, "pygame", lambda: pygame), "event"), "get")):
        _l_(536603)

        if _a_(536598, _n_(536597, "event", lambda: event), "type") == _a_(536600, _n_(536599, "pygame", lambda: pygame), "QUIT"):
            _l_(536602)

            running = False
            _l_(536601)

    _c_(536606, _a_(536605, _n_(536604, "screen", lambda: screen), "fill"), (244, 232, 255))
    _l_(536607)
    _c_(536609, _n_(536608, "player", lambda: player))
    _l_(536610)