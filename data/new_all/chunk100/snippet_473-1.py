# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(117727)
_c_(117729, _n_(117728, "print", lambda: print), 'Original list of integers:')
_l_(117730)
_c_(117733, _n_(117731, "print", lambda: print), _n_(117732, "nums", lambda: nums))
_l_(117734)
_c_(117736, _n_(117735, "print", lambda: print), '\nEven numbers from the said list:')
_l_(117737)
even_nums = _c_(117743, _n_(117738, "list", lambda: list), _c_(117742, _n_(117739, "filter", lambda: filter), lambda x: _n_(117740, "x", lambda: x) % 2 == 0, _n_(117741, "nums", lambda: nums)))
_l_(117744)
_c_(117747, _n_(117745, "print", lambda: print), _n_(117746, "even_nums", lambda: even_nums))
_l_(117748)
_c_(117750, _n_(117749, "print", lambda: print), '\nOdd numbers from the said list:')
_l_(117751)
_c_(117754, _n_(117752, "print", lambda: print), _n_(117753, "odd_nums", lambda: odd_nums))
_l_(117755)