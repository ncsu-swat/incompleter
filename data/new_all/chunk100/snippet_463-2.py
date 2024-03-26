# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums2 = [4, 5, 6]
_l_(117355)
_c_(117357, _n_(117356, "print", lambda: print), 'Original list:')
_l_(117358)
_c_(117361, _n_(117359, "print", lambda: print), _n_(117360, "nums1", lambda: nums1))
_l_(117362)
_c_(117365, _n_(117363, "print", lambda: print), _n_(117364, "nums2", lambda: nums2))
_l_(117366)
result = _c_(117372, _n_(117367, "map", lambda: map), lambda x, y: _n_(117368, "x", lambda: x) + _n_(117369, "y", lambda: y), _n_(117370, "nums1", lambda: nums1), _n_(117371, "nums2", lambda: nums2))
_l_(117373)
_c_(117375, _n_(117374, "print", lambda: print), '\nResult: after adding two list')
_l_(117376)
_c_(117381, _n_(117377, "print", lambda: print), _c_(117380, _n_(117378, "list", lambda: list), _n_(117379, "result", lambda: result)))
_l_(117382)