# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums1 = [1, 2, 3]
_l_(117305)
_c_(117307, _n_(117306, "print", lambda: print), 'Original list:')
_l_(117308)
_c_(117311, _n_(117309, "print", lambda: print), _n_(117310, "nums1", lambda: nums1))
_l_(117312)
_c_(117315, _n_(117313, "print", lambda: print), _n_(117314, "nums2", lambda: nums2))
_l_(117316)
result = _c_(117322, _n_(117317, "map", lambda: map), lambda x, y: _n_(117318, "x", lambda: x) + _n_(117319, "y", lambda: y), _n_(117320, "nums1", lambda: nums1), _n_(117321, "nums2", lambda: nums2))
_l_(117323)
_c_(117325, _n_(117324, "print", lambda: print), '\nResult: after adding two list')
_l_(117326)
_c_(117331, _n_(117327, "print", lambda: print), _c_(117330, _n_(117328, "list", lambda: list), _n_(117329, "result", lambda: result)))
_l_(117332)