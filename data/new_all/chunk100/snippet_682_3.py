# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums_tuple = (0, 1, 2, 3)
_l_(70755)
_c_(70757, _n_(70756, "print", lambda: print), 'Original list and tuple:')
_l_(70758)
_c_(70761, _n_(70759, "print", lambda: print), _n_(70760, "nums_list", lambda: nums_list))
_l_(70762)
_c_(70765, _n_(70763, "print", lambda: print), _n_(70764, "nums_tuple", lambda: nums_tuple))
_l_(70766)
result_list = _c_(70772, _n_(70767, "list", lambda: list), _c_(70771, _n_(70768, "map", lambda: map), _n_(70769, "str", lambda: str), _n_(70770, "nums_list", lambda: nums_list)))
_l_(70773)
result_tuple = _c_(70779, _n_(70774, "tuple", lambda: tuple), _c_(70778, _n_(70775, "map", lambda: map), _n_(70776, "str", lambda: str), _n_(70777, "nums_tuple", lambda: nums_tuple)))
_l_(70780)
_c_(70782, _n_(70781, "print", lambda: print), '\nList of strings:')
_l_(70783)
_c_(70786, _n_(70784, "print", lambda: print), _n_(70785, "result_list", lambda: result_list))
_l_(70787)
_c_(70789, _n_(70788, "print", lambda: print), '\nTuple of strings:')
_l_(70790)
_c_(70793, _n_(70791, "print", lambda: print), _n_(70792, "result_tuple", lambda: result_tuple))
_l_(70794)