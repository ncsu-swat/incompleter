# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cast_list(val):
    _l_(104447)

    aux = _c_(104437, _n_(104435, "list", lambda: list), _n_(104436, "val", lambda: val)) if _c_(104444, _n_(104438, "isinstance", lambda: isinstance), _n_(104439, "val", lambda: val), (_n_(104440, "tuple", lambda: tuple), _n_(104441, "list", lambda: list), _n_(104442, "set", lambda: set), _n_(104443, "dict", lambda: dict))) else [_n_(104445, "val", lambda: val)]
    _l_(104446)
    return aux
d1 = [1]
_l_(104448)
_c_(104453, _n_(104449, "print", lambda: print), _c_(104452, _n_(104450, "type", lambda: type), _n_(104451, "d1", lambda: d1)))
_l_(104454)
_c_(104459, _n_(104455, "print", lambda: print), _c_(104458, _n_(104456, "cast_list", lambda: cast_list), _n_(104457, "d1", lambda: d1)))
_l_(104460)
_c_(104465, _n_(104461, "print", lambda: print), _c_(104464, _n_(104462, "type", lambda: type), _n_(104463, "d2", lambda: d2)))
_l_(104466)
_c_(104471, _n_(104467, "print", lambda: print), _c_(104470, _n_(104468, "cast_list", lambda: cast_list), _n_(104469, "d2", lambda: d2)))
_l_(104472)
d3 = {'Red', 'Green'}
_l_(104473)
_c_(104478, _n_(104474, "print", lambda: print), _c_(104477, _n_(104475, "type", lambda: type), _n_(104476, "d3", lambda: d3)))
_l_(104479)
_c_(104484, _n_(104480, "print", lambda: print), _c_(104483, _n_(104481, "cast_list", lambda: cast_list), _n_(104482, "d3", lambda: d3)))
_l_(104485)
d4 = {1: 'Red', 2: 'Green', 3: 'Black'}
_l_(104486)
_c_(104491, _n_(104487, "print", lambda: print), _c_(104490, _n_(104488, "type", lambda: type), _n_(104489, "d4", lambda: d4)))
_l_(104492)
_c_(104497, _n_(104493, "print", lambda: print), _c_(104496, _n_(104494, "cast_list", lambda: cast_list), _n_(104495, "d4", lambda: d4)))
_l_(104498)