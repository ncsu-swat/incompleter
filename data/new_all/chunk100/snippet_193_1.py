# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cast_list(val):
    _l_(15390)

    aux = _c_(15380, _n_(15378, "list", lambda: list), _n_(15379, "val", lambda: val)) if _c_(15387, _n_(15381, "isinstance", lambda: isinstance), _n_(15382, "val", lambda: val), (_n_(15383, "tuple", lambda: tuple), _n_(15384, "list", lambda: list), _n_(15385, "set", lambda: set), _n_(15386, "dict", lambda: dict))) else [_n_(15388, "val", lambda: val)]
    _l_(15389)
    return aux
d1 = [1]
_l_(15391)
_c_(15396, _n_(15392, "print", lambda: print), _c_(15395, _n_(15393, "type", lambda: type), _n_(15394, "d1", lambda: d1)))
_l_(15397)
_c_(15402, _n_(15398, "print", lambda: print), _c_(15401, _n_(15399, "cast_list", lambda: cast_list), _n_(15400, "d1", lambda: d1)))
_l_(15403)
_c_(15408, _n_(15404, "print", lambda: print), _c_(15407, _n_(15405, "type", lambda: type), _n_(15406, "d2", lambda: d2)))
_l_(15409)
_c_(15414, _n_(15410, "print", lambda: print), _c_(15413, _n_(15411, "cast_list", lambda: cast_list), _n_(15412, "d2", lambda: d2)))
_l_(15415)
d3 = {'Red', 'Green'}
_l_(15416)
_c_(15421, _n_(15417, "print", lambda: print), _c_(15420, _n_(15418, "type", lambda: type), _n_(15419, "d3", lambda: d3)))
_l_(15422)
_c_(15427, _n_(15423, "print", lambda: print), _c_(15426, _n_(15424, "cast_list", lambda: cast_list), _n_(15425, "d3", lambda: d3)))
_l_(15428)
d4 = {1: 'Red', 2: 'Green', 3: 'Black'}
_l_(15429)
_c_(15434, _n_(15430, "print", lambda: print), _c_(15433, _n_(15431, "type", lambda: type), _n_(15432, "d4", lambda: d4)))
_l_(15435)
_c_(15440, _n_(15436, "print", lambda: print), _c_(15439, _n_(15437, "cast_list", lambda: cast_list), _n_(15438, "d4", lambda: d4)))
_l_(15441)