# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(98336)

except ImportError:
    pass
x = _c_(98341, _a_(98340, _c_(98339, _a_(98338, _n_(98337, "np", lambda: np), "arange"), 16), "reshape"), 4, 4)
_l_(98342)
_c_(98344, _n_(98343, "print", lambda: print), 'Original arrays:')
_l_(98345)
_c_(98348, _n_(98346, "print", lambda: print), _n_(98347, "x", lambda: x))
_l_(98349)
_c_(98351, _n_(98350, "print", lambda: print), '\nArray with size 2x2 from the said array:')
_l_(98352)
new_array1 = _c_(98356, _a_(98354, _n_(98353, "np", lambda: np), "resize"), _n_(98355, "x", lambda: x), (2, 2))
_l_(98357)
_c_(98360, _n_(98358, "print", lambda: print), _n_(98359, "new_array1", lambda: new_array1))
_l_(98361)
_c_(98363, _n_(98362, "print", lambda: print), '\nArray with size 6x6 from the said array:')
_l_(98364)
_c_(98367, _n_(98365, "print", lambda: print), _n_(98366, "new_array2", lambda: new_array2))
_l_(98368)