# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(76901)

except ImportError:
    pass
nums1 = _c_(76907, _a_(76904, _a_(76903, _n_(76902, "np", lambda: np), "random"), "randint"), low=0, high=256, size=(200, 300, 3), dtype=_a_(76906, _n_(76905, "np", lambda: np), "uint8"))
_l_(76908)
nums2 = _c_(76914, _a_(76911, _a_(76910, _n_(76909, "np", lambda: np), "random"), "randint"), low=0, high=256, size=(200, 300, 3), dtype=_a_(76913, _n_(76912, "np", lambda: np), "uint8"))
_l_(76915)
_c_(76917, _n_(76916, "print", lambda: print), 'Array1:')
_l_(76918)
_c_(76921, _n_(76919, "print", lambda: print), _n_(76920, "nums1", lambda: nums1))
_l_(76922)
_c_(76924, _n_(76923, "print", lambda: print), '\nArray2:')
_l_(76925)
_c_(76928, _n_(76926, "print", lambda: print), _n_(76927, "nums2", lambda: nums2))
_l_(76929)
nums1 = _c_(76933, _a_(76931, _n_(76930, "np", lambda: np), "expand_dims"), _n_(76932, "nums1", lambda: nums1), axis=0)
_l_(76934)
nums = _c_(76939, _a_(76936, _n_(76935, "np", lambda: np), "append"), _n_(76937, "nums1", lambda: nums1), _n_(76938, "nums2", lambda: nums2), axis=0)
_l_(76940)
_c_(76942, _n_(76941, "print", lambda: print), '\nCombined array:')
_l_(76943)
_c_(76946, _n_(76944, "print", lambda: print), _n_(76945, "nums", lambda: nums))
_l_(76947)