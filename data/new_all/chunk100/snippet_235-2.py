# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(106268)

except ImportError:
    pass
_c_(106270, _n_(106269, "print", lambda: print), '\nOriginal arrays:')
_l_(106271)
x = _c_(106274, _a_(106273, _n_(106272, "np", lambda: np), "array"), (1, 2, 3))
_l_(106275)
_c_(106277, _n_(106276, "print", lambda: print), 'Array-1')
_l_(106278)
_c_(106281, _n_(106279, "print", lambda: print), _n_(106280, "x", lambda: x))
_l_(106282)
_c_(106284, _n_(106283, "print", lambda: print), 'Array-2')
_l_(106285)
_c_(106288, _n_(106286, "print", lambda: print), _n_(106287, "y", lambda: y))
_l_(106289)
new_array = _c_(106294, _a_(106291, _n_(106290, "np", lambda: np), "row_stack"), (_n_(106292, "x", lambda: x), _n_(106293, "y", lambda: y)))
_l_(106295)
_c_(106297, _n_(106296, "print", lambda: print), '\nStack 1-D arrays as rows wise:')
_l_(106298)
_c_(106301, _n_(106299, "print", lambda: print), _n_(106300, "new_array", lambda: new_array))
_l_(106302)