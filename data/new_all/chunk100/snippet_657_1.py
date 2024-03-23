# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
_l_(67577)
_c_(67579, _n_(67578, "print", lambda: print), 'Original arrays:')
_l_(67580)
_c_(67583, _n_(67581, "print", lambda: print), _n_(67582, "array_nums", lambda: array_nums))
_l_(67584)
even_ctr = _c_(67592, _n_(67585, "len", lambda: len), _c_(67591, _n_(67586, "list", lambda: list), _c_(67590, _n_(67587, "filter", lambda: filter), lambda x: _n_(67588, "x", lambda: x) % 2 == 0, _n_(67589, "array_nums", lambda: array_nums))))
_l_(67593)
_c_(67596, _n_(67594, "print", lambda: print), '\nNumber of even numbers in the above array: ', _n_(67595, "even_ctr", lambda: even_ctr))
_l_(67597)
_c_(67600, _n_(67598, "print", lambda: print), '\nNumber of odd numbers in the above array: ', _n_(67599, "odd_ctr", lambda: odd_ctr))
_l_(67601)