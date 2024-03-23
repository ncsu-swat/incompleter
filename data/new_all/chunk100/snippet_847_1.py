# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(84267)

except ImportError:
    pass
arr1 = _c_(84271, _a_(84270, _a_(84269, _n_(84268, "np", lambda: np), "random"), "random"), size=(25, 25, 1))
_l_(84272)
arr3 = _c_(84276, _a_(84275, _a_(84274, _n_(84273, "np", lambda: np), "random"), "random"), size=(25, 25, 1))
_l_(84277)
_c_(84279, _n_(84278, "print", lambda: print), 'Original arrays:')
_l_(84280)
_c_(84283, _n_(84281, "print", lambda: print), _n_(84282, "arr1", lambda: arr1))
_l_(84284)
_c_(84287, _n_(84285, "print", lambda: print), _n_(84286, "arr2", lambda: arr2))
_l_(84288)
_c_(84291, _n_(84289, "print", lambda: print), _n_(84290, "arr3", lambda: arr3))
_l_(84292)
result = _c_(84298, _a_(84294, _n_(84293, "np", lambda: np), "concatenate"), (_n_(84295, "arr1", lambda: arr1), _n_(84296, "arr2", lambda: arr2), _n_(84297, "arr3", lambda: arr3)), axis=-1)
_l_(84299)
_c_(84301, _n_(84300, "print", lambda: print), '\nAfter concatenate:')
_l_(84302)
_c_(84305, _n_(84303, "print", lambda: print), _n_(84304, "result", lambda: result))
_l_(84306)