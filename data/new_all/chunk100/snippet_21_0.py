# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(17258, _n_(17257, "print", lambda: print), 'Orginal list:')
_l_(17259)
_c_(17262, _n_(17260, "print", lambda: print), _n_(17261, "nums", lambda: nums))
_l_(17263)
result = _c_(17270, _n_(17264, "list", lambda: list), _c_(17269, _n_(17265, "filter", lambda: filter), lambda x: _n_(17266, "x", lambda: x) % 19 == 0 or _n_(17267, "x", lambda: x) % 13 == 0, _n_(17268, "nums", lambda: nums)))
_l_(17271)
_c_(17273, _n_(17272, "print", lambda: print), '\nNumbers of the above list divisible by nineteen or thirteen:')
_l_(17274)
_c_(17277, _n_(17275, "print", lambda: print), _n_(17276, "result", lambda: result))
_l_(17278)