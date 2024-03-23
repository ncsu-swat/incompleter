# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import functools
    _l_(10114)

except ImportError:
    pass

def remove_duplicates(nums):
    _l_(10124)

    result = _c_(10120, _a_(10116, _n_(10115, "functools", lambda: functools), "reduce"), lambda x, y: _n_(10117, "x", lambda: x) * _n_(10118, "y", lambda: y), _n_(10119, "nums", lambda: nums), 1)
    _l_(10121)
    aux = _n_(10122, "result", lambda: result)
    _l_(10123)
    return aux
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(10125)
_c_(10128, _n_(10126, "print", lambda: print), 'list1:', _n_(10127, "nums1", lambda: nums1))
_l_(10129)
_c_(10131, _n_(10130, "print", lambda: print), 'Product of the said list numbers:')
_l_(10132)
_c_(10137, _n_(10133, "print", lambda: print), _c_(10136, _n_(10134, "remove_duplicates", lambda: remove_duplicates), _n_(10135, "nums1", lambda: nums1)))
_l_(10138)
_c_(10141, _n_(10139, "print", lambda: print), '\nlist2:', _n_(10140, "nums2", lambda: nums2))
_l_(10142)
_c_(10144, _n_(10143, "print", lambda: print), 'Product of the said list numbers:')
_l_(10145)
_c_(10150, _n_(10146, "print", lambda: print), _c_(10149, _n_(10147, "remove_duplicates", lambda: remove_duplicates), _n_(10148, "nums2", lambda: nums2)))
_l_(10151)