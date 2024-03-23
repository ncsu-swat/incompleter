# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
my_list = ['p', 'q']
_l_(48795)
new_list = [_c_(48799, _a_(48796, '{}{}', "format"), _n_(48797, "x", lambda: x), _n_(48798, "y", lambda: y)) for y in _c_(48802, _n_(48800, "range", lambda: range), 1, _n_(48801, "n", lambda: n) + 1) for x in _n_(48803, "my_list", lambda: my_list)]
_l_(48804)
_c_(48807, _n_(48805, "print", lambda: print), _n_(48806, "new_list", lambda: new_list))
_l_(48808)