# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cast_list(val):
    _l_(15454)

    aux = _c_(15444, _n_(15442, "list", lambda: list), _n_(15443, "val", lambda: val)) if _c_(15451, _n_(15445, "isinstance", lambda: isinstance), _n_(15446, "val", lambda: val), (_n_(15447, "tuple", lambda: tuple), _n_(15448, "list", lambda: list), _n_(15449, "set", lambda: set), _n_(15450, "dict", lambda: dict))) else [_n_(15452, "val", lambda: val)]
    _l_(15453)
    return aux
_c_(15459, _n_(15455, "print", lambda: print), _c_(15458, _n_(15456, "type", lambda: type), _n_(15457, "d1", lambda: d1)))
_l_(15460)
_c_(15465, _n_(15461, "print", lambda: print), _c_(15464, _n_(15462, "cast_list", lambda: cast_list), _n_(15463, "d1", lambda: d1)))
_l_(15466)
d2 = ('Red', 'Green')
_l_(15467)
_c_(15472, _n_(15468, "print", lambda: print), _c_(15471, _n_(15469, "type", lambda: type), _n_(15470, "d2", lambda: d2)))
_l_(15473)
_c_(15478, _n_(15474, "print", lambda: print), _c_(15477, _n_(15475, "cast_list", lambda: cast_list), _n_(15476, "d2", lambda: d2)))
_l_(15479)
d3 = {'Red', 'Green'}
_l_(15480)
_c_(15485, _n_(15481, "print", lambda: print), _c_(15484, _n_(15482, "type", lambda: type), _n_(15483, "d3", lambda: d3)))
_l_(15486)
_c_(15491, _n_(15487, "print", lambda: print), _c_(15490, _n_(15488, "cast_list", lambda: cast_list), _n_(15489, "d3", lambda: d3)))
_l_(15492)
d4 = {1: 'Red', 2: 'Green', 3: 'Black'}
_l_(15493)
_c_(15498, _n_(15494, "print", lambda: print), _c_(15497, _n_(15495, "type", lambda: type), _n_(15496, "d4", lambda: d4)))
_l_(15499)
_c_(15504, _n_(15500, "print", lambda: print), _c_(15503, _n_(15501, "cast_list", lambda: cast_list), _n_(15502, "d4", lambda: d4)))
_l_(15505)