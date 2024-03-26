# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(105696)

except ImportError:
    pass
_c_(105698, _n_(105697, "print", lambda: print), 'Original array:')
_l_(105699)
_c_(105702, _n_(105700, "print", lambda: print), _n_(105701, "a", lambda: a))
_l_(105703)
unique_elements, counts_elements = _c_(105707, _a_(105705, _n_(105704, "np", lambda: np), "unique"), _n_(105706, "a", lambda: a), return_counts=True)
_l_(105708)
_c_(105710, _n_(105709, "print", lambda: print), 'Frequency of unique values of the said array:')
_l_(105711)
_c_(105718, _n_(105712, "print", lambda: print), _c_(105717, _a_(105714, _n_(105713, "np", lambda: np), "asarray"), (_n_(105715, "unique_elements", lambda: unique_elements), _n_(105716, "counts_elements", lambda: counts_elements))))
_l_(105719)