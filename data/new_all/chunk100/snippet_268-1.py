# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def is_sort_list(nums):
    _l_(107776)

    result = _c_(107772, _n_(107762, "all", lambda: all), (_n_(107763, "nums", lambda: nums)[_n_(107764, "i", lambda: i)] <= _n_(107765, "nums", lambda: nums)[_n_(107766, "i", lambda: i) + 1] for i in _c_(107771, _n_(107767, "range", lambda: range), _c_(107770, _n_(107768, "len", lambda: len), _n_(107769, "nums", lambda: nums)) - 1)))
    _l_(107773)
    aux = _n_(107774, "result", lambda: result)
    _l_(107775)
    return aux
nums1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
_l_(107777)
_c_(107779, _n_(107778, "print", lambda: print), 'Original list:')
_l_(107780)
_c_(107783, _n_(107781, "print", lambda: print), _n_(107782, "nums1", lambda: nums1))
_l_(107784)
_c_(107786, _n_(107785, "print", lambda: print), '\nIs the said list is sorted!')
_l_(107787)
_c_(107792, _n_(107788, "print", lambda: print), _c_(107791, _n_(107789, "is_sort_list", lambda: is_sort_list), _n_(107790, "nums1", lambda: nums1)))
_l_(107793)
_c_(107795, _n_(107794, "print", lambda: print), '\nOriginal list:')
_l_(107796)
_c_(107799, _n_(107797, "print", lambda: print), _n_(107798, "nums1", lambda: nums1))
_l_(107800)
_c_(107802, _n_(107801, "print", lambda: print), '\nIs the said list is sorted!')
_l_(107803)
_c_(107808, _n_(107804, "print", lambda: print), _c_(107807, _n_(107805, "is_sort_list", lambda: is_sort_list), _n_(107806, "nums2", lambda: nums2)))
_l_(107809)