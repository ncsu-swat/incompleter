# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums_list = [1, 2, 3, 4]
_l_(70681)
nums_tuple = (0, 1, 2, 3)
_l_(70682)
_c_(70684, _n_(70683, "print", lambda: print), 'Original list and tuple:')
_l_(70685)
_c_(70688, _n_(70686, "print", lambda: print), _n_(70687, "nums_list", lambda: nums_list))
_l_(70689)
_c_(70692, _n_(70690, "print", lambda: print), _n_(70691, "nums_tuple", lambda: nums_tuple))
_l_(70693)
result_tuple = _c_(70699, _n_(70694, "tuple", lambda: tuple), _c_(70698, _n_(70695, "map", lambda: map), _n_(70696, "str", lambda: str), _n_(70697, "nums_tuple", lambda: nums_tuple)))
_l_(70700)
_c_(70702, _n_(70701, "print", lambda: print), '\nList of strings:')
_l_(70703)
_c_(70706, _n_(70704, "print", lambda: print), _n_(70705, "result_list", lambda: result_list))
_l_(70707)
_c_(70709, _n_(70708, "print", lambda: print), '\nTuple of strings:')
_l_(70710)
_c_(70713, _n_(70711, "print", lambda: print), _n_(70712, "result_tuple", lambda: result_tuple))
_l_(70714)