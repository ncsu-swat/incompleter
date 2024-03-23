# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def pancake_sort(nums):
    _l_(77847)

    arr_len = _c_(77816, _n_(77814, "len", lambda: len), _n_(77815, "nums", lambda: nums))
    _l_(77817)
    while _n_(77818, "arr_len", lambda: arr_len) > 1:
        _l_(77844)

        mi = _c_(77825, _a_(77820, _n_(77819, "nums", lambda: nums), "index"), _c_(77824, _n_(77821, "max", lambda: max), _n_(77822, "nums", lambda: nums)[0:_n_(77823, "arr_len", lambda: arr_len)]))
        _l_(77826)
        nums = _n_(77827, "nums", lambda: nums)[_n_(77828, "mi", lambda: mi)::-1] + _n_(77829, "nums", lambda: nums)[_n_(77830, "mi", lambda: mi) + 1:_c_(77833, _n_(77831, "len", lambda: len), _n_(77832, "nums", lambda: nums))]
        _l_(77834)
        nums = _n_(77835, "nums", lambda: nums)[_n_(77836, "arr_len", lambda: arr_len) - 1::-1] + _n_(77837, "nums", lambda: nums)[_n_(77838, "arr_len", lambda: arr_len):_c_(77841, _n_(77839, "len", lambda: len), _n_(77840, "nums", lambda: nums))]
        _l_(77842)
        arr_len -= 1
        _l_(77843)
    aux = _n_(77845, "nums", lambda: nums)
    _l_(77846)
    return aux
user_input = _c_(77851, _a_(77850, _c_(77849, _n_(77848, "input", lambda: input), 'Input numbers separated by a comma:\n'), "strip"))
_l_(77852)
_c_(77857, _n_(77853, "print", lambda: print), _c_(77856, _n_(77854, "pancake_sort", lambda: pancake_sort), _n_(77855, "nums", lambda: nums)))
_l_(77858)