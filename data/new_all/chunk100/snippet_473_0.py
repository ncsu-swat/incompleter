# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(49621)
_c_(49623, _n_(49622, "print", lambda: print), 'Original list of integers:')
_l_(49624)
_c_(49627, _n_(49625, "print", lambda: print), _n_(49626, "nums", lambda: nums))
_l_(49628)
_c_(49630, _n_(49629, "print", lambda: print), '\nEven numbers from the said list:')
_l_(49631)
_c_(49634, _n_(49632, "print", lambda: print), _n_(49633, "even_nums", lambda: even_nums))
_l_(49635)
_c_(49637, _n_(49636, "print", lambda: print), '\nOdd numbers from the said list:')
_l_(49638)
odd_nums = _c_(49644, _n_(49639, "list", lambda: list), _c_(49643, _n_(49640, "filter", lambda: filter), lambda x: _n_(49641, "x", lambda: x) % 2 != 0, _n_(49642, "nums", lambda: nums)))
_l_(49645)
_c_(49648, _n_(49646, "print", lambda: print), _n_(49647, "odd_nums", lambda: odd_nums))
_l_(49649)