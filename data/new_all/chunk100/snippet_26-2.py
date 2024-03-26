# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import copy
    _l_(107393)

except ImportError:
    pass
_c_(107396, _n_(107394, "print", lambda: print), 'Original dictionary: ', _n_(107395, "nums_x", lambda: nums_x))
_l_(107397)
nums_y = _c_(107401, _a_(107399, _n_(107398, "copy", lambda: copy), "deepcopy"), _n_(107400, "nums_x", lambda: nums_x))
_l_(107402)
_c_(107404, _n_(107403, "print", lambda: print), '\nDeep copy of the said list:')
_l_(107405)
_c_(107408, _n_(107406, "print", lambda: print), _n_(107407, "nums_y", lambda: nums_y))
_l_(107409)
_c_(107411, _n_(107410, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(107412)
_n_(107413, "nums_x", lambda: nums_x)['cc']['c'] = 10
_l_(107414)
_c_(107417, _n_(107415, "print", lambda: print), _n_(107416, "nums_x", lambda: nums_x))
_l_(107418)
_c_(107420, _n_(107419, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(107421)
_c_(107424, _n_(107422, "print", lambda: print), _n_(107423, "nums_y", lambda: nums_y))
_l_(107425)
nums = {'x': 1, 'y': 2, 'zz': {'z': 3}}
_l_(107426)
nums_copy = _c_(107430, _a_(107428, _n_(107427, "copy", lambda: copy), "deepcopy"), _n_(107429, "nums", lambda: nums))
_l_(107431)
_c_(107433, _n_(107432, "print", lambda: print), '\nOriginal dictionary :')
_l_(107434)
_c_(107437, _n_(107435, "print", lambda: print), _n_(107436, "nums", lambda: nums))
_l_(107438)
_c_(107440, _n_(107439, "print", lambda: print), '\nDeep copy of the said list:')
_l_(107441)
_c_(107444, _n_(107442, "print", lambda: print), _n_(107443, "nums_copy", lambda: nums_copy))
_l_(107445)
_c_(107447, _n_(107446, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(107448)
_n_(107449, "nums", lambda: nums)['zz']['z'] = 10
_l_(107450)
_c_(107452, _n_(107451, "print", lambda: print), '\nFirst dictionary:')
_l_(107453)
_c_(107456, _n_(107454, "print", lambda: print), _n_(107455, "nums", lambda: nums))
_l_(107457)
_c_(107459, _n_(107458, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(107460)
_c_(107463, _n_(107461, "print", lambda: print), _n_(107462, "nums_copy", lambda: nums_copy))
_l_(107464)