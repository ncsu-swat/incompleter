# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def merge_lists(*args, fill_value=None):
    _l_(14422)

    max_length = _c_(14396, _n_(14391, "max", lambda: max), [_c_(14394, _n_(14392, "len", lambda: len), _n_(14393, "lst", lambda: lst)) for lst in _n_(14395, "args", lambda: args)])
    _l_(14397)
    for i in _c_(14400, _n_(14398, "range", lambda: range), _n_(14399, "max_length", lambda: max_length)):
        _l_(14419)

        _c_(14417, _a_(14402, _n_(14401, "result", lambda: result), "append"), [_n_(14403, "args", lambda: args)[_n_(14404, "k", lambda: k)][_n_(14405, "i", lambda: i)] if _n_(14406, "i", lambda: i) < _c_(14410, _n_(14407, "len", lambda: len), _n_(14408, "args", lambda: args)[_n_(14409, "k", lambda: k)]) else _n_(14411, "fill_value", lambda: fill_value) for k in _c_(14416, _n_(14412, "range", lambda: range), _c_(14415, _n_(14413, "len", lambda: len), _n_(14414, "args", lambda: args)))])
        _l_(14418)
    aux = _n_(14420, "result", lambda: result)
    _l_(14421)
    return aux
_c_(14424, _n_(14423, "print", lambda: print), 'After merging lists into a list of lists:')
_l_(14425)
_c_(14429, _n_(14426, "print", lambda: print), _c_(14428, _n_(14427, "merge_lists", lambda: merge_lists), ['a', 'b'], [1, 2], [True, False]))
_l_(14430)
_c_(14434, _n_(14431, "print", lambda: print), _c_(14433, _n_(14432, "merge_lists", lambda: merge_lists), ['a'], [1, 2], [True, False]))
_l_(14435)
_c_(14439, _n_(14436, "print", lambda: print), _c_(14438, _n_(14437, "merge_lists", lambda: merge_lists), ['a'], [1, 2], [True, False], fill_value='_'))
_l_(14440)