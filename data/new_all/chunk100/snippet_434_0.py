# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(44148)

except ImportError:
    pass

def grouping_dictionary(l):
    _l_(44159)

    for (k, v) in _n_(44149, "l", lambda: l):
        _l_(44156)

        _c_(44154, _a_(44152, _n_(44150, "d", lambda: d)[_n_(44151, "k", lambda: k)], "append"), _n_(44153, "v", lambda: v))
        _l_(44155)
    aux = _n_(44157, "d", lambda: d)
    _l_(44158)
    return aux
colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
_l_(44160)
_c_(44162, _n_(44161, "print", lambda: print), 'Original list:')
_l_(44163)
_c_(44166, _n_(44164, "print", lambda: print), _n_(44165, "colors", lambda: colors))
_l_(44167)
_c_(44169, _n_(44168, "print", lambda: print), '\nGrouping a sequence of key-value pairs into a dictionary of lists:')
_l_(44170)
_c_(44175, _n_(44171, "print", lambda: print), _c_(44174, _n_(44172, "grouping_dictionary", lambda: grouping_dictionary), _n_(44173, "colors", lambda: colors)))
_l_(44176)