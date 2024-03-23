# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test_dsc(n):
    _l_(26268)

    aux = _c_(26266, _n_(26258, "int", lambda: int), _c_(26265, _a_(26259, '', "join"), _c_(26264, _n_(26260, "sorted", lambda: sorted), _c_(26263, _n_(26261, "str", lambda: str), _n_(26262, "n", lambda: n)), reverse=True)))
    _l_(26267)
    return aux

def test_asc(n):
    _l_(26281)

    aux = _c_(26279, _n_(26269, "int", lambda: int), _c_(26278, _a_(26270, '', "join"), _c_(26277, _n_(26271, "sorted", lambda: sorted), _c_(26276, _n_(26272, "list", lambda: list), _c_(26275, _n_(26273, "str", lambda: str), _n_(26274, "n", lambda: n)))))[::1])
    _l_(26280)
    return aux
n = 134543
_l_(26282)
_c_(26285, _n_(26283, "print", lambda: print), 'Original Number: ', _n_(26284, "n", lambda: n))
_l_(26286)
_c_(26291, _n_(26287, "print", lambda: print), 'Descending order of the said number: ', _c_(26290, _n_(26288, "test_dsc", lambda: test_dsc), _n_(26289, "n", lambda: n)))
_l_(26292)
_c_(26297, _n_(26293, "print", lambda: print), 'Ascending order of the said number: ', _c_(26296, _n_(26294, "test_asc", lambda: test_asc), _n_(26295, "n", lambda: n)))
_l_(26298)
_c_(26301, _n_(26299, "print", lambda: print), '\nOriginal Number: ', _n_(26300, "n", lambda: n))
_l_(26302)
_c_(26307, _n_(26303, "print", lambda: print), 'Descending order of the said number: ', _c_(26306, _n_(26304, "test_dsc", lambda: test_dsc), _n_(26305, "n", lambda: n)))
_l_(26308)
_c_(26313, _n_(26309, "print", lambda: print), 'Ascending order of the said number: ', _c_(26312, _n_(26310, "test_asc", lambda: test_asc), _n_(26311, "n", lambda: n)))
_l_(26314)