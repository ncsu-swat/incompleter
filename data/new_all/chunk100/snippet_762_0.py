# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def find_first_duplicate(nums):
    _l_(77382)

    no_duplicate = -1
    _l_(77360)
    for i in _c_(77365, _n_(77361, "range", lambda: range), _c_(77364, _n_(77362, "len", lambda: len), _n_(77363, "nums", lambda: nums))):
        _l_(77379)

        if _n_(77366, "nums", lambda: nums)[_n_(77367, "i", lambda: i)] in _n_(77368, "num_set", lambda: num_set):
            _l_(77378)

            aux = _n_(77369, "nums", lambda: nums)[_n_(77370, "i", lambda: i)]
            _l_(77371)
            return aux
        else:
            _c_(77376, _a_(77373, _n_(77372, "num_set", lambda: num_set), "add"), _n_(77374, "nums", lambda: nums)[_n_(77375, "i", lambda: i)])
            _l_(77377)
    aux = _n_(77380, "no_duplicate", lambda: no_duplicate)
    _l_(77381)
    return aux
_c_(77386, _n_(77383, "print", lambda: print), _c_(77385, _n_(77384, "find_first_duplicate", lambda: find_first_duplicate), [1, 2, 3, 4, 4, 5]))
_l_(77387)
_c_(77391, _n_(77388, "print", lambda: print), _c_(77390, _n_(77389, "find_first_duplicate", lambda: find_first_duplicate), [1, 2, 3, 4]))
_l_(77392)
_c_(77396, _n_(77393, "print", lambda: print), _c_(77395, _n_(77394, "find_first_duplicate", lambda: find_first_duplicate), [1, 1, 2, 3, 3, 2, 2]))
_l_(77397)