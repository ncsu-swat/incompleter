# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67459471/attributeerror-pygame-math-vector2-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pygame, sys
    _l_(400812)

except ImportError:
    pass
try:
    from pygame.locals import *
    _l_(400814)

except ImportError:
    pass
try:
    from pygame.math import Vector2
    _l_(400816)

except ImportError:
    pass

class Food:
    _l_(400851)

    def __init__(self):
        _l_(400829)

        _n_(400817, "self", lambda: self).food_x = 5
        _l_(400818)
        _n_(400819, "self", lambda: self).food_y = 4
        _l_(400820)
        _n_(400821, "self", lambda: self).position = _c_(400827, _n_(400822, "Vector2", lambda: Vector2), _a_(400824, _n_(400823, "self", lambda: self), "food_x"), _a_(400826, _n_(400825, "self", lambda: self), "food_y"))
        _l_(400828)

    def draw_food(self):
        _l_(400850)

        food_shape = _c_(400840, _a_(400831, _n_(400830, "pygame", lambda: pygame), "Rect"), _a_(400834, _a_(400833, _n_(400832, "self", lambda: self), "position"), "food_x"), _a_(400837, _a_(400836, _n_(400835, "self", lambda: self), "position"), "food_y"), _n_(400838, "cell_size", lambda: cell_size), _n_(400839, "cell_size", lambda: cell_size))
        _l_(400841)
        _c_(400848, _a_(400844, _a_(400843, _n_(400842, "pygame", lambda: pygame), "draw"), "rect"), _n_(400845, "screen", lambda: screen), _n_(400846, "screen_surface_color", lambda: screen_surface_color), _n_(400847, "food_shape", lambda: food_shape))
        _l_(400849)

cell_size = 40
_l_(400852)
cell_number = 19
_l_(400853)
screen_color = (175, 215, 70)
_l_(400854)
screen_surface_color = (70, 70, 214)
_l_(400855)

_c_(400858, _a_(400857, _n_(400856, "pygame", lambda: pygame), "init"))
_l_(400859)
screen = _c_(400867, _a_(400862, _a_(400861, _n_(400860, "pygame", lambda: pygame), "display"), "set_mode"), (_n_(400863, "cell_number", lambda: cell_number) * _n_(400864, "cell_size", lambda: cell_size), _n_(400865, "cell_number", lambda: cell_number) * _n_(400866, "cell_size", lambda: cell_size)))
_l_(400868)
clock = _c_(400872, _a_(400871, _a_(400870, _n_(400869, "pygame", lambda: pygame), "time"), "Clock"))
_l_(400873)

food = _c_(400875, _n_(400874, "Food", lambda: Food))
_l_(400876)

running = True
_l_(400877)
while _n_(400878, "running", lambda: running):
    _l_(400932)

    for event in _c_(400882, _a_(400881, _a_(400880, _n_(400879, "pygame", lambda: pygame), "event"), "get")):
        _l_(400913)

        if _a_(400884, _n_(400883, "event", lambda: event), "type") == _a_(400886, _n_(400885, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(400912)

            if _a_(400888, _n_(400887, "event", lambda: event), "key") == _n_(400889, "K_ESCAPE", lambda: K_ESCAPE):
                _l_(400898)

                _c_(400892, _a_(400891, _n_(400890, "pygame", lambda: pygame), "quit"))
                _l_(400893)
                _c_(400896, _a_(400895, _n_(400894, "sys", lambda: sys), "exit"))
                _l_(400897)
    
        elif _a_(400900, _n_(400899, "event", lambda: event), "type") == _a_(400902, _n_(400901, "pygame", lambda: pygame), "QUIT"):
            _l_(400911)

            _c_(400905, _a_(400904, _n_(400903, "pygame", lambda: pygame), "quit"))
            _l_(400906)
            _c_(400909, _a_(400908, _n_(400907, "sys", lambda: sys), "exit"))
            _l_(400910)

    _c_(400917, _a_(400915, _n_(400914, "screen", lambda: screen), "fill"), _n_(400916, "screen_color", lambda: screen_color))
    _l_(400918)
    _c_(400921, _a_(400920, _n_(400919, "food", lambda: food), "draw_food"))
    _l_(400922)
    _c_(400926, _a_(400925, _a_(400924, _n_(400923, "pygame", lambda: pygame), "display"), "update"))
    _l_(400927)
    _c_(400930, _a_(400929, _n_(400928, "clock", lambda: clock), "tick"), 60)
    _l_(400931)