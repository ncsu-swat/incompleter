# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def is_sort_list(nums):
    _l_(21610)

    result = _c_(21606, _n_(21596, "all", lambda: all), (_n_(21597, "nums", lambda: nums)[_n_(21598, "i", lambda: i)] <= _n_(21599, "nums", lambda: nums)[_n_(21600, "i", lambda: i) + 1] for i in _c_(21605, _n_(21601, "range", lambda: range), _c_(21604, _n_(21602, "len", lambda: len), _n_(21603, "nums", lambda: nums)) - 1)))
    _l_(21607)
    aux = _n_(21608, "result", lambda: result)
    _l_(21609)
    return aux
_c_(21612, _n_(21611, "print", lambda: print), 'Original list:')
_l_(21613)
_c_(21616, _n_(21614, "print", lambda: print), _n_(21615, "nums1", lambda: nums1))
_l_(21617)
_c_(21619, _n_(21618, "print", lambda: print), '\nIs the said list is sorted!')
_l_(21620)
_c_(21625, _n_(21621, "print", lambda: print), _c_(21624, _n_(21622, "is_sort_list", lambda: is_sort_list), _n_(21623, "nums1", lambda: nums1)))
_l_(21626)
nums2 = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
_l_(21627)
_c_(21629, _n_(21628, "print", lambda: print), '\nOriginal list:')
_l_(21630)
_c_(21633, _n_(21631, "print", lambda: print), _n_(21632, "nums1", lambda: nums1))
_l_(21634)
_c_(21636, _n_(21635, "print", lambda: print), '\nIs the said list is sorted!')
_l_(21637)
_c_(21642, _n_(21638, "print", lambda: print), _c_(21641, _n_(21639, "is_sort_list", lambda: is_sort_list), _n_(21640, "nums2", lambda: nums2)))
_l_(21643)