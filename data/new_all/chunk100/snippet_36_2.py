# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(36345)

except ImportError:
    pass

def cartesian_product(lists):
    _l_(36353)

    aux = _c_(36351, _n_(36346, "list", lambda: list), _c_(36350, _a_(36348, _n_(36347, "itertools", lambda: itertools), "product"), *_n_(36349, "lists", lambda: lists)))
    _l_(36352)
    return aux
ls = [[1, 2], [3, 4]]
_l_(36354)
_c_(36357, _n_(36355, "print", lambda: print), 'Original Lists:', _n_(36356, "ls", lambda: ls))
_l_(36358)
_c_(36363, _n_(36359, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36362, _n_(36360, "cartesian_product", lambda: cartesian_product), _n_(36361, "ls", lambda: ls)))
_l_(36364)
ls = [[1, 2, 3], [3, 4, 5]]
_l_(36365)
_c_(36368, _n_(36366, "print", lambda: print), '\nOriginal Lists:', _n_(36367, "ls", lambda: ls))
_l_(36369)
_c_(36374, _n_(36370, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36373, _n_(36371, "cartesian_product", lambda: cartesian_product), _n_(36372, "ls", lambda: ls)))
_l_(36375)
ls = [[], [1, 2, 3]]
_l_(36376)
_c_(36379, _n_(36377, "print", lambda: print), '\nOriginal Lists:', _n_(36378, "ls", lambda: ls))
_l_(36380)
_c_(36385, _n_(36381, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36384, _n_(36382, "cartesian_product", lambda: cartesian_product), _n_(36383, "ls", lambda: ls)))
_l_(36386)
_c_(36389, _n_(36387, "print", lambda: print), '\nOriginal Lists:', _n_(36388, "ls", lambda: ls))
_l_(36390)
_c_(36395, _n_(36391, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36394, _n_(36392, "cartesian_product", lambda: cartesian_product), _n_(36393, "ls", lambda: ls)))
_l_(36396)