# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(53335)

except ImportError:
    pass
_c_(53337, _n_(53336, "print", lambda: print), 'Original array:')
_l_(53338)
_c_(53341, _n_(53339, "print", lambda: print), _n_(53340, "nums", lambda: nums))
_l_(53342)
_c_(53344, _n_(53343, "print", lambda: print), '\nDelete the first column of the said array:')
_l_(53345)
_c_(53351, _n_(53346, "print", lambda: print), _c_(53350, _a_(53348, _n_(53347, "np", lambda: np), "delete"), _n_(53349, "nums", lambda: nums), [0], axis=1))
_l_(53352)
_c_(53354, _n_(53353, "print", lambda: print), '\nDelete the last column of the said array:')
_l_(53355)
_c_(53361, _n_(53356, "print", lambda: print), _c_(53360, _a_(53358, _n_(53357, "np", lambda: np), "delete"), _n_(53359, "nums", lambda: nums), [4], axis=1))
_l_(53362)