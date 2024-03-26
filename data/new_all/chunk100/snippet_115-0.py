# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(100927)

except ImportError:
    pass
_c_(100929, _n_(100928, "print", lambda: print), 'Original array:')
_l_(100930)
_c_(100933, _n_(100931, "print", lambda: print), _n_(100932, "array_nums", lambda: array_nums))
_l_(100934)
_c_(100936, _n_(100935, "print", lambda: print), '\nNew array of shape(5, 4):')
_l_(100937)
new_array = _c_(100940, _a_(100939, _n_(100938, "array_nums", lambda: array_nums), "reshape"), 5, 4)
_l_(100941)
_c_(100944, _n_(100942, "print", lambda: print), _n_(100943, "new_array", lambda: new_array))
_l_(100945)
_c_(100947, _n_(100946, "print", lambda: print), '\nRestore the reshaped array into a 1-D array:')
_l_(100948)
_c_(100953, _n_(100949, "print", lambda: print), _c_(100952, _a_(100951, _n_(100950, "new_array", lambda: new_array), "flatten")))
_l_(100954)