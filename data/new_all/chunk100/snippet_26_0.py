# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import copy
    _l_(21654)

except ImportError:
    pass
nums_x = {'a': 1, 'b': 2, 'cc': {'c': 3}}
_l_(21655)
_c_(21658, _n_(21656, "print", lambda: print), 'Original dictionary: ', _n_(21657, "nums_x", lambda: nums_x))
_l_(21659)
_c_(21661, _n_(21660, "print", lambda: print), '\nDeep copy of the said list:')
_l_(21662)
_c_(21665, _n_(21663, "print", lambda: print), _n_(21664, "nums_y", lambda: nums_y))
_l_(21666)
_c_(21668, _n_(21667, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(21669)
_n_(21670, "nums_x", lambda: nums_x)['cc']['c'] = 10
_l_(21671)
_c_(21674, _n_(21672, "print", lambda: print), _n_(21673, "nums_x", lambda: nums_x))
_l_(21675)
_c_(21677, _n_(21676, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(21678)
_c_(21681, _n_(21679, "print", lambda: print), _n_(21680, "nums_y", lambda: nums_y))
_l_(21682)
nums = {'x': 1, 'y': 2, 'zz': {'z': 3}}
_l_(21683)
nums_copy = _c_(21687, _a_(21685, _n_(21684, "copy", lambda: copy), "deepcopy"), _n_(21686, "nums", lambda: nums))
_l_(21688)
_c_(21690, _n_(21689, "print", lambda: print), '\nOriginal dictionary :')
_l_(21691)
_c_(21694, _n_(21692, "print", lambda: print), _n_(21693, "nums", lambda: nums))
_l_(21695)
_c_(21697, _n_(21696, "print", lambda: print), '\nDeep copy of the said list:')
_l_(21698)
_c_(21701, _n_(21699, "print", lambda: print), _n_(21700, "nums_copy", lambda: nums_copy))
_l_(21702)
_c_(21704, _n_(21703, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(21705)
_n_(21706, "nums", lambda: nums)['zz']['z'] = 10
_l_(21707)
_c_(21709, _n_(21708, "print", lambda: print), '\nFirst dictionary:')
_l_(21710)
_c_(21713, _n_(21711, "print", lambda: print), _n_(21712, "nums", lambda: nums))
_l_(21714)
_c_(21716, _n_(21715, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(21717)
_c_(21720, _n_(21718, "print", lambda: print), _n_(21719, "nums_copy", lambda: nums_copy))
_l_(21721)