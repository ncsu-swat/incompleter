# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_min_val(list_val):
    _l_(72972)

    max_val = _c_(72967, _n_(72960, "max", lambda: max), (_n_(72961, "i", lambda: i) for i in _n_(72962, "list_val", lambda: list_val) if _c_(72966, _n_(72963, "isinstance", lambda: isinstance), _n_(72964, "i", lambda: i), _n_(72965, "int", lambda: int))))
    _l_(72968)
    aux = (_n_(72969, "max_val", lambda: max_val), _n_(72970, "min_val", lambda: min_val))
    _l_(72971)
    return aux
list_val = ['Python', 3, 2, 4, 5, 'version']
_l_(72973)
_c_(72975, _n_(72974, "print", lambda: print), 'Original list:')
_l_(72976)
_c_(72979, _n_(72977, "print", lambda: print), _n_(72978, "list_val", lambda: list_val))
_l_(72980)
_c_(72982, _n_(72981, "print", lambda: print), '\nMaximum and Minimum values in the said list:')
_l_(72983)
_c_(72988, _n_(72984, "print", lambda: print), _c_(72987, _n_(72985, "max_min_val", lambda: max_min_val), _n_(72986, "list_val", lambda: list_val)))
_l_(72989)