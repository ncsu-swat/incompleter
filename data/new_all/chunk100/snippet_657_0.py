# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
_l_(67552)
_c_(67554, _n_(67553, "print", lambda: print), 'Original arrays:')
_l_(67555)
_c_(67558, _n_(67556, "print", lambda: print), _n_(67557, "array_nums", lambda: array_nums))
_l_(67559)
odd_ctr = _c_(67567, _n_(67560, "len", lambda: len), _c_(67566, _n_(67561, "list", lambda: list), _c_(67565, _n_(67562, "filter", lambda: filter), lambda x: _n_(67563, "x", lambda: x) % 2 != 0, _n_(67564, "array_nums", lambda: array_nums))))
_l_(67568)
_c_(67571, _n_(67569, "print", lambda: print), '\nNumber of even numbers in the above array: ', _n_(67570, "even_ctr", lambda: even_ctr))
_l_(67572)
_c_(67575, _n_(67573, "print", lambda: print), '\nNumber of odd numbers in the above array: ', _n_(67574, "odd_ctr", lambda: odd_ctr))
_l_(67576)