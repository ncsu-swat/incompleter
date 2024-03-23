# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(44211)

except ImportError:
    pass
_c_(44213, _n_(44212, "print", lambda: print), 'Original array')
_l_(44214)
_c_(44217, _n_(44215, "print", lambda: print), _n_(44216, "a", lambda: a))
_l_(44218)
_c_(44220, _n_(44219, "print", lambda: print), 'Checking for complex number:')
_l_(44221)
_c_(44227, _n_(44222, "print", lambda: print), _c_(44226, _a_(44224, _n_(44223, "np", lambda: np), "iscomplex"), _n_(44225, "a", lambda: a)))
_l_(44228)
_c_(44230, _n_(44229, "print", lambda: print), 'Checking for real number:')
_l_(44231)
_c_(44237, _n_(44232, "print", lambda: print), _c_(44236, _a_(44234, _n_(44233, "np", lambda: np), "isreal"), _n_(44235, "a", lambda: a)))
_l_(44238)
_c_(44240, _n_(44239, "print", lambda: print), 'Checking for scalar type:')
_l_(44241)
_c_(44246, _n_(44242, "print", lambda: print), _c_(44245, _a_(44244, _n_(44243, "np", lambda: np), "isscalar"), 3.1))
_l_(44247)
_c_(44252, _n_(44248, "print", lambda: print), _c_(44251, _a_(44250, _n_(44249, "np", lambda: np), "isscalar"), [3.1]))
_l_(44253)