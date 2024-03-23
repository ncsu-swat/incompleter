# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(92493)

except ImportError:
    pass
y = _c_(92496, _a_(92495, _n_(92494, "np", lambda: np), "array"), [2, 3, 4])
_l_(92497)
_c_(92499, _n_(92498, "print", lambda: print), 'Original arrays:')
_l_(92500)
_c_(92503, _n_(92501, "print", lambda: print), _n_(92502, "x", lambda: x))
_l_(92504)
_c_(92507, _n_(92505, "print", lambda: print), _n_(92506, "y", lambda: y))
_l_(92508)
_c_(92510, _n_(92509, "print", lambda: print), 'Sequence of arrays along a new axis:')
_l_(92511)
_c_(92518, _n_(92512, "print", lambda: print), _c_(92517, _a_(92514, _n_(92513, "np", lambda: np), "vstack"), (_n_(92515, "x", lambda: x), _n_(92516, "y", lambda: y))))
_l_(92519)
x = _c_(92522, _a_(92521, _n_(92520, "np", lambda: np), "array"), [[1], [2], [3]])
_l_(92523)
y = _c_(92526, _a_(92525, _n_(92524, "np", lambda: np), "array"), [[2], [3], [4]])
_l_(92527)
_c_(92529, _n_(92528, "print", lambda: print), '\nOriginal arrays:')
_l_(92530)
_c_(92533, _n_(92531, "print", lambda: print), _n_(92532, "x", lambda: x))
_l_(92534)
_c_(92536, _n_(92535, "print", lambda: print))
_l_(92537)
_c_(92540, _n_(92538, "print", lambda: print), _n_(92539, "y", lambda: y))
_l_(92541)
_c_(92543, _n_(92542, "print", lambda: print), 'Sequence of arrays along a new axis:')
_l_(92544)
_c_(92551, _n_(92545, "print", lambda: print), _c_(92550, _a_(92547, _n_(92546, "np", lambda: np), "vstack"), (_n_(92548, "x", lambda: x), _n_(92549, "y", lambda: y))))
_l_(92552)