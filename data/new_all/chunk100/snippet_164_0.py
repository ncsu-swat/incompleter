# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def merge_some_chars(lst, merge_from, merge_to):
    _l_(11041)

    result = _n_(11028, "lst", lambda: lst)
    _l_(11029)
    _n_(11030, "result", lambda: result)[_n_(11031, "merge_from", lambda: merge_from):_n_(11032, "merge_to", lambda: merge_to)] = [_c_(11037, _a_(11033, '', "join"), _n_(11034, "result", lambda: result)[_n_(11035, "merge_from", lambda: merge_from):_n_(11036, "merge_to", lambda: merge_to)])]
    _l_(11038)
    aux = _n_(11039, "result", lambda: result)
    _l_(11040)
    return aux
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
_l_(11042)
_c_(11044, _n_(11043, "print", lambda: print), 'Original lists:')
_l_(11045)
_c_(11048, _n_(11046, "print", lambda: print), _n_(11047, "chars", lambda: chars))
_l_(11049)
merge_from = 2
_l_(11050)
merge_to = 4
_l_(11051)
_c_(11055, _n_(11052, "print", lambda: print), '\nMerge items from', _n_(11053, "merge_from", lambda: merge_from), 'to', _n_(11054, "merge_to", lambda: merge_to), 'in the said List:')
_l_(11056)
_c_(11063, _n_(11057, "print", lambda: print), _c_(11062, _n_(11058, "merge_some_chars", lambda: merge_some_chars), _n_(11059, "chars", lambda: chars), _n_(11060, "merge_from", lambda: merge_from), _n_(11061, "merge_to", lambda: merge_to)))
_l_(11064)
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
_l_(11065)
merge_from = 3
_l_(11066)
_c_(11070, _n_(11067, "print", lambda: print), '\nMerge items from', _n_(11068, "merge_from", lambda: merge_from), 'to', _n_(11069, "merge_to", lambda: merge_to), 'in the said List:')
_l_(11071)
_c_(11078, _n_(11072, "print", lambda: print), _c_(11077, _n_(11073, "merge_some_chars", lambda: merge_some_chars), _n_(11074, "chars", lambda: chars), _n_(11075, "merge_from", lambda: merge_from), _n_(11076, "merge_to", lambda: merge_to)))
_l_(11079)