# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def merge_some_chars(lst, merge_from, merge_to):
    _l_(11093)

    result = _n_(11080, "lst", lambda: lst)
    _l_(11081)
    _n_(11082, "result", lambda: result)[_n_(11083, "merge_from", lambda: merge_from):_n_(11084, "merge_to", lambda: merge_to)] = [_c_(11089, _a_(11085, '', "join"), _n_(11086, "result", lambda: result)[_n_(11087, "merge_from", lambda: merge_from):_n_(11088, "merge_to", lambda: merge_to)])]
    _l_(11090)
    aux = _n_(11091, "result", lambda: result)
    _l_(11092)
    return aux
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
_l_(11094)
_c_(11096, _n_(11095, "print", lambda: print), 'Original lists:')
_l_(11097)
_c_(11100, _n_(11098, "print", lambda: print), _n_(11099, "chars", lambda: chars))
_l_(11101)
merge_from = 2
_l_(11102)
merge_to = 4
_l_(11103)
_c_(11107, _n_(11104, "print", lambda: print), '\nMerge items from', _n_(11105, "merge_from", lambda: merge_from), 'to', _n_(11106, "merge_to", lambda: merge_to), 'in the said List:')
_l_(11108)
_c_(11115, _n_(11109, "print", lambda: print), _c_(11114, _n_(11110, "merge_some_chars", lambda: merge_some_chars), _n_(11111, "chars", lambda: chars), _n_(11112, "merge_from", lambda: merge_from), _n_(11113, "merge_to", lambda: merge_to)))
_l_(11116)
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
_l_(11117)
merge_to = 7
_l_(11118)
_c_(11122, _n_(11119, "print", lambda: print), '\nMerge items from', _n_(11120, "merge_from", lambda: merge_from), 'to', _n_(11121, "merge_to", lambda: merge_to), 'in the said List:')
_l_(11123)
_c_(11130, _n_(11124, "print", lambda: print), _c_(11129, _n_(11125, "merge_some_chars", lambda: merge_some_chars), _n_(11126, "chars", lambda: chars), _n_(11127, "merge_from", lambda: merge_from), _n_(11128, "merge_to", lambda: merge_to)))
_l_(11131)