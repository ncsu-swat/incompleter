# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums2 = [4, 5, 6]
_l_(49044)
_c_(49046, _n_(49045, "print", lambda: print), 'Original list:')
_l_(49047)
_c_(49050, _n_(49048, "print", lambda: print), _n_(49049, "nums1", lambda: nums1))
_l_(49051)
_c_(49054, _n_(49052, "print", lambda: print), _n_(49053, "nums2", lambda: nums2))
_l_(49055)
result = _c_(49061, _n_(49056, "map", lambda: map), lambda x, y: _n_(49057, "x", lambda: x) + _n_(49058, "y", lambda: y), _n_(49059, "nums1", lambda: nums1), _n_(49060, "nums2", lambda: nums2))
_l_(49062)
_c_(49064, _n_(49063, "print", lambda: print), '\nResult: after adding two list')
_l_(49065)
_c_(49070, _n_(49066, "print", lambda: print), _c_(49069, _n_(49067, "list", lambda: list), _n_(49068, "result", lambda: result)))
_l_(49071)