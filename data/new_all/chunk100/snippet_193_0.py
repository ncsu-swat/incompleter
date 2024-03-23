# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cast_list(val):
    _l_(15326)

    aux = _c_(15316, _n_(15314, "list", lambda: list), _n_(15315, "val", lambda: val)) if _c_(15323, _n_(15317, "isinstance", lambda: isinstance), _n_(15318, "val", lambda: val), (_n_(15319, "tuple", lambda: tuple), _n_(15320, "list", lambda: list), _n_(15321, "set", lambda: set), _n_(15322, "dict", lambda: dict))) else [_n_(15324, "val", lambda: val)]
    _l_(15325)
    return aux
d1 = [1]
_l_(15327)
_c_(15332, _n_(15328, "print", lambda: print), _c_(15331, _n_(15329, "type", lambda: type), _n_(15330, "d1", lambda: d1)))
_l_(15333)
_c_(15338, _n_(15334, "print", lambda: print), _c_(15337, _n_(15335, "cast_list", lambda: cast_list), _n_(15336, "d1", lambda: d1)))
_l_(15339)
d2 = ('Red', 'Green')
_l_(15340)
_c_(15345, _n_(15341, "print", lambda: print), _c_(15344, _n_(15342, "type", lambda: type), _n_(15343, "d2", lambda: d2)))
_l_(15346)
_c_(15351, _n_(15347, "print", lambda: print), _c_(15350, _n_(15348, "cast_list", lambda: cast_list), _n_(15349, "d2", lambda: d2)))
_l_(15352)
d3 = {'Red', 'Green'}
_l_(15353)
_c_(15358, _n_(15354, "print", lambda: print), _c_(15357, _n_(15355, "type", lambda: type), _n_(15356, "d3", lambda: d3)))
_l_(15359)
_c_(15364, _n_(15360, "print", lambda: print), _c_(15363, _n_(15361, "cast_list", lambda: cast_list), _n_(15362, "d3", lambda: d3)))
_l_(15365)
_c_(15370, _n_(15366, "print", lambda: print), _c_(15369, _n_(15367, "type", lambda: type), _n_(15368, "d4", lambda: d4)))
_l_(15371)
_c_(15376, _n_(15372, "print", lambda: print), _c_(15375, _n_(15373, "cast_list", lambda: cast_list), _n_(15374, "d4", lambda: d4)))
_l_(15377)