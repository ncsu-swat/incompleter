# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(119399)

except ImportError:
    pass
_c_(119401, _n_(119400, "print", lambda: print), 'Create an array of zeros')
_l_(119402)
_c_(119404, _n_(119403, "print", lambda: print), 'Default type is float')
_l_(119405)
_c_(119408, _n_(119406, "print", lambda: print), _n_(119407, "x", lambda: x))
_l_(119409)
_c_(119411, _n_(119410, "print", lambda: print), 'Type changes to int')
_l_(119412)
x = _c_(119417, _a_(119414, _n_(119413, "np", lambda: np), "zeros"), (1, 2), dtype=_a_(119416, _n_(119415, "np", lambda: np), "int"))
_l_(119418)
_c_(119421, _n_(119419, "print", lambda: print), _n_(119420, "x", lambda: x))
_l_(119422)
_c_(119424, _n_(119423, "print", lambda: print), 'Create an array of ones')
_l_(119425)
y = _c_(119428, _a_(119427, _n_(119426, "np", lambda: np), "ones"), (1, 2))
_l_(119429)
_c_(119431, _n_(119430, "print", lambda: print), 'Default type is float')
_l_(119432)
_c_(119435, _n_(119433, "print", lambda: print), _n_(119434, "y", lambda: y))
_l_(119436)
_c_(119438, _n_(119437, "print", lambda: print), 'Type changes to int')
_l_(119439)
y = _c_(119444, _a_(119441, _n_(119440, "np", lambda: np), "ones"), (1, 2), dtype=_a_(119443, _n_(119442, "np", lambda: np), "int"))
_l_(119445)
_c_(119448, _n_(119446, "print", lambda: print), _n_(119447, "y", lambda: y))
_l_(119449)