# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cyclically_iteration(lst, spec_index):
    _l_(25107)

    result = []
    _l_(25086)
    length = _c_(25089, _n_(25087, "len", lambda: len), _n_(25088, "lst", lambda: lst))
    _l_(25090)
    for i in _c_(25093, _n_(25091, "range", lambda: range), _n_(25092, "length", lambda: length)):
        _l_(25104)

        element_index = _n_(25094, "spec_index", lambda: spec_index) % _n_(25095, "length", lambda: length)
        _l_(25096)
        _c_(25101, _a_(25098, _n_(25097, "result", lambda: result), "append"), _n_(25099, "lst", lambda: lst)[_n_(25100, "element_index", lambda: element_index)])
        _l_(25102)
        spec_index += 1
        _l_(25103)
    aux = _n_(25105, "result", lambda: result)
    _l_(25106)
    return aux
_c_(25109, _n_(25108, "print", lambda: print), 'Original list:')
_l_(25110)
_c_(25113, _n_(25111, "print", lambda: print), _n_(25112, "chars", lambda: chars))
_l_(25114)
spec_index = 3
_l_(25115)
_c_(25118, _n_(25116, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(25117, "spec_index", lambda: spec_index), ':')
_l_(25119)
_c_(25125, _n_(25120, "print", lambda: print), _c_(25124, _n_(25121, "cyclically_iteration", lambda: cyclically_iteration), _n_(25122, "chars", lambda: chars), _n_(25123, "spec_index", lambda: spec_index)))
_l_(25126)
spec_index = 5
_l_(25127)
_c_(25130, _n_(25128, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(25129, "spec_index", lambda: spec_index), ':')
_l_(25131)
_c_(25137, _n_(25132, "print", lambda: print), _c_(25136, _n_(25133, "cyclically_iteration", lambda: cyclically_iteration), _n_(25134, "chars", lambda: chars), _n_(25135, "spec_index", lambda: spec_index)))
_l_(25138)