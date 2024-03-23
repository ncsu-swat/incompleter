# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums_list = [1, 2, 3, 4]
_l_(70647)
nums_tuple = (0, 1, 2, 3)
_l_(70648)
_c_(70650, _n_(70649, "print", lambda: print), 'Original list and tuple:')
_l_(70651)
_c_(70654, _n_(70652, "print", lambda: print), _n_(70653, "nums_list", lambda: nums_list))
_l_(70655)
_c_(70658, _n_(70656, "print", lambda: print), _n_(70657, "nums_tuple", lambda: nums_tuple))
_l_(70659)
result_list = _c_(70665, _n_(70660, "list", lambda: list), _c_(70664, _n_(70661, "map", lambda: map), _n_(70662, "str", lambda: str), _n_(70663, "nums_list", lambda: nums_list)))
_l_(70666)
_c_(70668, _n_(70667, "print", lambda: print), '\nList of strings:')
_l_(70669)
_c_(70672, _n_(70670, "print", lambda: print), _n_(70671, "result_list", lambda: result_list))
_l_(70673)
_c_(70675, _n_(70674, "print", lambda: print), '\nTuple of strings:')
_l_(70676)
_c_(70679, _n_(70677, "print", lambda: print), _n_(70678, "result_tuple", lambda: result_tuple))
_l_(70680)