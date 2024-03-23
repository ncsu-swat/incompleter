# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(24856)

except ImportError:
    pass
a = _c_(24860, _a_(24859, _a_(24858, _n_(24857, "np", lambda: np), "random"), "randint"), 0, 10, (3, 4, 8))
_l_(24861)
_c_(24863, _n_(24862, "print", lambda: print), 'Original array and shape:')
_l_(24864)
_c_(24867, _n_(24865, "print", lambda: print), _n_(24866, "a", lambda: a))
_l_(24868)
_c_(24872, _n_(24869, "print", lambda: print), _a_(24871, _n_(24870, "a", lambda: a), "shape"))
_l_(24873)
_c_(24875, _n_(24874, "print", lambda: print), '--------------------------------')
_l_(24876)
_c_(24879, _n_(24877, "print", lambda: print), 'tidex: ', _n_(24878, "tidx", lambda: tidx))
_l_(24880)
_c_(24882, _n_(24881, "print", lambda: print), 'Result:')
_l_(24883)
_c_(24893, _n_(24884, "print", lambda: print), _n_(24885, "a", lambda: a)[_n_(24886, "tidx", lambda: tidx), _c_(24892, _a_(24888, _n_(24887, "np", lambda: np), "arange"), _c_(24891, _n_(24889, "len", lambda: len), _n_(24890, "tidx", lambda: tidx))), :])
_l_(24894)