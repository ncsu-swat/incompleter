# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(36292)

except ImportError:
    pass

def cartesian_product(lists):
    _l_(36300)

    aux = _c_(36298, _n_(36293, "list", lambda: list), _c_(36297, _a_(36295, _n_(36294, "itertools", lambda: itertools), "product"), *_n_(36296, "lists", lambda: lists)))
    _l_(36299)
    return aux
_c_(36303, _n_(36301, "print", lambda: print), 'Original Lists:', _n_(36302, "ls", lambda: ls))
_l_(36304)
_c_(36309, _n_(36305, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36308, _n_(36306, "cartesian_product", lambda: cartesian_product), _n_(36307, "ls", lambda: ls)))
_l_(36310)
ls = [[1, 2, 3], [3, 4, 5]]
_l_(36311)
_c_(36314, _n_(36312, "print", lambda: print), '\nOriginal Lists:', _n_(36313, "ls", lambda: ls))
_l_(36315)
_c_(36320, _n_(36316, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36319, _n_(36317, "cartesian_product", lambda: cartesian_product), _n_(36318, "ls", lambda: ls)))
_l_(36321)
ls = [[], [1, 2, 3]]
_l_(36322)
_c_(36325, _n_(36323, "print", lambda: print), '\nOriginal Lists:', _n_(36324, "ls", lambda: ls))
_l_(36326)
_c_(36331, _n_(36327, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36330, _n_(36328, "cartesian_product", lambda: cartesian_product), _n_(36329, "ls", lambda: ls)))
_l_(36332)
ls = [[1, 2], []]
_l_(36333)
_c_(36336, _n_(36334, "print", lambda: print), '\nOriginal Lists:', _n_(36335, "ls", lambda: ls))
_l_(36337)
_c_(36342, _n_(36338, "print", lambda: print), 'Cartesian product of the said lists: ', _c_(36341, _n_(36339, "cartesian_product", lambda: cartesian_product), _n_(36340, "ls", lambda: ls)))
_l_(36343)