# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(116170)

except ImportError:
    pass

def grouping_dictionary(l):
    _l_(116185)

    d = _c_(116173, _n_(116171, "defaultdict", lambda: defaultdict), _n_(116172, "list", lambda: list))
    _l_(116174)
    for k, v in _n_(116175, "l", lambda: l):
        _l_(116182)

        _c_(116180, _a_(116178, _n_(116176, "d", lambda: d)[_n_(116177, "k", lambda: k)], "append"), _n_(116179, "v", lambda: v))
        _l_(116181)
    aux = _n_(116183, "d", lambda: d)
    _l_(116184)
    return aux
_c_(116187, _n_(116186, "print", lambda: print), 'Original list:')
_l_(116188)
_c_(116191, _n_(116189, "print", lambda: print), _n_(116190, "colors", lambda: colors))
_l_(116192)
_c_(116194, _n_(116193, "print", lambda: print), '\nGrouping a sequence of key-value pairs into a dictionary of lists:')
_l_(116195)
_c_(116200, _n_(116196, "print", lambda: print), _c_(116199, _n_(116197, "grouping_dictionary", lambda: grouping_dictionary), _n_(116198, "colors", lambda: colors)))
_l_(116201)