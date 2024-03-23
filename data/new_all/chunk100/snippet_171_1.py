# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unique_sublists(input_list):
    _l_(12165)

    for l in _n_(12140, "input_list", lambda: input_list):
        _l_(12152)

        _c_(12150, _a_(12149, _c_(12148, _a_(12142, _n_(12141, "result", lambda: result), "setdefault"), _c_(12145, _n_(12143, "tuple", lambda: tuple), _n_(12144, "l", lambda: l)), _c_(12147, _n_(12146, "list", lambda: list))), "append"), 1)
        _l_(12151)
    for (a, b) in _c_(12155, _a_(12154, _n_(12153, "result", lambda: result), "items")):
        _l_(12162)

        _n_(12156, "result", lambda: result)[_n_(12157, "a", lambda: a)] = _c_(12160, _n_(12158, "sum", lambda: sum), _n_(12159, "b", lambda: b))
        _l_(12161)
    aux = _n_(12163, "result", lambda: result)
    _l_(12164)
    return aux
list1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
_l_(12166)
_c_(12168, _n_(12167, "print", lambda: print), 'Original list:')
_l_(12169)
_c_(12172, _n_(12170, "print", lambda: print), _n_(12171, "list1", lambda: list1))
_l_(12173)
_c_(12175, _n_(12174, "print", lambda: print), 'Number of unique lists of the said list:')
_l_(12176)
_c_(12181, _n_(12177, "print", lambda: print), _c_(12180, _n_(12178, "unique_sublists", lambda: unique_sublists), _n_(12179, "list1", lambda: list1)))
_l_(12182)
color1 = [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
_l_(12183)
_c_(12185, _n_(12184, "print", lambda: print), '\nOriginal list:')
_l_(12186)
_c_(12189, _n_(12187, "print", lambda: print), _n_(12188, "color1", lambda: color1))
_l_(12190)
_c_(12192, _n_(12191, "print", lambda: print), 'Number of unique lists of the said list:')
_l_(12193)
_c_(12198, _n_(12194, "print", lambda: print), _c_(12197, _n_(12195, "unique_sublists", lambda: unique_sublists), _n_(12196, "color1", lambda: color1)))
_l_(12199)