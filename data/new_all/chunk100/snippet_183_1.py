# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(14520)

except ImportError:
    pass
_c_(14522, _n_(14521, "print", lambda: print), '\nOriginal arrays:')
_l_(14523)
x = _c_(14528, _a_(14527, _c_(14526, _a_(14525, _n_(14524, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(14529)
y = _n_(14530, "x", lambda: x) * 3
_l_(14531)
_c_(14533, _n_(14532, "print", lambda: print), 'Array-1')
_l_(14534)
_c_(14537, _n_(14535, "print", lambda: print), _n_(14536, "x", lambda: x))
_l_(14538)
_c_(14540, _n_(14539, "print", lambda: print), 'Array-2')
_l_(14541)
_c_(14544, _n_(14542, "print", lambda: print), _n_(14543, "y", lambda: y))
_l_(14545)
_c_(14547, _n_(14546, "print", lambda: print), '\nStack arrays in sequence horizontally:')
_l_(14548)
_c_(14551, _n_(14549, "print", lambda: print), _n_(14550, "new_array", lambda: new_array))
_l_(14552)