# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cast_list(val):
    _l_(104383)

    aux = _c_(104373, _n_(104371, "list", lambda: list), _n_(104372, "val", lambda: val)) if _c_(104380, _n_(104374, "isinstance", lambda: isinstance), _n_(104375, "val", lambda: val), (_n_(104376, "tuple", lambda: tuple), _n_(104377, "list", lambda: list), _n_(104378, "set", lambda: set), _n_(104379, "dict", lambda: dict))) else [_n_(104381, "val", lambda: val)]
    _l_(104382)
    return aux
d1 = [1]
_l_(104384)
_c_(104389, _n_(104385, "print", lambda: print), _c_(104388, _n_(104386, "type", lambda: type), _n_(104387, "d1", lambda: d1)))
_l_(104390)
_c_(104395, _n_(104391, "print", lambda: print), _c_(104394, _n_(104392, "cast_list", lambda: cast_list), _n_(104393, "d1", lambda: d1)))
_l_(104396)
d2 = ('Red', 'Green')
_l_(104397)
_c_(104402, _n_(104398, "print", lambda: print), _c_(104401, _n_(104399, "type", lambda: type), _n_(104400, "d2", lambda: d2)))
_l_(104403)
_c_(104408, _n_(104404, "print", lambda: print), _c_(104407, _n_(104405, "cast_list", lambda: cast_list), _n_(104406, "d2", lambda: d2)))
_l_(104409)
_c_(104414, _n_(104410, "print", lambda: print), _c_(104413, _n_(104411, "type", lambda: type), _n_(104412, "d3", lambda: d3)))
_l_(104415)
_c_(104420, _n_(104416, "print", lambda: print), _c_(104419, _n_(104417, "cast_list", lambda: cast_list), _n_(104418, "d3", lambda: d3)))
_l_(104421)
d4 = {1: 'Red', 2: 'Green', 3: 'Black'}
_l_(104422)
_c_(104427, _n_(104423, "print", lambda: print), _c_(104426, _n_(104424, "type", lambda: type), _n_(104425, "d4", lambda: d4)))
_l_(104428)
_c_(104433, _n_(104429, "print", lambda: print), _c_(104432, _n_(104430, "cast_list", lambda: cast_list), _n_(104431, "d4", lambda: d4)))
_l_(104434)