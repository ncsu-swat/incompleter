# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(116203)

except ImportError:
    pass
_c_(116205, _n_(116204, "print", lambda: print), 'Original array')
_l_(116206)
_c_(116209, _n_(116207, "print", lambda: print), _n_(116208, "a", lambda: a))
_l_(116210)
_c_(116212, _n_(116211, "print", lambda: print), 'Checking for complex number:')
_l_(116213)
_c_(116219, _n_(116214, "print", lambda: print), _c_(116218, _a_(116216, _n_(116215, "np", lambda: np), "iscomplex"), _n_(116217, "a", lambda: a)))
_l_(116220)
_c_(116222, _n_(116221, "print", lambda: print), 'Checking for real number:')
_l_(116223)
_c_(116229, _n_(116224, "print", lambda: print), _c_(116228, _a_(116226, _n_(116225, "np", lambda: np), "isreal"), _n_(116227, "a", lambda: a)))
_l_(116230)
_c_(116232, _n_(116231, "print", lambda: print), 'Checking for scalar type:')
_l_(116233)
_c_(116238, _n_(116234, "print", lambda: print), _c_(116237, _a_(116236, _n_(116235, "np", lambda: np), "isscalar"), 3.1))
_l_(116239)
_c_(116244, _n_(116240, "print", lambda: print), _c_(116243, _a_(116242, _n_(116241, "np", lambda: np), "isscalar"), [3.1]))
_l_(116245)