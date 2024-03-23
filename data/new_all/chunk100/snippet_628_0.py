# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(65510)

except ImportError:
    pass
A = _c_(65513, _a_(65512, _n_(65511, "np", lambda: np), "ones"), (3, 3))
_l_(65514)
_c_(65516, _n_(65515, "print", lambda: print), 'Original array:')
_l_(65517)
_c_(65519, _n_(65518, "print", lambda: print), 'Array-1')
_l_(65520)
_c_(65523, _n_(65521, "print", lambda: print), _n_(65522, "A", lambda: A))
_l_(65524)
_c_(65526, _n_(65525, "print", lambda: print), 'Array-2')
_l_(65527)
_c_(65530, _n_(65528, "print", lambda: print), _n_(65529, "B", lambda: B))
_l_(65531)
_c_(65533, _n_(65532, "print", lambda: print), 'A + B:')
_l_(65534)
new_array = _n_(65535, "A", lambda: A) + _n_(65536, "B", lambda: B)
_l_(65537)
_c_(65540, _n_(65538, "print", lambda: print), _n_(65539, "new_array", lambda: new_array))
_l_(65541)