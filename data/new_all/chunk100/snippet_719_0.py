# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_min_val(list_val):
    _l_(72943)

    max_val = _c_(72929, _n_(72922, "max", lambda: max), (_n_(72923, "i", lambda: i) for i in _n_(72924, "list_val", lambda: list_val) if _c_(72928, _n_(72925, "isinstance", lambda: isinstance), _n_(72926, "i", lambda: i), _n_(72927, "int", lambda: int))))
    _l_(72930)
    min_val = _c_(72938, _n_(72931, "min", lambda: min), (_n_(72932, "i", lambda: i) for i in _n_(72933, "list_val", lambda: list_val) if _c_(72937, _n_(72934, "isinstance", lambda: isinstance), _n_(72935, "i", lambda: i), _n_(72936, "int", lambda: int))))
    _l_(72939)
    aux = (_n_(72940, "max_val", lambda: max_val), _n_(72941, "min_val", lambda: min_val))
    _l_(72942)
    return aux
_c_(72945, _n_(72944, "print", lambda: print), 'Original list:')
_l_(72946)
_c_(72949, _n_(72947, "print", lambda: print), _n_(72948, "list_val", lambda: list_val))
_l_(72950)
_c_(72952, _n_(72951, "print", lambda: print), '\nMaximum and Minimum values in the said list:')
_l_(72953)
_c_(72958, _n_(72954, "print", lambda: print), _c_(72957, _n_(72955, "max_min_val", lambda: max_min_val), _n_(72956, "list_val", lambda: list_val)))
_l_(72959)