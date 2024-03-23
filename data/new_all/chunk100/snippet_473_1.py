# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(49650)
_c_(49652, _n_(49651, "print", lambda: print), 'Original list of integers:')
_l_(49653)
_c_(49656, _n_(49654, "print", lambda: print), _n_(49655, "nums", lambda: nums))
_l_(49657)
_c_(49659, _n_(49658, "print", lambda: print), '\nEven numbers from the said list:')
_l_(49660)
even_nums = _c_(49666, _n_(49661, "list", lambda: list), _c_(49665, _n_(49662, "filter", lambda: filter), lambda x: _n_(49663, "x", lambda: x) % 2 == 0, _n_(49664, "nums", lambda: nums)))
_l_(49667)
_c_(49670, _n_(49668, "print", lambda: print), _n_(49669, "even_nums", lambda: even_nums))
_l_(49671)
_c_(49673, _n_(49672, "print", lambda: print), '\nOdd numbers from the said list:')
_l_(49674)
_c_(49677, _n_(49675, "print", lambda: print), _n_(49676, "odd_nums", lambda: odd_nums))
_l_(49678)