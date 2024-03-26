# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(117698)
_c_(117700, _n_(117699, "print", lambda: print), 'Original list of integers:')
_l_(117701)
_c_(117704, _n_(117702, "print", lambda: print), _n_(117703, "nums", lambda: nums))
_l_(117705)
_c_(117707, _n_(117706, "print", lambda: print), '\nEven numbers from the said list:')
_l_(117708)
_c_(117711, _n_(117709, "print", lambda: print), _n_(117710, "even_nums", lambda: even_nums))
_l_(117712)
_c_(117714, _n_(117713, "print", lambda: print), '\nOdd numbers from the said list:')
_l_(117715)
odd_nums = _c_(117721, _n_(117716, "list", lambda: list), _c_(117720, _n_(117717, "filter", lambda: filter), lambda x: _n_(117718, "x", lambda: x) % 2 != 0, _n_(117719, "nums", lambda: nums)))
_l_(117722)
_c_(117725, _n_(117723, "print", lambda: print), _n_(117724, "odd_nums", lambda: odd_nums))
_l_(117726)