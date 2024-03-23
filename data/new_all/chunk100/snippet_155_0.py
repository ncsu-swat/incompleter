# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def condition_match(x):
    _l_(10404)

    aux = _n_(10402, "x", lambda: x) % 2 == 0
    _l_(10403)
    return aux

def remove_items_con(data, N):
    _l_(10423)

    ctr = 1
    _l_(10405)
    for x in _n_(10406, "data", lambda: data):
        _l_(10420)

        if _n_(10407, "ctr", lambda: ctr) > _n_(10408, "N", lambda: N) or not _c_(10411, _n_(10409, "condition_match", lambda: condition_match), _n_(10410, "x", lambda: x)):
            _l_(10419)

            _c_(10415, _a_(10413, _n_(10412, "result", lambda: result), "append"), _n_(10414, "x", lambda: x))
            _l_(10416)
        else:
            ctr = _n_(10417, "ctr", lambda: ctr) + 1
            _l_(10418)
    aux = _n_(10421, "result", lambda: result)
    _l_(10422)
    return aux
nums = [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
_l_(10424)
N = 4
_l_(10425)
_c_(10427, _n_(10426, "print", lambda: print), 'Original list:')
_l_(10428)
_c_(10431, _n_(10429, "print", lambda: print), _n_(10430, "nums", lambda: nums))
_l_(10432)
_c_(10434, _n_(10433, "print", lambda: print), '\nRemove first 4 even numbers from the said list:')
_l_(10435)
_c_(10441, _n_(10436, "print", lambda: print), _c_(10440, _n_(10437, "remove_items_con", lambda: remove_items_con), _n_(10438, "nums", lambda: nums), _n_(10439, "N", lambda: N)))
_l_(10442)