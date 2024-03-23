# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unique_list(text_str):
    _l_(77589)

    temp = []
    _l_(77574)
    for x in _n_(77575, "l", lambda: l):
        _l_(77584)

        if _n_(77576, "x", lambda: x) not in _n_(77577, "temp", lambda: temp):
            _l_(77583)

            _c_(77581, _a_(77579, _n_(77578, "temp", lambda: temp), "append"), _n_(77580, "x", lambda: x))
            _l_(77582)
    aux = _c_(77587, _a_(77585, ' ', "join"), _n_(77586, "temp", lambda: temp))
    _l_(77588)
    return aux
text_str = 'Python Exercises Practice Solution Exercises'
_l_(77590)
_c_(77592, _n_(77591, "print", lambda: print), 'Original String:')
_l_(77593)
_c_(77596, _n_(77594, "print", lambda: print), _n_(77595, "text_str", lambda: text_str))
_l_(77597)
_c_(77599, _n_(77598, "print", lambda: print), '\nAfter removing duplicate words from the said string:')
_l_(77600)
_c_(77605, _n_(77601, "print", lambda: print), _c_(77604, _n_(77602, "unique_list", lambda: unique_list), _n_(77603, "text_str", lambda: text_str)))
_l_(77606)