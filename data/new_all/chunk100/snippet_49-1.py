# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def diff_consecutive_nums(nums):
    _l_(118392)

    result = [_n_(118383, "b", lambda: b) - _n_(118384, "a", lambda: a) for a, b in _c_(118388, _n_(118385, "zip", lambda: zip), _n_(118386, "nums", lambda: nums)[:-1], _n_(118387, "nums", lambda: nums)[1:])]
    _l_(118389)
    aux = _n_(118390, "result", lambda: result)
    _l_(118391)
    return aux
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
_l_(118393)
_c_(118395, _n_(118394, "print", lambda: print), 'Original list:')
_l_(118396)
_c_(118399, _n_(118397, "print", lambda: print), _n_(118398, "nums1", lambda: nums1))
_l_(118400)
_c_(118402, _n_(118401, "print", lambda: print), 'Difference between consecutive numbers of the said list:')
_l_(118403)
_c_(118408, _n_(118404, "print", lambda: print), _c_(118407, _n_(118405, "diff_consecutive_nums", lambda: diff_consecutive_nums), _n_(118406, "nums1", lambda: nums1)))
_l_(118409)
_c_(118411, _n_(118410, "print", lambda: print), '\nOriginal list:')
_l_(118412)
_c_(118415, _n_(118413, "print", lambda: print), _n_(118414, "nums2", lambda: nums2))
_l_(118416)
_c_(118418, _n_(118417, "print", lambda: print), 'Difference between consecutive numbers of the said list:')
_l_(118419)
_c_(118424, _n_(118420, "print", lambda: print), _c_(118423, _n_(118421, "diff_consecutive_nums", lambda: diff_consecutive_nums), _n_(118422, "nums2", lambda: nums2)))
_l_(118425)