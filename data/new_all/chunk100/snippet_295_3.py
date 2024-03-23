# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cyclically_iteration(lst, spec_index):
    _l_(25213)

    result = []
    _l_(25192)
    length = _c_(25195, _n_(25193, "len", lambda: len), _n_(25194, "lst", lambda: lst))
    _l_(25196)
    for i in _c_(25199, _n_(25197, "range", lambda: range), _n_(25198, "length", lambda: length)):
        _l_(25210)

        element_index = _n_(25200, "spec_index", lambda: spec_index) % _n_(25201, "length", lambda: length)
        _l_(25202)
        _c_(25207, _a_(25204, _n_(25203, "result", lambda: result), "append"), _n_(25205, "lst", lambda: lst)[_n_(25206, "element_index", lambda: element_index)])
        _l_(25208)
        spec_index += 1
        _l_(25209)
    aux = _n_(25211, "result", lambda: result)
    _l_(25212)
    return aux
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
_l_(25214)
_c_(25216, _n_(25215, "print", lambda: print), 'Original list:')
_l_(25217)
_c_(25220, _n_(25218, "print", lambda: print), _n_(25219, "chars", lambda: chars))
_l_(25221)
spec_index = 3
_l_(25222)
_c_(25225, _n_(25223, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(25224, "spec_index", lambda: spec_index), ':')
_l_(25226)
_c_(25232, _n_(25227, "print", lambda: print), _c_(25231, _n_(25228, "cyclically_iteration", lambda: cyclically_iteration), _n_(25229, "chars", lambda: chars), _n_(25230, "spec_index", lambda: spec_index)))
_l_(25233)
_c_(25236, _n_(25234, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(25235, "spec_index", lambda: spec_index), ':')
_l_(25237)
_c_(25243, _n_(25238, "print", lambda: print), _c_(25242, _n_(25239, "cyclically_iteration", lambda: cyclically_iteration), _n_(25240, "chars", lambda: chars), _n_(25241, "spec_index", lambda: spec_index)))
_l_(25244)