# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def condition_match(x):
    _l_(102616)

    aux = _n_(102614, "x", lambda: x) % 2 == 0
    _l_(102615)
    return aux

def remove_items_con(data, N):
    _l_(102636)

    ctr = 1
    _l_(102617)
    result = []
    _l_(102618)
    for x in _n_(102619, "data", lambda: data):
        _l_(102633)

        if _n_(102620, "ctr", lambda: ctr) > _n_(102621, "N", lambda: N) or not _c_(102624, _n_(102622, "condition_match", lambda: condition_match), _n_(102623, "x", lambda: x)):
            _l_(102632)

            _c_(102628, _a_(102626, _n_(102625, "result", lambda: result), "append"), _n_(102627, "x", lambda: x))
            _l_(102629)
        else:
            ctr = _n_(102630, "ctr", lambda: ctr) + 1
            _l_(102631)
    aux = _n_(102634, "result", lambda: result)
    _l_(102635)
    return aux
N = 4
_l_(102637)
_c_(102639, _n_(102638, "print", lambda: print), 'Original list:')
_l_(102640)
_c_(102643, _n_(102641, "print", lambda: print), _n_(102642, "nums", lambda: nums))
_l_(102644)
_c_(102646, _n_(102645, "print", lambda: print), '\nRemove first 4 even numbers from the said list:')
_l_(102647)
_c_(102653, _n_(102648, "print", lambda: print), _c_(102652, _n_(102649, "remove_items_con", lambda: remove_items_con), _n_(102650, "nums", lambda: nums), _n_(102651, "N", lambda: N)))
_l_(102654)