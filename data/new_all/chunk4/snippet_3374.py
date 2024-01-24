# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75189625/attributeerror-str-object-has-no-attribute-type-in-snake-game
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from turtle import Turtle
    _l_(624061)

except ImportError:
    pass
try:
    from random import randint, choice
    _l_(624063)

except ImportError:
    pass
try:
    from foods import foods, shape_names
    _l_(624065)

except ImportError:
    pass


class Food(_n_(624066, "Turtle", lambda: Turtle)):
    _l_(624119)

    def __init__(self):
        _l_(624098)

        _c_(624069, _a_(624068, _n_(624067, "super", lambda: super)(), "__init__"))
        _l_(624070)
        _c_(624076, _a_(624072, _n_(624071, "self", lambda: self), "shape"), _c_(624075, _n_(624073, "choice", lambda: choice), _n_(624074, "shape_names", lambda: shape_names)))
        _l_(624077)
        _c_(624080, _a_(624079, _n_(624078, "self", lambda: self), "penup"))
        _l_(624081)
        _c_(624084, _a_(624083, _n_(624082, "self", lambda: self), "shapesize"), stretch_len=0.5, stretch_wid=0.5)
        _l_(624085)
        _c_(624088, _a_(624087, _n_(624086, "self", lambda: self), "color"), 'blue')
        _l_(624089)
        _c_(624092, _a_(624091, _n_(624090, "self", lambda: self), "speed"), 0)
        _l_(624093)
        _c_(624096, _a_(624095, _n_(624094, "self", lambda: self), "refresh"))
        _l_(624097)

    def refresh(self):
        _l_(624118)

        rand_x = _c_(624100, _n_(624099, "randint", lambda: randint), -280, 280)
        _l_(624101)
        rand_y = _c_(624103, _n_(624102, "randint", lambda: randint), -280, 280)
        _l_(624104)
        _c_(624110, _a_(624106, _n_(624105, "self", lambda: self), "shape"), _c_(624109, _n_(624107, "choice", lambda: choice), _n_(624108, "shape_names", lambda: shape_names)))
        _l_(624111)
        _c_(624116, _a_(624113, _n_(624112, "self", lambda: self), "goto"), x=_n_(624114, "rand_x", lambda: rand_x), y=_n_(624115, "rand_y", lambda: rand_y))
        _l_(624117)