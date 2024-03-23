# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cyclically_iteration(lst, spec_index):
    _l_(25053)

    length = _c_(25035, _n_(25033, "len", lambda: len), _n_(25034, "lst", lambda: lst))
    _l_(25036)
    for i in _c_(25039, _n_(25037, "range", lambda: range), _n_(25038, "length", lambda: length)):
        _l_(25050)

        element_index = _n_(25040, "spec_index", lambda: spec_index) % _n_(25041, "length", lambda: length)
        _l_(25042)
        _c_(25047, _a_(25044, _n_(25043, "result", lambda: result), "append"), _n_(25045, "lst", lambda: lst)[_n_(25046, "element_index", lambda: element_index)])
        _l_(25048)
        spec_index += 1
        _l_(25049)
    aux = _n_(25051, "result", lambda: result)
    _l_(25052)
    return aux
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
_l_(25054)
_c_(25056, _n_(25055, "print", lambda: print), 'Original list:')
_l_(25057)
_c_(25060, _n_(25058, "print", lambda: print), _n_(25059, "chars", lambda: chars))
_l_(25061)
spec_index = 3
_l_(25062)
_c_(25065, _n_(25063, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(25064, "spec_index", lambda: spec_index), ':')
_l_(25066)
_c_(25072, _n_(25067, "print", lambda: print), _c_(25071, _n_(25068, "cyclically_iteration", lambda: cyclically_iteration), _n_(25069, "chars", lambda: chars), _n_(25070, "spec_index", lambda: spec_index)))
_l_(25073)
spec_index = 5
_l_(25074)
_c_(25077, _n_(25075, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(25076, "spec_index", lambda: spec_index), ':')
_l_(25078)
_c_(25084, _n_(25079, "print", lambda: print), _c_(25083, _n_(25080, "cyclically_iteration", lambda: cyclically_iteration), _n_(25081, "chars", lambda: chars), _n_(25082, "spec_index", lambda: spec_index)))
_l_(25085)