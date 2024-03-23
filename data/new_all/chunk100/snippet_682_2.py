# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums_list = [1, 2, 3, 4]
_l_(70715)
_c_(70717, _n_(70716, "print", lambda: print), 'Original list and tuple:')
_l_(70718)
_c_(70721, _n_(70719, "print", lambda: print), _n_(70720, "nums_list", lambda: nums_list))
_l_(70722)
_c_(70725, _n_(70723, "print", lambda: print), _n_(70724, "nums_tuple", lambda: nums_tuple))
_l_(70726)
result_list = _c_(70732, _n_(70727, "list", lambda: list), _c_(70731, _n_(70728, "map", lambda: map), _n_(70729, "str", lambda: str), _n_(70730, "nums_list", lambda: nums_list)))
_l_(70733)
result_tuple = _c_(70739, _n_(70734, "tuple", lambda: tuple), _c_(70738, _n_(70735, "map", lambda: map), _n_(70736, "str", lambda: str), _n_(70737, "nums_tuple", lambda: nums_tuple)))
_l_(70740)
_c_(70742, _n_(70741, "print", lambda: print), '\nList of strings:')
_l_(70743)
_c_(70746, _n_(70744, "print", lambda: print), _n_(70745, "result_list", lambda: result_list))
_l_(70747)
_c_(70749, _n_(70748, "print", lambda: print), '\nTuple of strings:')
_l_(70750)
_c_(70753, _n_(70751, "print", lambda: print), _n_(70752, "result_tuple", lambda: result_tuple))
_l_(70754)