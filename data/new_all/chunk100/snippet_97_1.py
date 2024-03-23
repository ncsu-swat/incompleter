# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(98194)

except ImportError:
    pass

def permutations_data(iter, length):
    _l_(98201)

    aux = _c_(98199, _a_(98196, _n_(98195, "it", lambda: it), "permutations"), _n_(98197, "iter", lambda: iter), _n_(98198, "length", lambda: length))
    _l_(98200)
    return aux
_c_(98203, _n_(98202, "print", lambda: print), '\nIterator to get specified number of permutations of elements:')
_l_(98204)
for i in _n_(98205, "result", lambda: result):
    _l_(98210)

    _c_(98208, _n_(98206, "print", lambda: print), _n_(98207, "i", lambda: i))
    _l_(98209)
result = _c_(98212, _n_(98211, "permutations_data", lambda: permutations_data), 'Python', 2)
_l_(98213)
_c_(98215, _n_(98214, "print", lambda: print), '\nIterator to get specified number of permutations of elements:')
_l_(98216)
for i in _n_(98217, "result", lambda: result):
    _l_(98222)

    _c_(98220, _n_(98218, "print", lambda: print), _n_(98219, "i", lambda: i))
    _l_(98221)