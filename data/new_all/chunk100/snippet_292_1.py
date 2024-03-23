# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(24896)

except ImportError:
    pass
_c_(24898, _n_(24897, "print", lambda: print), 'Original array and shape:')
_l_(24899)
_c_(24902, _n_(24900, "print", lambda: print), _n_(24901, "a", lambda: a))
_l_(24903)
_c_(24907, _n_(24904, "print", lambda: print), _a_(24906, _n_(24905, "a", lambda: a), "shape"))
_l_(24908)
_c_(24910, _n_(24909, "print", lambda: print), '--------------------------------')
_l_(24911)
tidx = _c_(24915, _a_(24914, _a_(24913, _n_(24912, "np", lambda: np), "random"), "randint"), 0, 3, 4)
_l_(24916)
_c_(24919, _n_(24917, "print", lambda: print), 'tidex: ', _n_(24918, "tidx", lambda: tidx))
_l_(24920)
_c_(24922, _n_(24921, "print", lambda: print), 'Result:')
_l_(24923)
_c_(24933, _n_(24924, "print", lambda: print), _n_(24925, "a", lambda: a)[_n_(24926, "tidx", lambda: tidx), _c_(24932, _a_(24928, _n_(24927, "np", lambda: np), "arange"), _c_(24931, _n_(24929, "len", lambda: len), _n_(24930, "tidx", lambda: tidx))), :])
_l_(24934)