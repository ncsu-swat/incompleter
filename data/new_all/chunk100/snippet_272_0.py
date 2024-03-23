# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
_l_(21958)
_c_(21961, _n_(21959, "print", lambda: print), 'Original list:', _n_(21960, "nums", lambda: nums))
_l_(21962)
total_negative_nums = _c_(21968, _n_(21963, "list", lambda: list), _c_(21967, _n_(21964, "filter", lambda: filter), lambda nums: _n_(21965, "nums", lambda: nums) < 0, _n_(21966, "nums", lambda: nums)))
_l_(21969)
_c_(21974, _n_(21970, "print", lambda: print), 'Sum of the positive numbers: ', _c_(21973, _n_(21971, "sum", lambda: sum), _n_(21972, "total_negative_nums", lambda: total_negative_nums)))
_l_(21975)
_c_(21980, _n_(21976, "print", lambda: print), 'Sum of the negative numbers: ', _c_(21979, _n_(21977, "sum", lambda: sum), _n_(21978, "total_positive_nums", lambda: total_positive_nums)))
_l_(21981)