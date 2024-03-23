# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(5678)

except ImportError:
    pass
_c_(5680, _n_(5679, "print", lambda: print), 'Original array:')
_l_(5681)
_c_(5684, _n_(5682, "print", lambda: print), _n_(5683, "x", lambda: x))
_l_(5685)
_c_(5687, _n_(5686, "print", lambda: print), 'Mean of each column:')
_l_(5688)
_c_(5693, _n_(5689, "print", lambda: print), _c_(5692, _a_(5691, _n_(5690, "x", lambda: x), "mean"), axis=0))
_l_(5694)
_c_(5696, _n_(5695, "print", lambda: print), 'Mean of each row:')
_l_(5697)
_c_(5702, _n_(5698, "print", lambda: print), _c_(5701, _a_(5700, _n_(5699, "x", lambda: x), "mean"), axis=1))
_l_(5703)