# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cyclically_iteration(lst, spec_index):
    _l_(25160)

    result = []
    _l_(25139)
    length = _c_(25142, _n_(25140, "len", lambda: len), _n_(25141, "lst", lambda: lst))
    _l_(25143)
    for i in _c_(25146, _n_(25144, "range", lambda: range), _n_(25145, "length", lambda: length)):
        _l_(25157)

        element_index = _n_(25147, "spec_index", lambda: spec_index) % _n_(25148, "length", lambda: length)
        _l_(25149)
        _c_(25154, _a_(25151, _n_(25150, "result", lambda: result), "append"), _n_(25152, "lst", lambda: lst)[_n_(25153, "element_index", lambda: element_index)])
        _l_(25155)
        spec_index += 1
        _l_(25156)
    aux = _n_(25158, "result", lambda: result)
    _l_(25159)
    return aux
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
_l_(25161)
_c_(25163, _n_(25162, "print", lambda: print), 'Original list:')
_l_(25164)
_c_(25167, _n_(25165, "print", lambda: print), _n_(25166, "chars", lambda: chars))
_l_(25168)
_c_(25171, _n_(25169, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(25170, "spec_index", lambda: spec_index), ':')
_l_(25172)
_c_(25178, _n_(25173, "print", lambda: print), _c_(25177, _n_(25174, "cyclically_iteration", lambda: cyclically_iteration), _n_(25175, "chars", lambda: chars), _n_(25176, "spec_index", lambda: spec_index)))
_l_(25179)
spec_index = 5
_l_(25180)
_c_(25183, _n_(25181, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(25182, "spec_index", lambda: spec_index), ':')
_l_(25184)
_c_(25190, _n_(25185, "print", lambda: print), _c_(25189, _n_(25186, "cyclically_iteration", lambda: cyclically_iteration), _n_(25187, "chars", lambda: chars), _n_(25188, "spec_index", lambda: spec_index)))
_l_(25191)