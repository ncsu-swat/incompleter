# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68157511/typeerror-when-drawing-circle-in-pygame
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame
    _l_(617731)

except ImportError:
    pass
try:
    from circle import Circle
    _l_(617733)

except ImportError:
    pass
try:
    from draw import Draw
    _l_(617735)

except ImportError:
    pass
try:
    from Box2D import b2World
    _l_(617737)

except ImportError:
    pass

PPM = 20
_l_(617738)
TARGET_FPS = 60
_l_(617739)
TIME_STEP = 1.0 / _n_(617740, "TARGET_FPS", lambda: TARGET_FPS)
_l_(617741)

_c_(617744, _a_(617743, _n_(617742, "pygame", lambda: pygame), "init"))
_l_(617745)
screen = _c_(617749, _a_(617748, _a_(617747, _n_(617746, "pygame", lambda: pygame), "display"), "set_mode"), (600, 480))
_l_(617750)
clock = _c_(617754, _a_(617753, _a_(617752, _n_(617751, "pygame", lambda: pygame), "time"), "Clock"))
_l_(617755)

# A list for all of our rectangles
world = _c_(617757, _n_(617756, "b2World", lambda: b2World), gravity=(0, 30), doSleep=True)
_l_(617758)


close = False
_l_(617759)

while not _n_(617760, "close", lambda: close):
    _l_(617803)

    
    for event in _c_(617764, _a_(617763, _a_(617762, _n_(617761, "pygame", lambda: pygame), "event"), "get")):
        _l_(617771)

        if _a_(617766, _n_(617765, "event", lambda: event), "type") == _a_(617768, _n_(617767, "pygame", lambda: pygame), "QUIT"):
            _l_(617770)

            close = True
            _l_(617769)
    
    _c_(617774, _a_(617773, _n_(617772, "screen", lambda: screen), "fill"), (255,255,255))
    _l_(617775)
    
    circle = _c_(617779, _n_(617776, "Circle", lambda: Circle), _n_(617777, "world", lambda: world),300,300,_n_(617778, "PPM", lambda: PPM))
    _l_(617780)
    
    _c_(617786, _n_(617781, "Draw", lambda: Draw), _n_(617782, "screen", lambda: screen),_a_(617784, _n_(617783, "world", lambda: world), "bodies"),_n_(617785, "PPM", lambda: PPM))
    _l_(617787)
    
    _c_(617791, _a_(617789, _n_(617788, "world", lambda: world), "Step"), _n_(617790, "TIME_STEP", lambda: TIME_STEP), 10, 10)
    _l_(617792)
    _c_(617796, _a_(617795, _a_(617794, _n_(617793, "pygame", lambda: pygame), "display"), "flip"))
    _l_(617797)
    _c_(617801, _a_(617799, _n_(617798, "clock", lambda: clock), "tick"), _n_(617800, "TARGET_FPS", lambda: TARGET_FPS))
    _l_(617802)

_c_(617806, _a_(617805, _n_(617804, "pygame", lambda: pygame), "quit"))
_l_(617807)