# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cast_list(val):
    _l_(15518)

    aux = _c_(15508, _n_(15506, "list", lambda: list), _n_(15507, "val", lambda: val)) if _c_(15515, _n_(15509, "isinstance", lambda: isinstance), _n_(15510, "val", lambda: val), (_n_(15511, "tuple", lambda: tuple), _n_(15512, "list", lambda: list), _n_(15513, "set", lambda: set), _n_(15514, "dict", lambda: dict))) else [_n_(15516, "val", lambda: val)]
    _l_(15517)
    return aux
d1 = [1]
_l_(15519)
_c_(15524, _n_(15520, "print", lambda: print), _c_(15523, _n_(15521, "type", lambda: type), _n_(15522, "d1", lambda: d1)))
_l_(15525)
_c_(15530, _n_(15526, "print", lambda: print), _c_(15529, _n_(15527, "cast_list", lambda: cast_list), _n_(15528, "d1", lambda: d1)))
_l_(15531)
d2 = ('Red', 'Green')
_l_(15532)
_c_(15537, _n_(15533, "print", lambda: print), _c_(15536, _n_(15534, "type", lambda: type), _n_(15535, "d2", lambda: d2)))
_l_(15538)
_c_(15543, _n_(15539, "print", lambda: print), _c_(15542, _n_(15540, "cast_list", lambda: cast_list), _n_(15541, "d2", lambda: d2)))
_l_(15544)
_c_(15549, _n_(15545, "print", lambda: print), _c_(15548, _n_(15546, "type", lambda: type), _n_(15547, "d3", lambda: d3)))
_l_(15550)
_c_(15555, _n_(15551, "print", lambda: print), _c_(15554, _n_(15552, "cast_list", lambda: cast_list), _n_(15553, "d3", lambda: d3)))
_l_(15556)
d4 = {1: 'Red', 2: 'Green', 3: 'Black'}
_l_(15557)
_c_(15562, _n_(15558, "print", lambda: print), _c_(15561, _n_(15559, "type", lambda: type), _n_(15560, "d4", lambda: d4)))
_l_(15563)
_c_(15568, _n_(15564, "print", lambda: print), _c_(15567, _n_(15565, "cast_list", lambda: cast_list), _n_(15566, "d4", lambda: d4)))
_l_(15569)