# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def merge_some_chars(lst, merge_from, merge_to):
    _l_(11300)

    result = _n_(11287, "lst", lambda: lst)
    _l_(11288)
    _n_(11289, "result", lambda: result)[_n_(11290, "merge_from", lambda: merge_from):_n_(11291, "merge_to", lambda: merge_to)] = [_c_(11296, _a_(11292, '', "join"), _n_(11293, "result", lambda: result)[_n_(11294, "merge_from", lambda: merge_from):_n_(11295, "merge_to", lambda: merge_to)])]
    _l_(11297)
    aux = _n_(11298, "result", lambda: result)
    _l_(11299)
    return aux
_c_(11302, _n_(11301, "print", lambda: print), 'Original lists:')
_l_(11303)
_c_(11306, _n_(11304, "print", lambda: print), _n_(11305, "chars", lambda: chars))
_l_(11307)
merge_from = 2
_l_(11308)
merge_to = 4
_l_(11309)
_c_(11313, _n_(11310, "print", lambda: print), '\nMerge items from', _n_(11311, "merge_from", lambda: merge_from), 'to', _n_(11312, "merge_to", lambda: merge_to), 'in the said List:')
_l_(11314)
_c_(11321, _n_(11315, "print", lambda: print), _c_(11320, _n_(11316, "merge_some_chars", lambda: merge_some_chars), _n_(11317, "chars", lambda: chars), _n_(11318, "merge_from", lambda: merge_from), _n_(11319, "merge_to", lambda: merge_to)))
_l_(11322)
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
_l_(11323)
merge_from = 3
_l_(11324)
merge_to = 7
_l_(11325)
_c_(11329, _n_(11326, "print", lambda: print), '\nMerge items from', _n_(11327, "merge_from", lambda: merge_from), 'to', _n_(11328, "merge_to", lambda: merge_to), 'in the said List:')
_l_(11330)
_c_(11337, _n_(11331, "print", lambda: print), _c_(11336, _n_(11332, "merge_some_chars", lambda: merge_some_chars), _n_(11333, "chars", lambda: chars), _n_(11334, "merge_from", lambda: merge_from), _n_(11335, "merge_to", lambda: merge_to)))
_l_(11338)