# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49566391/nameerror-for-importing-random-and-numpy-random-but-nothing-else
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numpy.random import uniform
    _l_(537401)

except ImportError:
    pass
sample = [_c_(537403, _n_(537402, "uniform", lambda: uniform)) for item in [1,2,3]]
_l_(537404)