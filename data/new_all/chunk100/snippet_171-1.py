# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unique_sublists(input_list):
    _l_(103388)

    result = {}
    _l_(103362)
    for l in _n_(103363, "input_list", lambda: input_list):
        _l_(103375)

        _c_(103373, _a_(103372, _c_(103371, _a_(103365, _n_(103364, "result", lambda: result), "setdefault"), _c_(103368, _n_(103366, "tuple", lambda: tuple), _n_(103367, "l", lambda: l)), _c_(103370, _n_(103369, "list", lambda: list))), "append"), 1)
        _l_(103374)
    for a, b in _c_(103378, _a_(103377, _n_(103376, "result", lambda: result), "items")):
        _l_(103385)

        _n_(103379, "result", lambda: result)[_n_(103380, "a", lambda: a)] = _c_(103383, _n_(103381, "sum", lambda: sum), _n_(103382, "b", lambda: b))
        _l_(103384)
    aux = _n_(103386, "result", lambda: result)
    _l_(103387)
    return aux
_c_(103390, _n_(103389, "print", lambda: print), 'Original list:')
_l_(103391)
_c_(103394, _n_(103392, "print", lambda: print), _n_(103393, "list1", lambda: list1))
_l_(103395)
_c_(103397, _n_(103396, "print", lambda: print), 'Number of unique lists of the said list:')
_l_(103398)
_c_(103403, _n_(103399, "print", lambda: print), _c_(103402, _n_(103400, "unique_sublists", lambda: unique_sublists), _n_(103401, "list1", lambda: list1)))
_l_(103404)
color1 = [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
_l_(103405)
_c_(103407, _n_(103406, "print", lambda: print), '\nOriginal list:')
_l_(103408)
_c_(103411, _n_(103409, "print", lambda: print), _n_(103410, "color1", lambda: color1))
_l_(103412)
_c_(103414, _n_(103413, "print", lambda: print), 'Number of unique lists of the said list:')
_l_(103415)
_c_(103420, _n_(103416, "print", lambda: print), _c_(103419, _n_(103417, "unique_sublists", lambda: unique_sublists), _n_(103418, "color1", lambda: color1)))
_l_(103421)