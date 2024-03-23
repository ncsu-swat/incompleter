# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def find_first_duplicate(nums):
    _l_(77422)

    num_set = _c_(77399, _n_(77398, "set", lambda: set))
    _l_(77400)
    for i in _c_(77405, _n_(77401, "range", lambda: range), _c_(77404, _n_(77402, "len", lambda: len), _n_(77403, "nums", lambda: nums))):
        _l_(77419)

        if _n_(77406, "nums", lambda: nums)[_n_(77407, "i", lambda: i)] in _n_(77408, "num_set", lambda: num_set):
            _l_(77418)

            aux = _n_(77409, "nums", lambda: nums)[_n_(77410, "i", lambda: i)]
            _l_(77411)
            return aux
        else:
            _c_(77416, _a_(77413, _n_(77412, "num_set", lambda: num_set), "add"), _n_(77414, "nums", lambda: nums)[_n_(77415, "i", lambda: i)])
            _l_(77417)
    aux = _n_(77420, "no_duplicate", lambda: no_duplicate)
    _l_(77421)
    return aux
_c_(77426, _n_(77423, "print", lambda: print), _c_(77425, _n_(77424, "find_first_duplicate", lambda: find_first_duplicate), [1, 2, 3, 4, 4, 5]))
_l_(77427)
_c_(77431, _n_(77428, "print", lambda: print), _c_(77430, _n_(77429, "find_first_duplicate", lambda: find_first_duplicate), [1, 2, 3, 4]))
_l_(77432)
_c_(77436, _n_(77433, "print", lambda: print), _c_(77435, _n_(77434, "find_first_duplicate", lambda: find_first_duplicate), [1, 1, 2, 3, 3, 2, 2]))
_l_(77437)