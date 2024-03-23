# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import combinations
    _l_(58605)

except ImportError:
    pass

def unique_combinations_colors(list_data, n):
    _l_(58614)

    aux = [_c_(58608, _a_(58606, ' and ', "join"), _n_(58607, "items", lambda: items)) for items in _c_(58612, _n_(58609, "combinations", lambda: combinations), _n_(58610, "list_data", lambda: list_data), r=_n_(58611, "n", lambda: n))]
    _l_(58613)
    return aux
_c_(58617, _n_(58615, "print", lambda: print), 'Original List: ', _n_(58616, "colors", lambda: colors))
_l_(58618)
n = 1
_l_(58619)
_c_(58621, _n_(58620, "print", lambda: print), '\nn = 1')
_l_(58622)
_c_(58630, _n_(58623, "print", lambda: print), _c_(58629, _n_(58624, "list", lambda: list), _c_(58628, _n_(58625, "unique_combinations_colors", lambda: unique_combinations_colors), _n_(58626, "colors", lambda: colors), _n_(58627, "n", lambda: n))))
_l_(58631)
n = 2
_l_(58632)
_c_(58634, _n_(58633, "print", lambda: print), '\nn = 2')
_l_(58635)
_c_(58643, _n_(58636, "print", lambda: print), _c_(58642, _n_(58637, "list", lambda: list), _c_(58641, _n_(58638, "unique_combinations_colors", lambda: unique_combinations_colors), _n_(58639, "colors", lambda: colors), _n_(58640, "n", lambda: n))))
_l_(58644)
n = 3
_l_(58645)
_c_(58647, _n_(58646, "print", lambda: print), '\nn = 3')
_l_(58648)
_c_(58656, _n_(58649, "print", lambda: print), _c_(58655, _n_(58650, "list", lambda: list), _c_(58654, _n_(58651, "unique_combinations_colors", lambda: unique_combinations_colors), _n_(58652, "colors", lambda: colors), _n_(58653, "n", lambda: n))))
_l_(58657)