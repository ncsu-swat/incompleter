# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums = [2, 4, 6, 9, 11]
_l_(65616)
_c_(65619, _n_(65617, "print", lambda: print), 'Original list: ', _n_(65618, "nums", lambda: nums))
_l_(65620)
_c_(65623, _n_(65621, "print", lambda: print), 'Given number: ', _n_(65622, "n", lambda: n))
_l_(65624)
filtered_numbers = _c_(65631, _n_(65625, "list", lambda: list), _c_(65630, _n_(65626, "map", lambda: map), lambda number: _n_(65627, "number", lambda: number) * _n_(65628, "n", lambda: n), _n_(65629, "nums", lambda: nums)))
_l_(65632)
_c_(65634, _n_(65633, "print", lambda: print), 'Result:')
_l_(65635)
_c_(65643, _n_(65636, "print", lambda: print), _c_(65642, _a_(65637, ' ', "join"), _c_(65641, _n_(65638, "map", lambda: map), _n_(65639, "str", lambda: str), _n_(65640, "filtered_numbers", lambda: filtered_numbers))))
_l_(65644)