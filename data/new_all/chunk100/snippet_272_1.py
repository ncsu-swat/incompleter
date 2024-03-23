# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
_l_(21982)
_c_(21985, _n_(21983, "print", lambda: print), 'Original list:', _n_(21984, "nums", lambda: nums))
_l_(21986)
total_positive_nums = _c_(21992, _n_(21987, "list", lambda: list), _c_(21991, _n_(21988, "filter", lambda: filter), lambda nums: _n_(21989, "nums", lambda: nums) > 0, _n_(21990, "nums", lambda: nums)))
_l_(21993)
_c_(21998, _n_(21994, "print", lambda: print), 'Sum of the positive numbers: ', _c_(21997, _n_(21995, "sum", lambda: sum), _n_(21996, "total_negative_nums", lambda: total_negative_nums)))
_l_(21999)
_c_(22004, _n_(22000, "print", lambda: print), 'Sum of the negative numbers: ', _c_(22003, _n_(22001, "sum", lambda: sum), _n_(22002, "total_positive_nums", lambda: total_positive_nums)))
_l_(22005)