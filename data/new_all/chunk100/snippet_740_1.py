# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from operator import itemgetter
    _l_(74487)

except ImportError:
    pass

def max_min_list_tuples(class_students):
    _l_(74503)

    return_max = _c_(74492, _n_(74488, "max", lambda: max), _n_(74489, "class_students", lambda: class_students), key=_c_(74491, _n_(74490, "itemgetter", lambda: itemgetter), 1))[1]
    _l_(74493)
    return_min = _c_(74498, _n_(74494, "min", lambda: min), _n_(74495, "class_students", lambda: class_students), key=_c_(74497, _n_(74496, "itemgetter", lambda: itemgetter), 1))[1]
    _l_(74499)
    aux = (_n_(74500, "return_max", lambda: return_max), _n_(74501, "return_min", lambda: return_min))
    _l_(74502)
    return aux
_c_(74505, _n_(74504, "print", lambda: print), 'Original list with tuples:')
_l_(74506)
_c_(74509, _n_(74507, "print", lambda: print), _n_(74508, "class_students", lambda: class_students))
_l_(74510)
_c_(74512, _n_(74511, "print", lambda: print), '\nMaximum and minimum values of the said list of tuples:')
_l_(74513)
_c_(74518, _n_(74514, "print", lambda: print), _c_(74517, _n_(74515, "max_min_list_tuples", lambda: max_min_list_tuples), _n_(74516, "class_students", lambda: class_students)))
_l_(74519)