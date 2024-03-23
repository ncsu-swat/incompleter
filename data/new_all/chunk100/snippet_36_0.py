# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(36239)

except ImportError:
    pass

def cartesian_product(lists):
    _l_(36247)

    aux = _c_(36245, _n_(36240, "list", lambda: list), _c_(36244, _a_(36242, _n_(36241, "itertools", lambda: itertools), "product"), *_n_(36243, "lists", lambda: lists)))
    _l_(36246)
    return aux
ls = [[1, 2], [3, 4]]
_l_(36248)
_c_(36251, _n_(36249, "print", lambda: print), 'Original Lists:', _n_(36250, "ls", lambda: ls))
_l_(36252)
_c_(36257, _n_(36253, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36256, _n_(36254, "cartesian_product", lambda: cartesian_product), _n_(36255, "ls", lambda: ls)))
_l_(36258)
ls = [[1, 2, 3], [3, 4, 5]]
_l_(36259)
_c_(36262, _n_(36260, "print", lambda: print), '\nOriginal Lists:', _n_(36261, "ls", lambda: ls))
_l_(36263)
_c_(36268, _n_(36264, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36267, _n_(36265, "cartesian_product", lambda: cartesian_product), _n_(36266, "ls", lambda: ls)))
_l_(36269)
_c_(36272, _n_(36270, "print", lambda: print), '\nOriginal Lists:', _n_(36271, "ls", lambda: ls))
_l_(36273)
_c_(36278, _n_(36274, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36277, _n_(36275, "cartesian_product", lambda: cartesian_product), _n_(36276, "ls", lambda: ls)))
_l_(36279)
ls = [[1, 2], []]
_l_(36280)
_c_(36283, _n_(36281, "print", lambda: print), '\nOriginal Lists:', _n_(36282, "ls", lambda: ls))
_l_(36284)
_c_(36289, _n_(36285, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36288, _n_(36286, "cartesian_product", lambda: cartesian_product), _n_(36287, "ls", lambda: ls)))
_l_(36290)