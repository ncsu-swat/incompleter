# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(52477)

except ImportError:
    pass

def combinations_list(list1):
    _l_(52497)

    for i in _c_(52482, _n_(52478, "range", lambda: range), 0, _c_(52481, _n_(52479, "len", lambda: len), _n_(52480, "list1", lambda: list1)) + 1):
        _l_(52494)

        _c_(52492, _a_(52484, _n_(52483, "temp", lambda: temp), "append"), _c_(52491, _n_(52485, "list", lambda: list), _c_(52490, _a_(52487, _n_(52486, "itertools", lambda: itertools), "combinations"), _n_(52488, "list1", lambda: list1), _n_(52489, "i", lambda: i))))
        _l_(52493)
    aux = _n_(52495, "temp", lambda: temp)
    _l_(52496)
    return aux
colors = ['orange', 'red', 'green', 'blue']
_l_(52498)
_c_(52500, _n_(52499, "print", lambda: print), 'Original list:')
_l_(52501)
_c_(52504, _n_(52502, "print", lambda: print), _n_(52503, "colors", lambda: colors))
_l_(52505)
_c_(52507, _n_(52506, "print", lambda: print), '\nAll possible combinations of the said list’s elements:')
_l_(52508)
_c_(52513, _n_(52509, "print", lambda: print), _c_(52512, _n_(52510, "combinations_list", lambda: combinations_list), _n_(52511, "colors", lambda: colors)))
_l_(52514)