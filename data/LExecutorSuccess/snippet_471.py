# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/432112/is-there-a-numpy-function-to-return-the-first-index-of-something-in-an-array
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
sequence_of_arrays = [[0, 1], [1, 2], [-5, 0]]
_l_(1543738)
arrays_to_query = [[-5, 0], [1, 0]]
_l_(1543739)
try:
    import numpy_indexed as npi
    _l_(1543741)

except ImportError:
    pass
idx = _c_(1543746, _a_(1543743, _n_(1543742, "npi", lambda: npi), "indices"), _n_(1543744, "sequence_of_arrays", lambda: sequence_of_arrays), _n_(1543745, "arrays_to_query", lambda: arrays_to_query), missing=-1)
_l_(1543747)
_c_(1543750, _n_(1543748, "print", lambda: print), _n_(1543749, "idx", lambda: idx))   # [2, -1]
_l_(1543751)   # [2, -1]

