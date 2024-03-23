# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(84308)

except ImportError:
    pass
arr1 = _c_(84312, _a_(84311, _a_(84310, _n_(84309, "np", lambda: np), "random"), "random"), size=(25, 25, 1))
_l_(84313)
arr2 = _c_(84317, _a_(84316, _a_(84315, _n_(84314, "np", lambda: np), "random"), "random"), size=(25, 25, 1))
_l_(84318)
_c_(84320, _n_(84319, "print", lambda: print), 'Original arrays:')
_l_(84321)
_c_(84324, _n_(84322, "print", lambda: print), _n_(84323, "arr1", lambda: arr1))
_l_(84325)
_c_(84328, _n_(84326, "print", lambda: print), _n_(84327, "arr2", lambda: arr2))
_l_(84329)
_c_(84332, _n_(84330, "print", lambda: print), _n_(84331, "arr3", lambda: arr3))
_l_(84333)
result = _c_(84339, _a_(84335, _n_(84334, "np", lambda: np), "concatenate"), (_n_(84336, "arr1", lambda: arr1), _n_(84337, "arr2", lambda: arr2), _n_(84338, "arr3", lambda: arr3)), axis=-1)
_l_(84340)
_c_(84342, _n_(84341, "print", lambda: print), '\nAfter concatenate:')
_l_(84343)
_c_(84346, _n_(84344, "print", lambda: print), _n_(84345, "result", lambda: result))
_l_(84347)