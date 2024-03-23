# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(49680, _n_(49679, "print", lambda: print), 'Original list of integers:')
_l_(49681)
_c_(49684, _n_(49682, "print", lambda: print), _n_(49683, "nums", lambda: nums))
_l_(49685)
_c_(49687, _n_(49686, "print", lambda: print), '\nEven numbers from the said list:')
_l_(49688)
even_nums = _c_(49694, _n_(49689, "list", lambda: list), _c_(49693, _n_(49690, "filter", lambda: filter), lambda x: _n_(49691, "x", lambda: x) % 2 == 0, _n_(49692, "nums", lambda: nums)))
_l_(49695)
_c_(49698, _n_(49696, "print", lambda: print), _n_(49697, "even_nums", lambda: even_nums))
_l_(49699)
_c_(49701, _n_(49700, "print", lambda: print), '\nOdd numbers from the said list:')
_l_(49702)
odd_nums = _c_(49708, _n_(49703, "list", lambda: list), _c_(49707, _n_(49704, "filter", lambda: filter), lambda x: _n_(49705, "x", lambda: x) % 2 != 0, _n_(49706, "nums", lambda: nums)))
_l_(49709)
_c_(49712, _n_(49710, "print", lambda: print), _n_(49711, "odd_nums", lambda: odd_nums))
_l_(49713)