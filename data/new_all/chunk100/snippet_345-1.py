# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(111489)

except ImportError:
    pass
_c_(111491, _n_(111490, "print", lambda: print), 'Original array: ')
_l_(111492)
_c_(111495, _n_(111493, "print", lambda: print), _n_(111494, "x", lambda: x))
_l_(111496)
_c_(111498, _n_(111497, "print", lambda: print), 'Cumulative product  of the elements along a given axis:')
_l_(111499)
r = _c_(111503, _a_(111501, _n_(111500, "np", lambda: np), "cumprod"), _n_(111502, "x", lambda: x))
_l_(111504)
_c_(111507, _n_(111505, "print", lambda: print), _n_(111506, "r", lambda: r))
_l_(111508)
_c_(111510, _n_(111509, "print", lambda: print), '\nProduct over rows for each of the 3 columns:')
_l_(111511)
r = _c_(111515, _a_(111513, _n_(111512, "np", lambda: np), "cumprod"), _n_(111514, "x", lambda: x), axis=0)
_l_(111516)
_c_(111519, _n_(111517, "print", lambda: print), _n_(111518, "r", lambda: r))
_l_(111520)
_c_(111522, _n_(111521, "print", lambda: print), '\nProduct  over columns for each of the 2 rows:')
_l_(111523)
r = _c_(111527, _a_(111525, _n_(111524, "np", lambda: np), "cumprod"), _n_(111526, "x", lambda: x), axis=1)
_l_(111528)
_c_(111531, _n_(111529, "print", lambda: print), _n_(111530, "r", lambda: r))
_l_(111532)