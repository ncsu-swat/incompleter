# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections.abc import Iterable
    _l_(78409)

except ImportError:
    pass

def deep_flatten(lst):
    _l_(78421)

    aux = [_n_(78410, "a", lambda: a) for i in _n_(78411, "lst", lambda: lst) for a in _c_(78414, _n_(78412, "deep_flatten", lambda: deep_flatten), _n_(78413, "i", lambda: i))] if _c_(78418, _n_(78415, "isinstance", lambda: isinstance), _n_(78416, "lst", lambda: lst), _n_(78417, "Iterable", lambda: Iterable)) else [_n_(78419, "lst", lambda: lst)]
    _l_(78420)
    return aux
_c_(78423, _n_(78422, "print", lambda: print), 'Original list elements:')
_l_(78424)
_c_(78427, _n_(78425, "print", lambda: print), _n_(78426, "nums", lambda: nums))
_l_(78428)
_c_(78430, _n_(78429, "print", lambda: print))
_l_(78431)
_c_(78433, _n_(78432, "print", lambda: print), 'Deep flatten the said list:')
_l_(78434)
_c_(78439, _n_(78435, "print", lambda: print), _c_(78438, _n_(78436, "deep_flatten", lambda: deep_flatten), _n_(78437, "nums", lambda: nums)))
_l_(78440)
nums = [[[1, 2, 3], [4, 5]], 6]
_l_(78441)
_c_(78443, _n_(78442, "print", lambda: print), '\nOriginal list elements:')
_l_(78444)
_c_(78447, _n_(78445, "print", lambda: print), _n_(78446, "nums", lambda: nums))
_l_(78448)
_c_(78450, _n_(78449, "print", lambda: print))
_l_(78451)
_c_(78453, _n_(78452, "print", lambda: print), 'Deep flatten the said list:')
_l_(78454)
_c_(78459, _n_(78455, "print", lambda: print), _c_(78458, _n_(78456, "deep_flatten", lambda: deep_flatten), _n_(78457, "nums", lambda: nums)))
_l_(78460)