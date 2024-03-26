# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def diff_consecutive_nums(nums):
    _l_(118349)

    result = [_n_(118340, "b", lambda: b) - _n_(118341, "a", lambda: a) for a, b in _c_(118345, _n_(118342, "zip", lambda: zip), _n_(118343, "nums", lambda: nums)[:-1], _n_(118344, "nums", lambda: nums)[1:])]
    _l_(118346)
    aux = _n_(118347, "result", lambda: result)
    _l_(118348)
    return aux
_c_(118351, _n_(118350, "print", lambda: print), 'Original list:')
_l_(118352)
_c_(118355, _n_(118353, "print", lambda: print), _n_(118354, "nums1", lambda: nums1))
_l_(118356)
_c_(118358, _n_(118357, "print", lambda: print), 'Difference between consecutive numbers of the said list:')
_l_(118359)
_c_(118364, _n_(118360, "print", lambda: print), _c_(118363, _n_(118361, "diff_consecutive_nums", lambda: diff_consecutive_nums), _n_(118362, "nums1", lambda: nums1)))
_l_(118365)
nums2 = [4, 5, 8, 9, 6, 10]
_l_(118366)
_c_(118368, _n_(118367, "print", lambda: print), '\nOriginal list:')
_l_(118369)
_c_(118372, _n_(118370, "print", lambda: print), _n_(118371, "nums2", lambda: nums2))
_l_(118373)
_c_(118375, _n_(118374, "print", lambda: print), 'Difference between consecutive numbers of the said list:')
_l_(118376)
_c_(118381, _n_(118377, "print", lambda: print), _c_(118380, _n_(118378, "diff_consecutive_nums", lambda: diff_consecutive_nums), _n_(118379, "nums2", lambda: nums2)))
_l_(118382)