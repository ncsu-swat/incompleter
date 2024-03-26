# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def cyclically_iteration(lst, spec_index):
    _l_(108985)

    result = []
    _l_(108964)
    length = _c_(108967, _n_(108965, "len", lambda: len), _n_(108966, "lst", lambda: lst))
    _l_(108968)
    for i in _c_(108971, _n_(108969, "range", lambda: range), _n_(108970, "length", lambda: length)):
        _l_(108982)

        element_index = _n_(108972, "spec_index", lambda: spec_index) % _n_(108973, "length", lambda: length)
        _l_(108974)
        _c_(108979, _a_(108976, _n_(108975, "result", lambda: result), "append"), _n_(108977, "lst", lambda: lst)[_n_(108978, "element_index", lambda: element_index)])
        _l_(108980)
        spec_index += 1
        _l_(108981)
    aux = _n_(108983, "result", lambda: result)
    _l_(108984)
    return aux
_c_(108987, _n_(108986, "print", lambda: print), 'Original list:')
_l_(108988)
_c_(108991, _n_(108989, "print", lambda: print), _n_(108990, "chars", lambda: chars))
_l_(108992)
spec_index = 3
_l_(108993)
_c_(108996, _n_(108994, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(108995, "spec_index", lambda: spec_index), ':')
_l_(108997)
_c_(109003, _n_(108998, "print", lambda: print), _c_(109002, _n_(108999, "cyclically_iteration", lambda: cyclically_iteration), _n_(109000, "chars", lambda: chars), _n_(109001, "spec_index", lambda: spec_index)))
_l_(109004)
spec_index = 5
_l_(109005)
_c_(109008, _n_(109006, "print", lambda: print), '\nIterate the said  list cyclically on specific index position', _n_(109007, "spec_index", lambda: spec_index), ':')
_l_(109009)
_c_(109015, _n_(109010, "print", lambda: print), _c_(109014, _n_(109011, "cyclically_iteration", lambda: cyclically_iteration), _n_(109012, "chars", lambda: chars), _n_(109013, "spec_index", lambda: spec_index)))
_l_(109016)