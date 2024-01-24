# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54232611/unexpected-type-error-using-numpy-save-and-savez
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy
    _l_(534501)

except ImportError:
    pass

test_path = "test.npy"
_l_(534502)
test_data = _c_(534506, _a_(534505, _a_(534504, _n_(534503, "numpy", lambda: numpy), "random"), "rand"), 100000)
_l_(534507)

with _c_(534510, _n_(534508, "open", lambda: open), _n_(534509, "test_path", lambda: test_path), 'w') as test_file:
    _l_(534517)

    _c_(534515, _a_(534512, _n_(534511, "numpy", lambda: numpy), "save"), _n_(534513, "test_file", lambda: test_file), _n_(534514, "test_data", lambda: test_data))
    _l_(534516)