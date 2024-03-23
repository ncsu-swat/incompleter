# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import functools
    _l_(10153)

except ImportError:
    pass

def remove_duplicates(nums):
    _l_(10163)

    result = _c_(10159, _a_(10155, _n_(10154, "functools", lambda: functools), "reduce"), lambda x, y: _n_(10156, "x", lambda: x) * _n_(10157, "y", lambda: y), _n_(10158, "nums", lambda: nums), 1)
    _l_(10160)
    aux = _n_(10161, "result", lambda: result)
    _l_(10162)
    return aux
nums2 = [2.2, 4.12, 6.6, 8.1, 8.3]
_l_(10164)
_c_(10167, _n_(10165, "print", lambda: print), 'list1:', _n_(10166, "nums1", lambda: nums1))
_l_(10168)
_c_(10170, _n_(10169, "print", lambda: print), 'Product of the said list numbers:')
_l_(10171)
_c_(10176, _n_(10172, "print", lambda: print), _c_(10175, _n_(10173, "remove_duplicates", lambda: remove_duplicates), _n_(10174, "nums1", lambda: nums1)))
_l_(10177)
_c_(10180, _n_(10178, "print", lambda: print), '\nlist2:', _n_(10179, "nums2", lambda: nums2))
_l_(10181)
_c_(10183, _n_(10182, "print", lambda: print), 'Product of the said list numbers:')
_l_(10184)
_c_(10189, _n_(10185, "print", lambda: print), _c_(10188, _n_(10186, "remove_duplicates", lambda: remove_duplicates), _n_(10187, "nums2", lambda: nums2)))
_l_(10190)