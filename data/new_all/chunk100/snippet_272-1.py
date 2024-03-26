# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
_l_(107930)
_c_(107933, _n_(107931, "print", lambda: print), 'Original list:', _n_(107932, "nums", lambda: nums))
_l_(107934)
total_negative_nums = _c_(107940, _n_(107935, "list", lambda: list), _c_(107939, _n_(107936, "filter", lambda: filter), lambda nums: _n_(107937, "nums", lambda: nums) < 0, _n_(107938, "nums", lambda: nums)))
_l_(107941)
_c_(107946, _n_(107942, "print", lambda: print), 'Sum of the positive numbers: ', _c_(107945, _n_(107943, "sum", lambda: sum), _n_(107944, "total_negative_nums", lambda: total_negative_nums)))
_l_(107947)
_c_(107952, _n_(107948, "print", lambda: print), 'Sum of the negative numbers: ', _c_(107951, _n_(107949, "sum", lambda: sum), _n_(107950, "total_positive_nums", lambda: total_positive_nums)))
_l_(107953)