# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unique_list(text_str):
    _l_(77662)

    l = _c_(77645, _a_(77644, _n_(77643, "text_str", lambda: text_str), "split"))
    _l_(77646)
    temp = []
    _l_(77647)
    for x in _n_(77648, "l", lambda: l):
        _l_(77657)

        if _n_(77649, "x", lambda: x) not in _n_(77650, "temp", lambda: temp):
            _l_(77656)

            _c_(77654, _a_(77652, _n_(77651, "temp", lambda: temp), "append"), _n_(77653, "x", lambda: x))
            _l_(77655)
    aux = _c_(77660, _a_(77658, ' ', "join"), _n_(77659, "temp", lambda: temp))
    _l_(77661)
    return aux
_c_(77664, _n_(77663, "print", lambda: print), 'Original String:')
_l_(77665)
_c_(77668, _n_(77666, "print", lambda: print), _n_(77667, "text_str", lambda: text_str))
_l_(77669)
_c_(77671, _n_(77670, "print", lambda: print), '\nAfter removing duplicate words from the said string:')
_l_(77672)
_c_(77677, _n_(77673, "print", lambda: print), _c_(77676, _n_(77674, "unique_list", lambda: unique_list), _n_(77675, "text_str", lambda: text_str)))
_l_(77678)