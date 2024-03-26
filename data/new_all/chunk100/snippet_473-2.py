# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(117757, _n_(117756, "print", lambda: print), 'Original list of integers:')
_l_(117758)
_c_(117761, _n_(117759, "print", lambda: print), _n_(117760, "nums", lambda: nums))
_l_(117762)
_c_(117764, _n_(117763, "print", lambda: print), '\nEven numbers from the said list:')
_l_(117765)
even_nums = _c_(117771, _n_(117766, "list", lambda: list), _c_(117770, _n_(117767, "filter", lambda: filter), lambda x: _n_(117768, "x", lambda: x) % 2 == 0, _n_(117769, "nums", lambda: nums)))
_l_(117772)
_c_(117775, _n_(117773, "print", lambda: print), _n_(117774, "even_nums", lambda: even_nums))
_l_(117776)
_c_(117778, _n_(117777, "print", lambda: print), '\nOdd numbers from the said list:')
_l_(117779)
odd_nums = _c_(117785, _n_(117780, "list", lambda: list), _c_(117784, _n_(117781, "filter", lambda: filter), lambda x: _n_(117782, "x", lambda: x) % 2 != 0, _n_(117783, "nums", lambda: nums)))
_l_(117786)
_c_(117789, _n_(117787, "print", lambda: print), _n_(117788, "odd_nums", lambda: odd_nums))
_l_(117790)