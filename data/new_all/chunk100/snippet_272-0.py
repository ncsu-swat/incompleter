# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
_l_(107906)
_c_(107909, _n_(107907, "print", lambda: print), 'Original list:', _n_(107908, "nums", lambda: nums))
_l_(107910)
total_positive_nums = _c_(107916, _n_(107911, "list", lambda: list), _c_(107915, _n_(107912, "filter", lambda: filter), lambda nums: _n_(107913, "nums", lambda: nums) > 0, _n_(107914, "nums", lambda: nums)))
_l_(107917)
_c_(107922, _n_(107918, "print", lambda: print), 'Sum of the positive numbers: ', _c_(107921, _n_(107919, "sum", lambda: sum), _n_(107920, "total_negative_nums", lambda: total_negative_nums)))
_l_(107923)
_c_(107928, _n_(107924, "print", lambda: print), 'Sum of the negative numbers: ', _c_(107927, _n_(107925, "sum", lambda: sum), _n_(107926, "total_positive_nums", lambda: total_positive_nums)))
_l_(107929)