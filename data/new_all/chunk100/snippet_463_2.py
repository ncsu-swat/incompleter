# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums1 = [1, 2, 3]
_l_(49072)
_c_(49074, _n_(49073, "print", lambda: print), 'Original list:')
_l_(49075)
_c_(49078, _n_(49076, "print", lambda: print), _n_(49077, "nums1", lambda: nums1))
_l_(49079)
_c_(49082, _n_(49080, "print", lambda: print), _n_(49081, "nums2", lambda: nums2))
_l_(49083)
result = _c_(49089, _n_(49084, "map", lambda: map), lambda x, y: _n_(49085, "x", lambda: x) + _n_(49086, "y", lambda: y), _n_(49087, "nums1", lambda: nums1), _n_(49088, "nums2", lambda: nums2))
_l_(49090)
_c_(49092, _n_(49091, "print", lambda: print), '\nResult: after adding two list')
_l_(49093)
_c_(49098, _n_(49094, "print", lambda: print), _c_(49097, _n_(49095, "list", lambda: list), _n_(49096, "result", lambda: result)))
_l_(49099)