# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def condition_match(x):
    _l_(10486)

    aux = _n_(10484, "x", lambda: x) % 2 == 0
    _l_(10485)
    return aux

def remove_items_con(data, N):
    _l_(10506)

    ctr = 1
    _l_(10487)
    result = []
    _l_(10488)
    for x in _n_(10489, "data", lambda: data):
        _l_(10503)

        if _n_(10490, "ctr", lambda: ctr) > _n_(10491, "N", lambda: N) or not _c_(10494, _n_(10492, "condition_match", lambda: condition_match), _n_(10493, "x", lambda: x)):
            _l_(10502)

            _c_(10498, _a_(10496, _n_(10495, "result", lambda: result), "append"), _n_(10497, "x", lambda: x))
            _l_(10499)
        else:
            ctr = _n_(10500, "ctr", lambda: ctr) + 1
            _l_(10501)
    aux = _n_(10504, "result", lambda: result)
    _l_(10505)
    return aux
nums = [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
_l_(10507)
_c_(10509, _n_(10508, "print", lambda: print), 'Original list:')
_l_(10510)
_c_(10513, _n_(10511, "print", lambda: print), _n_(10512, "nums", lambda: nums))
_l_(10514)
_c_(10516, _n_(10515, "print", lambda: print), '\nRemove first 4 even numbers from the said list:')
_l_(10517)
_c_(10523, _n_(10518, "print", lambda: print), _c_(10522, _n_(10519, "remove_items_con", lambda: remove_items_con), _n_(10520, "nums", lambda: nums), _n_(10521, "N", lambda: N)))
_l_(10524)