# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def is_sort_list(nums):
    _l_(107728)

    result = _c_(107724, _n_(107714, "all", lambda: all), (_n_(107715, "nums", lambda: nums)[_n_(107716, "i", lambda: i)] <= _n_(107717, "nums", lambda: nums)[_n_(107718, "i", lambda: i) + 1] for i in _c_(107723, _n_(107719, "range", lambda: range), _c_(107722, _n_(107720, "len", lambda: len), _n_(107721, "nums", lambda: nums)) - 1)))
    _l_(107725)
    aux = _n_(107726, "result", lambda: result)
    _l_(107727)
    return aux
_c_(107730, _n_(107729, "print", lambda: print), 'Original list:')
_l_(107731)
_c_(107734, _n_(107732, "print", lambda: print), _n_(107733, "nums1", lambda: nums1))
_l_(107735)
_c_(107737, _n_(107736, "print", lambda: print), '\nIs the said list is sorted!')
_l_(107738)
_c_(107743, _n_(107739, "print", lambda: print), _c_(107742, _n_(107740, "is_sort_list", lambda: is_sort_list), _n_(107741, "nums1", lambda: nums1)))
_l_(107744)
nums2 = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
_l_(107745)
_c_(107747, _n_(107746, "print", lambda: print), '\nOriginal list:')
_l_(107748)
_c_(107751, _n_(107749, "print", lambda: print), _n_(107750, "nums1", lambda: nums1))
_l_(107752)
_c_(107754, _n_(107753, "print", lambda: print), '\nIs the said list is sorted!')
_l_(107755)
_c_(107760, _n_(107756, "print", lambda: print), _c_(107759, _n_(107757, "is_sort_list", lambda: is_sort_list), _n_(107758, "nums2", lambda: nums2)))
_l_(107761)