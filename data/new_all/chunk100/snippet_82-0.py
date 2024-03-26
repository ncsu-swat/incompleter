# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(120742)

except ImportError:
    pass
_c_(120744, _n_(120743, "print", lambda: print), 'Original list:')
_l_(120745)
_c_(120748, _n_(120746, "print", lambda: print), _n_(120747, "uno_list", lambda: uno_list))
_l_(120749)
_c_(120752, _a_(120751, _n_(120750, "uno_list", lambda: uno_list), "sort"))
_l_(120753)
_c_(120756, _n_(120754, "print", lambda: print), _n_(120755, "uno_list", lambda: uno_list))
_l_(120757)
_c_(120759, _n_(120758, "print", lambda: print), '\nSort the said unordered list:')
_l_(120760)
_c_(120763, _n_(120761, "print", lambda: print), _n_(120762, "uno_list", lambda: uno_list))
_l_(120764)
_c_(120766, _n_(120765, "print", lambda: print), '\nFrequency of the elements of the said unordered list:')
_l_(120767)
result = [_c_(120772, _n_(120768, "len", lambda: len), _c_(120771, _n_(120769, "list", lambda: list), _n_(120770, "group", lambda: group))) for key, group in _c_(120775, _n_(120773, "groupby", lambda: groupby), _n_(120774, "uno_list", lambda: uno_list))]
_l_(120776)
_c_(120779, _n_(120777, "print", lambda: print), _n_(120778, "result", lambda: result))
_l_(120780)