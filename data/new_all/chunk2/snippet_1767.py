# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57318922/typeerror-argument-x-has-incorrect-type-expected-cupy-core-core-ndarray-got
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy, cupy, cupyx
    _l_(464734)

except ImportError:
    pass

_c_(464739, _n_(464735, "print", lambda: print), _c_(464738, _a_(464737, _n_(464736, "cupyx", lambda: cupyx), "get_runtime_info")) )
_l_(464740)

mydata = _c_(464743, _a_(464742, _n_(464741, "numpy", lambda: numpy), "empty"), (3,), dtype='f')
_l_(464744)

#gpu = False
gpu = True
_l_(464745)
if not _n_(464746, "gpu", lambda: gpu):
    _l_(464756)

    xp = _n_(464747, "numpy", lambda: numpy)
    _l_(464748)
else:
    xp = _n_(464749, "cupy", lambda: cupy)
    _l_(464750)

    mydata_like = _c_(464754, _a_(464752, _n_(464751, "xp", lambda: xp), "zeros_like"), _n_(464753, "mydata", lambda: mydata))
    _l_(464755)