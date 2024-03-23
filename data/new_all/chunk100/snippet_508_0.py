# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(52438)

except ImportError:
    pass

def combinations_list(list1):
    _l_(52459)

    temp = []
    _l_(52439)
    for i in _c_(52444, _n_(52440, "range", lambda: range), 0, _c_(52443, _n_(52441, "len", lambda: len), _n_(52442, "list1", lambda: list1)) + 1):
        _l_(52456)

        _c_(52454, _a_(52446, _n_(52445, "temp", lambda: temp), "append"), _c_(52453, _n_(52447, "list", lambda: list), _c_(52452, _a_(52449, _n_(52448, "itertools", lambda: itertools), "combinations"), _n_(52450, "list1", lambda: list1), _n_(52451, "i", lambda: i))))
        _l_(52455)
    aux = _n_(52457, "temp", lambda: temp)
    _l_(52458)
    return aux
_c_(52461, _n_(52460, "print", lambda: print), 'Original list:')
_l_(52462)
_c_(52465, _n_(52463, "print", lambda: print), _n_(52464, "colors", lambda: colors))
_l_(52466)
_c_(52468, _n_(52467, "print", lambda: print), '\nAll possible combinations of the said list’s elements:')
_l_(52469)
_c_(52474, _n_(52470, "print", lambda: print), _c_(52473, _n_(52471, "combinations_list", lambda: combinations_list), _n_(52472, "colors", lambda: colors)))
_l_(52475)