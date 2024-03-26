# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(111010)

except ImportError:
    pass
_c_(111012, _n_(111011, "print", lambda: print), 'Original array:')
_l_(111013)
_c_(111016, _n_(111014, "print", lambda: print), _n_(111015, "array_nums", lambda: array_nums))
_l_(111017)
_c_(111019, _n_(111018, "print", lambda: print), '\nAfter reversing:')
_l_(111020)
_n_(111021, "array_nums", lambda: array_nums)[:] = _n_(111022, "array_nums", lambda: array_nums)[3::-1]
_l_(111023)
_c_(111026, _n_(111024, "print", lambda: print), _n_(111025, "array_nums", lambda: array_nums))
_l_(111027)