# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(108800)

except ImportError:
    pass
a = _c_(108804, _a_(108803, _a_(108802, _n_(108801, "np", lambda: np), "random"), "randint"), 0, 10, (3, 4, 8))
_l_(108805)
_c_(108807, _n_(108806, "print", lambda: print), 'Original array and shape:')
_l_(108808)
_c_(108811, _n_(108809, "print", lambda: print), _n_(108810, "a", lambda: a))
_l_(108812)
_c_(108816, _n_(108813, "print", lambda: print), _a_(108815, _n_(108814, "a", lambda: a), "shape"))
_l_(108817)
_c_(108819, _n_(108818, "print", lambda: print), '--------------------------------')
_l_(108820)
_c_(108823, _n_(108821, "print", lambda: print), 'tidex: ', _n_(108822, "tidx", lambda: tidx))
_l_(108824)
_c_(108826, _n_(108825, "print", lambda: print), 'Result:')
_l_(108827)
_c_(108837, _n_(108828, "print", lambda: print), _n_(108829, "a", lambda: a)[_n_(108830, "tidx", lambda: tidx), _c_(108836, _a_(108832, _n_(108831, "np", lambda: np), "arange"), _c_(108835, _n_(108833, "len", lambda: len), _n_(108834, "tidx", lambda: tidx))), :])
_l_(108838)