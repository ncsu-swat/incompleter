# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unique_list(text_str):
    _l_(77625)

    l = _c_(77609, _a_(77608, _n_(77607, "text_str", lambda: text_str), "split"))
    _l_(77610)
    for x in _n_(77611, "l", lambda: l):
        _l_(77620)

        if _n_(77612, "x", lambda: x) not in _n_(77613, "temp", lambda: temp):
            _l_(77619)

            _c_(77617, _a_(77615, _n_(77614, "temp", lambda: temp), "append"), _n_(77616, "x", lambda: x))
            _l_(77618)
    aux = _c_(77623, _a_(77621, ' ', "join"), _n_(77622, "temp", lambda: temp))
    _l_(77624)
    return aux
text_str = 'Python Exercises Practice Solution Exercises'
_l_(77626)
_c_(77628, _n_(77627, "print", lambda: print), 'Original String:')
_l_(77629)
_c_(77632, _n_(77630, "print", lambda: print), _n_(77631, "text_str", lambda: text_str))
_l_(77633)
_c_(77635, _n_(77634, "print", lambda: print), '\nAfter removing duplicate words from the said string:')
_l_(77636)
_c_(77641, _n_(77637, "print", lambda: print), _c_(77640, _n_(77638, "unique_list", lambda: unique_list), _n_(77639, "text_str", lambda: text_str)))
_l_(77642)