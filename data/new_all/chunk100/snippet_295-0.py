# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cyclically_iteration(lst, spec_index):
    _l_(108932)

    result = []
    _l_(108911)
    length = _c_(108914, _n_(108912, "len", lambda: len), _n_(108913, "lst", lambda: lst))
    _l_(108915)
    for i in _c_(108918, _n_(108916, "range", lambda: range), _n_(108917, "length", lambda: length)):
        _l_(108929)

        element_index = _n_(108919, "spec_index", lambda: spec_index) % _n_(108920, "length", lambda: length)
        _l_(108921)
        _c_(108926, _a_(108923, _n_(108922, "result", lambda: result), "append"), _n_(108924, "lst", lambda: lst)[_n_(108925, "element_index", lambda: element_index)])
        _l_(108927)
        spec_index += 1
        _l_(108928)
    aux = _n_(108930, "result", lambda: result)
    _l_(108931)
    return aux
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
_l_(108933)
_c_(108935, _n_(108934, "print", lambda: print), 'Original list:')
_l_(108936)
_c_(108939, _n_(108937, "print", lambda: print), _n_(108938, "chars", lambda: chars))
_l_(108940)
_c_(108943, _n_(108941, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(108942, "spec_index", lambda: spec_index), ':')
_l_(108944)
_c_(108950, _n_(108945, "print", lambda: print), _c_(108949, _n_(108946, "cyclically_iteration", lambda: cyclically_iteration), _n_(108947, "chars", lambda: chars), _n_(108948, "spec_index", lambda: spec_index)))
_l_(108951)
spec_index = 5
_l_(108952)
_c_(108955, _n_(108953, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(108954, "spec_index", lambda: spec_index), ':')
_l_(108956)
_c_(108962, _n_(108957, "print", lambda: print), _c_(108961, _n_(108958, "cyclically_iteration", lambda: cyclically_iteration), _n_(108959, "chars", lambda: chars), _n_(108960, "spec_index", lambda: spec_index)))
_l_(108963)