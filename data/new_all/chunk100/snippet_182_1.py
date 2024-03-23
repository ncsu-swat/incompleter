# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def merge_lists(*args, fill_value=None):
    _l_(14466)

    result = []
    _l_(14441)
    for i in _c_(14444, _n_(14442, "range", lambda: range), _n_(14443, "max_length", lambda: max_length)):
        _l_(14463)

        _c_(14461, _a_(14446, _n_(14445, "result", lambda: result), "append"), [_n_(14447, "args", lambda: args)[_n_(14448, "k", lambda: k)][_n_(14449, "i", lambda: i)] if _n_(14450, "i", lambda: i) < _c_(14454, _n_(14451, "len", lambda: len), _n_(14452, "args", lambda: args)[_n_(14453, "k", lambda: k)]) else _n_(14455, "fill_value", lambda: fill_value) for k in _c_(14460, _n_(14456, "range", lambda: range), _c_(14459, _n_(14457, "len", lambda: len), _n_(14458, "args", lambda: args)))])
        _l_(14462)
    aux = _n_(14464, "result", lambda: result)
    _l_(14465)
    return aux
_c_(14468, _n_(14467, "print", lambda: print), 'After merging lists into a list of lists:')
_l_(14469)
_c_(14473, _n_(14470, "print", lambda: print), _c_(14472, _n_(14471, "merge_lists", lambda: merge_lists), ['a', 'b'], [1, 2], [True, False]))
_l_(14474)
_c_(14478, _n_(14475, "print", lambda: print), _c_(14477, _n_(14476, "merge_lists", lambda: merge_lists), ['a'], [1, 2], [True, False]))
_l_(14479)
_c_(14483, _n_(14480, "print", lambda: print), _c_(14482, _n_(14481, "merge_lists", lambda: merge_lists), ['a'], [1, 2], [True, False], fill_value='_'))
_l_(14484)