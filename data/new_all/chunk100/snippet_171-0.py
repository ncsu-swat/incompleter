# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unique_sublists(input_list):
    _l_(103328)

    result = {}
    _l_(103302)
    for l in _n_(103303, "input_list", lambda: input_list):
        _l_(103315)

        _c_(103313, _a_(103312, _c_(103311, _a_(103305, _n_(103304, "result", lambda: result), "setdefault"), _c_(103308, _n_(103306, "tuple", lambda: tuple), _n_(103307, "l", lambda: l)), _c_(103310, _n_(103309, "list", lambda: list))), "append"), 1)
        _l_(103314)
    for a, b in _c_(103318, _a_(103317, _n_(103316, "result", lambda: result), "items")):
        _l_(103325)

        _n_(103319, "result", lambda: result)[_n_(103320, "a", lambda: a)] = _c_(103323, _n_(103321, "sum", lambda: sum), _n_(103322, "b", lambda: b))
        _l_(103324)
    aux = _n_(103326, "result", lambda: result)
    _l_(103327)
    return aux
list1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
_l_(103329)
_c_(103331, _n_(103330, "print", lambda: print), 'Original list:')
_l_(103332)
_c_(103335, _n_(103333, "print", lambda: print), _n_(103334, "list1", lambda: list1))
_l_(103336)
_c_(103338, _n_(103337, "print", lambda: print), 'Number of unique lists of the said list:')
_l_(103339)
_c_(103344, _n_(103340, "print", lambda: print), _c_(103343, _n_(103341, "unique_sublists", lambda: unique_sublists), _n_(103342, "list1", lambda: list1)))
_l_(103345)
_c_(103347, _n_(103346, "print", lambda: print), '\nOriginal list:')
_l_(103348)
_c_(103351, _n_(103349, "print", lambda: print), _n_(103350, "color1", lambda: color1))
_l_(103352)
_c_(103354, _n_(103353, "print", lambda: print), 'Number of unique lists of the said list:')
_l_(103355)
_c_(103360, _n_(103356, "print", lambda: print), _c_(103359, _n_(103357, "unique_sublists", lambda: unique_sublists), _n_(103358, "color1", lambda: color1)))
_l_(103361)