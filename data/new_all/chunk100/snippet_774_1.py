# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections.abc import Iterable
    _l_(78462)

except ImportError:
    pass

def deep_flatten(lst):
    _l_(78474)

    aux = [_n_(78463, "a", lambda: a) for i in _n_(78464, "lst", lambda: lst) for a in _c_(78467, _n_(78465, "deep_flatten", lambda: deep_flatten), _n_(78466, "i", lambda: i))] if _c_(78471, _n_(78468, "isinstance", lambda: isinstance), _n_(78469, "lst", lambda: lst), _n_(78470, "Iterable", lambda: Iterable)) else [_n_(78472, "lst", lambda: lst)]
    _l_(78473)
    return aux
nums = [1, [2], [[3], [4], 5], 6]
_l_(78475)
_c_(78477, _n_(78476, "print", lambda: print), 'Original list elements:')
_l_(78478)
_c_(78481, _n_(78479, "print", lambda: print), _n_(78480, "nums", lambda: nums))
_l_(78482)
_c_(78484, _n_(78483, "print", lambda: print))
_l_(78485)
_c_(78487, _n_(78486, "print", lambda: print), 'Deep flatten the said list:')
_l_(78488)
_c_(78493, _n_(78489, "print", lambda: print), _c_(78492, _n_(78490, "deep_flatten", lambda: deep_flatten), _n_(78491, "nums", lambda: nums)))
_l_(78494)
_c_(78496, _n_(78495, "print", lambda: print), '\nOriginal list elements:')
_l_(78497)
_c_(78500, _n_(78498, "print", lambda: print), _n_(78499, "nums", lambda: nums))
_l_(78501)
_c_(78503, _n_(78502, "print", lambda: print))
_l_(78504)
_c_(78506, _n_(78505, "print", lambda: print), 'Deep flatten the said list:')
_l_(78507)
_c_(78512, _n_(78508, "print", lambda: print), _c_(78511, _n_(78509, "deep_flatten", lambda: deep_flatten), _n_(78510, "nums", lambda: nums)))
_l_(78513)