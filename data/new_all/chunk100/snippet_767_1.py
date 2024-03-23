# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def pancake_sort(nums):
    _l_(77795)

    while _n_(77766, "arr_len", lambda: arr_len) > 1:
        _l_(77792)

        mi = _c_(77773, _a_(77768, _n_(77767, "nums", lambda: nums), "index"), _c_(77772, _n_(77769, "max", lambda: max), _n_(77770, "nums", lambda: nums)[0:_n_(77771, "arr_len", lambda: arr_len)]))
        _l_(77774)
        nums = _n_(77775, "nums", lambda: nums)[_n_(77776, "mi", lambda: mi)::-1] + _n_(77777, "nums", lambda: nums)[_n_(77778, "mi", lambda: mi) + 1:_c_(77781, _n_(77779, "len", lambda: len), _n_(77780, "nums", lambda: nums))]
        _l_(77782)
        nums = _n_(77783, "nums", lambda: nums)[_n_(77784, "arr_len", lambda: arr_len) - 1::-1] + _n_(77785, "nums", lambda: nums)[_n_(77786, "arr_len", lambda: arr_len):_c_(77789, _n_(77787, "len", lambda: len), _n_(77788, "nums", lambda: nums))]
        _l_(77790)
        arr_len -= 1
        _l_(77791)
    aux = _n_(77793, "nums", lambda: nums)
    _l_(77794)
    return aux
user_input = _c_(77799, _a_(77798, _c_(77797, _n_(77796, "input", lambda: input), 'Input numbers separated by a comma:\n'), "strip"))
_l_(77800)
nums = [_c_(77803, _n_(77801, "int", lambda: int), _n_(77802, "item", lambda: item)) for item in _c_(77806, _a_(77805, _n_(77804, "user_input", lambda: user_input), "split"), ',')]
_l_(77807)
_c_(77812, _n_(77808, "print", lambda: print), _c_(77811, _n_(77809, "pancake_sort", lambda: pancake_sort), _n_(77810, "nums", lambda: nums)))
_l_(77813)