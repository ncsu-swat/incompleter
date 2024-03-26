# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(115416)

except ImportError:
    pass
num_series = _c_(115421, _a_(115418, _n_(115417, "pd", lambda: pd), "Series"), _c_(115420, _n_(115419, "list", lambda: list), '2390238923902390239023'))
_l_(115422)
element_pos = [0, 2, 6, 11, 21]
_l_(115423)
_c_(115425, _n_(115424, "print", lambda: print), 'Original Series:')
_l_(115426)
_c_(115429, _n_(115427, "print", lambda: print), _n_(115428, "num_series", lambda: num_series))
_l_(115430)
_c_(115432, _n_(115431, "print", lambda: print), '\nExtract items at given positions of the said series:')
_l_(115433)
_c_(115436, _n_(115434, "print", lambda: print), _n_(115435, "result", lambda: result))
_l_(115437)