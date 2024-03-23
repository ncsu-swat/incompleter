# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(44178)

except ImportError:
    pass

def grouping_dictionary(l):
    _l_(44193)

    d = _c_(44181, _n_(44179, "defaultdict", lambda: defaultdict), _n_(44180, "list", lambda: list))
    _l_(44182)
    for (k, v) in _n_(44183, "l", lambda: l):
        _l_(44190)

        _c_(44188, _a_(44186, _n_(44184, "d", lambda: d)[_n_(44185, "k", lambda: k)], "append"), _n_(44187, "v", lambda: v))
        _l_(44189)
    aux = _n_(44191, "d", lambda: d)
    _l_(44192)
    return aux
_c_(44195, _n_(44194, "print", lambda: print), 'Original list:')
_l_(44196)
_c_(44199, _n_(44197, "print", lambda: print), _n_(44198, "colors", lambda: colors))
_l_(44200)
_c_(44202, _n_(44201, "print", lambda: print), '\nGrouping a sequence of key-value pairs into a dictionary of lists:')
_l_(44203)
_c_(44208, _n_(44204, "print", lambda: print), _c_(44207, _n_(44205, "grouping_dictionary", lambda: grouping_dictionary), _n_(44206, "colors", lambda: colors)))
_l_(44209)