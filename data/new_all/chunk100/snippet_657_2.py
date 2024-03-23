# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(67603, _n_(67602, "print", lambda: print), 'Original arrays:')
_l_(67604)
_c_(67607, _n_(67605, "print", lambda: print), _n_(67606, "array_nums", lambda: array_nums))
_l_(67608)
odd_ctr = _c_(67616, _n_(67609, "len", lambda: len), _c_(67615, _n_(67610, "list", lambda: list), _c_(67614, _n_(67611, "filter", lambda: filter), lambda x: _n_(67612, "x", lambda: x) % 2 != 0, _n_(67613, "array_nums", lambda: array_nums))))
_l_(67617)
even_ctr = _c_(67625, _n_(67618, "len", lambda: len), _c_(67624, _n_(67619, "list", lambda: list), _c_(67623, _n_(67620, "filter", lambda: filter), lambda x: _n_(67621, "x", lambda: x) % 2 == 0, _n_(67622, "array_nums", lambda: array_nums))))
_l_(67626)
_c_(67629, _n_(67627, "print", lambda: print), '\nNumber of even numbers in the above array: ', _n_(67628, "even_ctr", lambda: even_ctr))
_l_(67630)
_c_(67633, _n_(67631, "print", lambda: print), '\nNumber of odd numbers in the above array: ', _n_(67632, "odd_ctr", lambda: odd_ctr))
_l_(67634)