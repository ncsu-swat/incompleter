# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(22008, _n_(22006, "print", lambda: print), 'Original list:', _n_(22007, "nums", lambda: nums))
_l_(22009)
total_negative_nums = _c_(22015, _n_(22010, "list", lambda: list), _c_(22014, _n_(22011, "filter", lambda: filter), lambda nums: _n_(22012, "nums", lambda: nums) < 0, _n_(22013, "nums", lambda: nums)))
_l_(22016)
total_positive_nums = _c_(22022, _n_(22017, "list", lambda: list), _c_(22021, _n_(22018, "filter", lambda: filter), lambda nums: _n_(22019, "nums", lambda: nums) > 0, _n_(22020, "nums", lambda: nums)))
_l_(22023)
_c_(22028, _n_(22024, "print", lambda: print), 'Sum of the positive numbers: ', _c_(22027, _n_(22025, "sum", lambda: sum), _n_(22026, "total_negative_nums", lambda: total_negative_nums)))
_l_(22029)
_c_(22034, _n_(22030, "print", lambda: print), 'Sum of the negative numbers: ', _c_(22033, _n_(22031, "sum", lambda: sum), _n_(22032, "total_positive_nums", lambda: total_positive_nums)))
_l_(22035)