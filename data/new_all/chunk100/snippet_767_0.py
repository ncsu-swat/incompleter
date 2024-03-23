# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def pancake_sort(nums):
    _l_(77752)

    arr_len = _c_(77721, _n_(77719, "len", lambda: len), _n_(77720, "nums", lambda: nums))
    _l_(77722)
    while _n_(77723, "arr_len", lambda: arr_len) > 1:
        _l_(77749)

        mi = _c_(77730, _a_(77725, _n_(77724, "nums", lambda: nums), "index"), _c_(77729, _n_(77726, "max", lambda: max), _n_(77727, "nums", lambda: nums)[0:_n_(77728, "arr_len", lambda: arr_len)]))
        _l_(77731)
        nums = _n_(77732, "nums", lambda: nums)[_n_(77733, "mi", lambda: mi)::-1] + _n_(77734, "nums", lambda: nums)[_n_(77735, "mi", lambda: mi) + 1:_c_(77738, _n_(77736, "len", lambda: len), _n_(77737, "nums", lambda: nums))]
        _l_(77739)
        nums = _n_(77740, "nums", lambda: nums)[_n_(77741, "arr_len", lambda: arr_len) - 1::-1] + _n_(77742, "nums", lambda: nums)[_n_(77743, "arr_len", lambda: arr_len):_c_(77746, _n_(77744, "len", lambda: len), _n_(77745, "nums", lambda: nums))]
        _l_(77747)
        arr_len -= 1
        _l_(77748)
    aux = _n_(77750, "nums", lambda: nums)
    _l_(77751)
    return aux
nums = [_c_(77755, _n_(77753, "int", lambda: int), _n_(77754, "item", lambda: item)) for item in _c_(77758, _a_(77757, _n_(77756, "user_input", lambda: user_input), "split"), ',')]
_l_(77759)
_c_(77764, _n_(77760, "print", lambda: print), _c_(77763, _n_(77761, "pancake_sort", lambda: pancake_sort), _n_(77762, "nums", lambda: nums)))
_l_(77765)