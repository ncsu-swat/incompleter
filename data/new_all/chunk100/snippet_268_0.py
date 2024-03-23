# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def is_sort_list(nums):
    _l_(21525)

    result = _c_(21521, _n_(21511, "all", lambda: all), (_n_(21512, "nums", lambda: nums)[_n_(21513, "i", lambda: i)] <= _n_(21514, "nums", lambda: nums)[_n_(21515, "i", lambda: i) + 1] for i in _c_(21520, _n_(21516, "range", lambda: range), _c_(21519, _n_(21517, "len", lambda: len), _n_(21518, "nums", lambda: nums)) - 1)))
    _l_(21522)
    aux = _n_(21523, "result", lambda: result)
    _l_(21524)
    return aux
nums1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
_l_(21526)
_c_(21528, _n_(21527, "print", lambda: print), 'Original list:')
_l_(21529)
_c_(21532, _n_(21530, "print", lambda: print), _n_(21531, "nums1", lambda: nums1))
_l_(21533)
_c_(21535, _n_(21534, "print", lambda: print), '\nIs the said list is sorted!')
_l_(21536)
_c_(21541, _n_(21537, "print", lambda: print), _c_(21540, _n_(21538, "is_sort_list", lambda: is_sort_list), _n_(21539, "nums1", lambda: nums1)))
_l_(21542)
_c_(21544, _n_(21543, "print", lambda: print), '\nOriginal list:')
_l_(21545)
_c_(21548, _n_(21546, "print", lambda: print), _n_(21547, "nums1", lambda: nums1))
_l_(21549)
_c_(21551, _n_(21550, "print", lambda: print), '\nIs the said list is sorted!')
_l_(21552)
_c_(21557, _n_(21553, "print", lambda: print), _c_(21556, _n_(21554, "is_sort_list", lambda: is_sort_list), _n_(21555, "nums2", lambda: nums2)))
_l_(21558)