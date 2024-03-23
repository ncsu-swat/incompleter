# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(17295)

except ImportError:
    pass
_c_(17297, _n_(17296, "print", lambda: print), 'Original array:')
_l_(17298)
_c_(17301, _n_(17299, "print", lambda: print), _n_(17300, "a", lambda: a))
_l_(17302)
(unique_elements, counts_elements) = _c_(17306, _a_(17304, _n_(17303, "np", lambda: np), "unique"), _n_(17305, "a", lambda: a), return_counts=True)
_l_(17307)
_c_(17309, _n_(17308, "print", lambda: print), 'Frequency of unique values of the said array:')
_l_(17310)
_c_(17317, _n_(17311, "print", lambda: print), _c_(17316, _a_(17313, _n_(17312, "np", lambda: np), "asarray"), (_n_(17314, "unique_elements", lambda: unique_elements), _n_(17315, "counts_elements", lambda: counts_elements))))
_l_(17318)