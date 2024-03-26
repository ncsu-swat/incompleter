# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(108840)

except ImportError:
    pass
_c_(108842, _n_(108841, "print", lambda: print), 'Original array and shape:')
_l_(108843)
_c_(108846, _n_(108844, "print", lambda: print), _n_(108845, "a", lambda: a))
_l_(108847)
_c_(108851, _n_(108848, "print", lambda: print), _a_(108850, _n_(108849, "a", lambda: a), "shape"))
_l_(108852)
_c_(108854, _n_(108853, "print", lambda: print), '--------------------------------')
_l_(108855)
tidx = _c_(108859, _a_(108858, _a_(108857, _n_(108856, "np", lambda: np), "random"), "randint"), 0, 3, 4)
_l_(108860)
_c_(108863, _n_(108861, "print", lambda: print), 'tidex: ', _n_(108862, "tidx", lambda: tidx))
_l_(108864)
_c_(108866, _n_(108865, "print", lambda: print), 'Result:')
_l_(108867)
_c_(108877, _n_(108868, "print", lambda: print), _n_(108869, "a", lambda: a)[_n_(108870, "tidx", lambda: tidx), _c_(108876, _a_(108872, _n_(108871, "np", lambda: np), "arange"), _c_(108875, _n_(108873, "len", lambda: len), _n_(108874, "tidx", lambda: tidx))), :])
_l_(108878)