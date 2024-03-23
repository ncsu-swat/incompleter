# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cyclically_iteration(lst, spec_index):
    _l_(25262)

    result = []
    _l_(25245)
    for i in _c_(25248, _n_(25246, "range", lambda: range), _n_(25247, "length", lambda: length)):
        _l_(25259)

        element_index = _n_(25249, "spec_index", lambda: spec_index) % _n_(25250, "length", lambda: length)
        _l_(25251)
        _c_(25256, _a_(25253, _n_(25252, "result", lambda: result), "append"), _n_(25254, "lst", lambda: lst)[_n_(25255, "element_index", lambda: element_index)])
        _l_(25257)
        spec_index += 1
        _l_(25258)
    aux = _n_(25260, "result", lambda: result)
    _l_(25261)
    return aux
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
_l_(25263)
_c_(25265, _n_(25264, "print", lambda: print), 'Original list:')
_l_(25266)
_c_(25269, _n_(25267, "print", lambda: print), _n_(25268, "chars", lambda: chars))
_l_(25270)
spec_index = 3
_l_(25271)
_c_(25274, _n_(25272, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(25273, "spec_index", lambda: spec_index), ':')
_l_(25275)
_c_(25281, _n_(25276, "print", lambda: print), _c_(25280, _n_(25277, "cyclically_iteration", lambda: cyclically_iteration), _n_(25278, "chars", lambda: chars), _n_(25279, "spec_index", lambda: spec_index)))
_l_(25282)
spec_index = 5
_l_(25283)
_c_(25286, _n_(25284, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(25285, "spec_index", lambda: spec_index), ':')
_l_(25287)
_c_(25293, _n_(25288, "print", lambda: print), _c_(25292, _n_(25289, "cyclically_iteration", lambda: cyclically_iteration), _n_(25290, "chars", lambda: chars), _n_(25291, "spec_index", lambda: spec_index)))
_l_(25294)