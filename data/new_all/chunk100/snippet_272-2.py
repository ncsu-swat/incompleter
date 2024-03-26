# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(107956, _n_(107954, "print", lambda: print), 'Original list:', _n_(107955, "nums", lambda: nums))
_l_(107957)
total_negative_nums = _c_(107963, _n_(107958, "list", lambda: list), _c_(107962, _n_(107959, "filter", lambda: filter), lambda nums: _n_(107960, "nums", lambda: nums) < 0, _n_(107961, "nums", lambda: nums)))
_l_(107964)
total_positive_nums = _c_(107970, _n_(107965, "list", lambda: list), _c_(107969, _n_(107966, "filter", lambda: filter), lambda nums: _n_(107967, "nums", lambda: nums) > 0, _n_(107968, "nums", lambda: nums)))
_l_(107971)
_c_(107976, _n_(107972, "print", lambda: print), 'Sum of the positive numbers: ', _c_(107975, _n_(107973, "sum", lambda: sum), _n_(107974, "total_negative_nums", lambda: total_negative_nums)))
_l_(107977)
_c_(107982, _n_(107978, "print", lambda: print), 'Sum of the negative numbers: ', _c_(107981, _n_(107979, "sum", lambda: sum), _n_(107980, "total_positive_nums", lambda: total_positive_nums)))
_l_(107983)