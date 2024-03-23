# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(82823)

except ImportError:
    pass
_c_(82825, _n_(82824, "print", lambda: print), 'Original arrays:')
_l_(82826)
_c_(82829, _n_(82827, "print", lambda: print), _n_(82828, "arra1", lambda: arra1))
_l_(82830)
_c_(82832, _n_(82831, "print", lambda: print), '\nRecord array;')
_l_(82833)
result = _c_(82840, _a_(82837, _a_(82836, _a_(82835, _n_(82834, "np", lambda: np), "core"), "records"), "fromarrays"), _a_(82839, _n_(82838, "arra1", lambda: arra1), "T"), names='col1, col2, col3', formats='S80, f8, i8')
_l_(82841)
_c_(82844, _n_(82842, "print", lambda: print), _n_(82843, "result", lambda: result))
_l_(82845)