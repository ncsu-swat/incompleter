# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unique_sublists(input_list):
    _l_(12226)

    result = {}
    _l_(12200)
    for l in _n_(12201, "input_list", lambda: input_list):
        _l_(12213)

        _c_(12211, _a_(12210, _c_(12209, _a_(12203, _n_(12202, "result", lambda: result), "setdefault"), _c_(12206, _n_(12204, "tuple", lambda: tuple), _n_(12205, "l", lambda: l)), _c_(12208, _n_(12207, "list", lambda: list))), "append"), 1)
        _l_(12212)
    for (a, b) in _c_(12216, _a_(12215, _n_(12214, "result", lambda: result), "items")):
        _l_(12223)

        _n_(12217, "result", lambda: result)[_n_(12218, "a", lambda: a)] = _c_(12221, _n_(12219, "sum", lambda: sum), _n_(12220, "b", lambda: b))
        _l_(12222)
    aux = _n_(12224, "result", lambda: result)
    _l_(12225)
    return aux
list1 = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
_l_(12227)
_c_(12229, _n_(12228, "print", lambda: print), 'Original list:')
_l_(12230)
_c_(12233, _n_(12231, "print", lambda: print), _n_(12232, "list1", lambda: list1))
_l_(12234)
_c_(12236, _n_(12235, "print", lambda: print), 'Number of unique lists of the said list:')
_l_(12237)
_c_(12242, _n_(12238, "print", lambda: print), _c_(12241, _n_(12239, "unique_sublists", lambda: unique_sublists), _n_(12240, "list1", lambda: list1)))
_l_(12243)
_c_(12245, _n_(12244, "print", lambda: print), '\nOriginal list:')
_l_(12246)
_c_(12249, _n_(12247, "print", lambda: print), _n_(12248, "color1", lambda: color1))
_l_(12250)
_c_(12252, _n_(12251, "print", lambda: print), 'Number of unique lists of the said list:')
_l_(12253)
_c_(12258, _n_(12254, "print", lambda: print), _c_(12257, _n_(12255, "unique_sublists", lambda: unique_sublists), _n_(12256, "color1", lambda: color1)))
_l_(12259)