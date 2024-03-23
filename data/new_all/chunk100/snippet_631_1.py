# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
n = 2
_l_(65645)
_c_(65648, _n_(65646, "print", lambda: print), 'Original list: ', _n_(65647, "nums", lambda: nums))
_l_(65649)
_c_(65652, _n_(65650, "print", lambda: print), 'Given number: ', _n_(65651, "n", lambda: n))
_l_(65653)
filtered_numbers = _c_(65660, _n_(65654, "list", lambda: list), _c_(65659, _n_(65655, "map", lambda: map), lambda number: _n_(65656, "number", lambda: number) * _n_(65657, "n", lambda: n), _n_(65658, "nums", lambda: nums)))
_l_(65661)
_c_(65663, _n_(65662, "print", lambda: print), 'Result:')
_l_(65664)
_c_(65672, _n_(65665, "print", lambda: print), _c_(65671, _a_(65666, ' ', "join"), _c_(65670, _n_(65667, "map", lambda: map), _n_(65668, "str", lambda: str), _n_(65669, "filtered_numbers", lambda: filtered_numbers))))
_l_(65673)