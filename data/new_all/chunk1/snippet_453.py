# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44471789/python-typeerror-argument-1-must-be-pygame-surface-not-pygame-rect
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(398263)

except ImportError:
    pass
try:
    import sys
    _l_(398265)

except ImportError:
    pass
_c_(398268, _a_(398267, _n_(398266, "pygame", lambda: pygame), "init"))
_l_(398269)
screen = _c_(398273, _a_(398272, _a_(398271, _n_(398270, "pygame", lambda: pygame), "display"), "set_mode"), [640,480])
_l_(398274)
_c_(398277, _a_(398276, _n_(398275, "screen", lambda: screen), "fill"), [255,255,255])
_l_(398278)
circle = _c_(398283, _a_(398281, _a_(398280, _n_(398279, "pygame", lambda: pygame), "draw"), "circle"), _n_(398282, "screen", lambda: screen), [255,0,0],[100,100],30,0)
_l_(398284)
x = 50
_l_(398285)
y = 50
_l_(398286)
x_speed = 5
_l_(398287)
y_speed = 5
_l_(398288)

done = "False"
_l_(398289)
while _n_(398290, "done", lambda: done) == "False":
    _l_(398349)

    for event in _c_(398294, _a_(398293, _a_(398292, _n_(398291, "pygame", lambda: pygame), "event"), "get")):
        _l_(398301)

        if _a_(398296, _n_(398295, "event", lambda: event), "type") == _a_(398298, _n_(398297, "pygame", lambda: pygame), "QUIT"):
            _l_(398300)

            done="True"
            _l_(398299)
    _c_(398305, _a_(398304, _a_(398303, _n_(398302, "pygame", lambda: pygame), "time"), "delay"), 20)
    _l_(398306)
    _c_(398313, _a_(398309, _a_(398308, _n_(398307, "pygame", lambda: pygame), "draw"), "rect"), _n_(398310, "screen", lambda: screen),[255,255,255],[_n_(398311, "x", lambda: x),_n_(398312, "y", lambda: y),30,30],0)
    _l_(398314)
    x = _n_(398315, "x", lambda: x) + _n_(398316, "x_speed", lambda: x_speed)
    _l_(398317)
    y = _n_(398318, "y", lambda: y) + _n_(398319, "y_speed", lambda: y_speed)
    _l_(398320)
    if _n_(398321, "x", lambda: x) > _c_(398324, _a_(398323, _n_(398322, "screen", lambda: screen), "get_width")) - 30 or _n_(398325, "x", lambda: x) < 0:
        _l_(398328)

        x_speed = -_n_(398326, "x_speed", lambda: x_speed)
        _l_(398327)
    if _n_(398329, "y", lambda: y) > _c_(398332, _a_(398331, _n_(398330, "screen", lambda: screen), "get_height")) - 30 or _n_(398333, "y", lambda: y) < 0:
        _l_(398336)

        y_speed = -_n_(398334, "y_speed", lambda: y_speed)
        _l_(398335)
    _c_(398342, _a_(398338, _n_(398337, "screen", lambda: screen), "blit"), _n_(398339, "circle", lambda: circle),[_n_(398340, "x", lambda: x),_n_(398341, "y", lambda: y)])
    _l_(398343)
    _c_(398347, _a_(398346, _a_(398345, _n_(398344, "pygame", lambda: pygame), "display"), "flip"))
    _l_(398348)

_c_(398352, _a_(398351, _n_(398350, "pygame", lambda: pygame), "quit"))
_l_(398353)