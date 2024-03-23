# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_min_val(list_val):
    _l_(73002)

    min_val = _c_(72997, _n_(72990, "min", lambda: min), (_n_(72991, "i", lambda: i) for i in _n_(72992, "list_val", lambda: list_val) if _c_(72996, _n_(72993, "isinstance", lambda: isinstance), _n_(72994, "i", lambda: i), _n_(72995, "int", lambda: int))))
    _l_(72998)
    aux = (_n_(72999, "max_val", lambda: max_val), _n_(73000, "min_val", lambda: min_val))
    _l_(73001)
    return aux
list_val = ['Python', 3, 2, 4, 5, 'version']
_l_(73003)
_c_(73005, _n_(73004, "print", lambda: print), 'Original list:')
_l_(73006)
_c_(73009, _n_(73007, "print", lambda: print), _n_(73008, "list_val", lambda: list_val))
_l_(73010)
_c_(73012, _n_(73011, "print", lambda: print), '\nMaximum and Minimum values in the said list:')
_l_(73013)
_c_(73018, _n_(73014, "print", lambda: print), _c_(73017, _n_(73015, "max_min_val", lambda: max_min_val), _n_(73016, "list_val", lambda: list_val)))
_l_(73019)