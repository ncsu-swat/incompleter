# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(98164)

except ImportError:
    pass

def permutations_data(iter, length):
    _l_(98171)

    aux = _c_(98169, _a_(98166, _n_(98165, "it", lambda: it), "permutations"), _n_(98167, "iter", lambda: iter), _n_(98168, "length", lambda: length))
    _l_(98170)
    return aux
result = _c_(98173, _n_(98172, "permutations_data", lambda: permutations_data), ['A', 'B', 'C', 'D'], 3)
_l_(98174)
_c_(98176, _n_(98175, "print", lambda: print), '\nIterator to get specified number of permutations of elements:')
_l_(98177)
for i in _n_(98178, "result", lambda: result):
    _l_(98183)

    _c_(98181, _n_(98179, "print", lambda: print), _n_(98180, "i", lambda: i))
    _l_(98182)
_c_(98185, _n_(98184, "print", lambda: print), '\nIterator to get specified number of permutations of elements:')
_l_(98186)
for i in _n_(98187, "result", lambda: result):
    _l_(98192)

    _c_(98190, _n_(98188, "print", lambda: print), _n_(98189, "i", lambda: i))
    _l_(98191)