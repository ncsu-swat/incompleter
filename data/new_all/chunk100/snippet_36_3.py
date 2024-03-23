# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(36398)

except ImportError:
    pass

def cartesian_product(lists):
    _l_(36406)

    aux = _c_(36404, _n_(36399, "list", lambda: list), _c_(36403, _a_(36401, _n_(36400, "itertools", lambda: itertools), "product"), *_n_(36402, "lists", lambda: lists)))
    _l_(36405)
    return aux
ls = [[1, 2], [3, 4]]
_l_(36407)
_c_(36410, _n_(36408, "print", lambda: print), 'Original Lists:', _n_(36409, "ls", lambda: ls))
_l_(36411)
_c_(36416, _n_(36412, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36415, _n_(36413, "cartesian_product", lambda: cartesian_product), _n_(36414, "ls", lambda: ls)))
_l_(36417)
_c_(36420, _n_(36418, "print", lambda: print), '\nOriginal Lists:', _n_(36419, "ls", lambda: ls))
_l_(36421)
_c_(36426, _n_(36422, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36425, _n_(36423, "cartesian_product", lambda: cartesian_product), _n_(36424, "ls", lambda: ls)))
_l_(36427)
ls = [[], [1, 2, 3]]
_l_(36428)
_c_(36431, _n_(36429, "print", lambda: print), '\nOriginal Lists:', _n_(36430, "ls", lambda: ls))
_l_(36432)
_c_(36437, _n_(36433, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36436, _n_(36434, "cartesian_product", lambda: cartesian_product), _n_(36435, "ls", lambda: ls)))
_l_(36438)
ls = [[1, 2], []]
_l_(36439)
_c_(36442, _n_(36440, "print", lambda: print), '\nOriginal Lists:', _n_(36441, "ls", lambda: ls))
_l_(36443)
_c_(36448, _n_(36444, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36447, _n_(36445, "cartesian_product", lambda: cartesian_product), _n_(36446, "ls", lambda: ls)))
_l_(36449)