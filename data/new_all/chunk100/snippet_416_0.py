# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(40752)

except ImportError:
    pass

def combination(str1):
    _l_(40771)

    result = _c_(40765, _n_(40753, "map", lambda: map), _a_(40754, '', "join"), _c_(40764, _a_(40756, _n_(40755, "itertools", lambda: itertools), "product"), *((_c_(40759, _a_(40758, _n_(40757, "c", lambda: c), "lower")), _c_(40762, _a_(40761, _n_(40760, "c", lambda: c), "upper"))) for c in _n_(40763, "str1", lambda: str1))))
    _l_(40766)
    aux = _c_(40769, _n_(40767, "list", lambda: list), _n_(40768, "result", lambda: result))
    _l_(40770)
    return aux
_c_(40773, _n_(40772, "print", lambda: print), 'Original string:')
_l_(40774)
_c_(40777, _n_(40775, "print", lambda: print), _n_(40776, "st", lambda: st))
_l_(40778)
_c_(40780, _n_(40779, "print", lambda: print), 'All lower and upper mixed case combinations of the said string:')
_l_(40781)
_c_(40786, _n_(40782, "print", lambda: print), _c_(40785, _n_(40783, "combination", lambda: combination), _n_(40784, "st", lambda: st)))
_l_(40787)
st = 'w3r'
_l_(40788)
_c_(40790, _n_(40789, "print", lambda: print), '\nOriginal string:')
_l_(40791)
_c_(40794, _n_(40792, "print", lambda: print), _n_(40793, "st", lambda: st))
_l_(40795)
_c_(40797, _n_(40796, "print", lambda: print), 'All lower and upper mixed case combinations of the said string:')
_l_(40798)
_c_(40803, _n_(40799, "print", lambda: print), _c_(40802, _n_(40800, "combination", lambda: combination), _n_(40801, "st", lambda: st)))
_l_(40804)
st = 'Python'
_l_(40805)
_c_(40807, _n_(40806, "print", lambda: print), '\nOriginal string:')
_l_(40808)
_c_(40811, _n_(40809, "print", lambda: print), _n_(40810, "st", lambda: st))
_l_(40812)
_c_(40814, _n_(40813, "print", lambda: print), 'All lower and upper mixed case combinations of the said string:')
_l_(40815)
_c_(40820, _n_(40816, "print", lambda: print), _c_(40819, _n_(40817, "combination", lambda: combination), _n_(40818, "st", lambda: st)))
_l_(40821)