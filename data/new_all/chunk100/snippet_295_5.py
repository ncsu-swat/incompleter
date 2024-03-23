# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cyclically_iteration(lst, spec_index):
    _l_(25313)

    result = []
    _l_(25295)
    length = _c_(25298, _n_(25296, "len", lambda: len), _n_(25297, "lst", lambda: lst))
    _l_(25299)
    for i in _c_(25302, _n_(25300, "range", lambda: range), _n_(25301, "length", lambda: length)):
        _l_(25310)

        _c_(25307, _a_(25304, _n_(25303, "result", lambda: result), "append"), _n_(25305, "lst", lambda: lst)[_n_(25306, "element_index", lambda: element_index)])
        _l_(25308)
        spec_index += 1
        _l_(25309)
    aux = _n_(25311, "result", lambda: result)
    _l_(25312)
    return aux
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
_l_(25314)
_c_(25316, _n_(25315, "print", lambda: print), 'Original list:')
_l_(25317)
_c_(25320, _n_(25318, "print", lambda: print), _n_(25319, "chars", lambda: chars))
_l_(25321)
spec_index = 3
_l_(25322)
_c_(25325, _n_(25323, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(25324, "spec_index", lambda: spec_index), ':')
_l_(25326)
_c_(25332, _n_(25327, "print", lambda: print), _c_(25331, _n_(25328, "cyclically_iteration", lambda: cyclically_iteration), _n_(25329, "chars", lambda: chars), _n_(25330, "spec_index", lambda: spec_index)))
_l_(25333)
spec_index = 5
_l_(25334)
_c_(25337, _n_(25335, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(25336, "spec_index", lambda: spec_index), ':')
_l_(25338)
_c_(25344, _n_(25339, "print", lambda: print), _c_(25343, _n_(25340, "cyclically_iteration", lambda: cyclically_iteration), _n_(25341, "chars", lambda: chars), _n_(25342, "spec_index", lambda: spec_index)))
_l_(25345)