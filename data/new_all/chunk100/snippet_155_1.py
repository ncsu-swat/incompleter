# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def condition_match(x):
    _l_(10445)

    aux = _n_(10443, "x", lambda: x) % 2 == 0
    _l_(10444)
    return aux

def remove_items_con(data, N):
    _l_(10465)

    ctr = 1
    _l_(10446)
    result = []
    _l_(10447)
    for x in _n_(10448, "data", lambda: data):
        _l_(10462)

        if _n_(10449, "ctr", lambda: ctr) > _n_(10450, "N", lambda: N) or not _c_(10453, _n_(10451, "condition_match", lambda: condition_match), _n_(10452, "x", lambda: x)):
            _l_(10461)

            _c_(10457, _a_(10455, _n_(10454, "result", lambda: result), "append"), _n_(10456, "x", lambda: x))
            _l_(10458)
        else:
            ctr = _n_(10459, "ctr", lambda: ctr) + 1
            _l_(10460)
    aux = _n_(10463, "result", lambda: result)
    _l_(10464)
    return aux
N = 4
_l_(10466)
_c_(10468, _n_(10467, "print", lambda: print), 'Original list:')
_l_(10469)
_c_(10472, _n_(10470, "print", lambda: print), _n_(10471, "nums", lambda: nums))
_l_(10473)
_c_(10475, _n_(10474, "print", lambda: print), '\nRemove first 4 even numbers from the said list:')
_l_(10476)
_c_(10482, _n_(10477, "print", lambda: print), _c_(10481, _n_(10478, "remove_items_con", lambda: remove_items_con), _n_(10479, "nums", lambda: nums), _n_(10480, "N", lambda: N)))
_l_(10483)