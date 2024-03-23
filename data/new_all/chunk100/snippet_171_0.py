# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unique_sublists(input_list):
    _l_(12106)

    result = {}
    _l_(12080)
    for l in _n_(12081, "input_list", lambda: input_list):
        _l_(12093)

        _c_(12091, _a_(12090, _c_(12089, _a_(12083, _n_(12082, "result", lambda: result), "setdefault"), _c_(12086, _n_(12084, "tuple", lambda: tuple), _n_(12085, "l", lambda: l)), _c_(12088, _n_(12087, "list", lambda: list))), "append"), 1)
        _l_(12092)
    for (a, b) in _c_(12096, _a_(12095, _n_(12094, "result", lambda: result), "items")):
        _l_(12103)

        _n_(12097, "result", lambda: result)[_n_(12098, "a", lambda: a)] = _c_(12101, _n_(12099, "sum", lambda: sum), _n_(12100, "b", lambda: b))
        _l_(12102)
    aux = _n_(12104, "result", lambda: result)
    _l_(12105)
    return aux
_c_(12108, _n_(12107, "print", lambda: print), 'Original list:')
_l_(12109)
_c_(12112, _n_(12110, "print", lambda: print), _n_(12111, "list1", lambda: list1))
_l_(12113)
_c_(12115, _n_(12114, "print", lambda: print), 'Number of unique lists of the said list:')
_l_(12116)
_c_(12121, _n_(12117, "print", lambda: print), _c_(12120, _n_(12118, "unique_sublists", lambda: unique_sublists), _n_(12119, "list1", lambda: list1)))
_l_(12122)
color1 = [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
_l_(12123)
_c_(12125, _n_(12124, "print", lambda: print), '\nOriginal list:')
_l_(12126)
_c_(12129, _n_(12127, "print", lambda: print), _n_(12128, "color1", lambda: color1))
_l_(12130)
_c_(12132, _n_(12131, "print", lambda: print), 'Number of unique lists of the said list:')
_l_(12133)
_c_(12138, _n_(12134, "print", lambda: print), _c_(12137, _n_(12135, "unique_sublists", lambda: unique_sublists), _n_(12136, "color1", lambda: color1)))
_l_(12139)