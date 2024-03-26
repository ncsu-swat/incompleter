# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def condition_match(x):
    _l_(102657)

    aux = _n_(102655, "x", lambda: x) % 2 == 0
    _l_(102656)
    return aux

def remove_items_con(data, N):
    _l_(102677)

    ctr = 1
    _l_(102658)
    result = []
    _l_(102659)
    for x in _n_(102660, "data", lambda: data):
        _l_(102674)

        if _n_(102661, "ctr", lambda: ctr) > _n_(102662, "N", lambda: N) or not _c_(102665, _n_(102663, "condition_match", lambda: condition_match), _n_(102664, "x", lambda: x)):
            _l_(102673)

            _c_(102669, _a_(102667, _n_(102666, "result", lambda: result), "append"), _n_(102668, "x", lambda: x))
            _l_(102670)
        else:
            ctr = _n_(102671, "ctr", lambda: ctr) + 1
            _l_(102672)
    aux = _n_(102675, "result", lambda: result)
    _l_(102676)
    return aux
nums = [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
_l_(102678)
_c_(102680, _n_(102679, "print", lambda: print), 'Original list:')
_l_(102681)
_c_(102684, _n_(102682, "print", lambda: print), _n_(102683, "nums", lambda: nums))
_l_(102685)
_c_(102687, _n_(102686, "print", lambda: print), '\nRemove first 4 even numbers from the said list:')
_l_(102688)
_c_(102694, _n_(102689, "print", lambda: print), _c_(102693, _n_(102690, "remove_items_con", lambda: remove_items_con), _n_(102691, "nums", lambda: nums), _n_(102692, "N", lambda: N)))
_l_(102695)