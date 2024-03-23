# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import copy
    _l_(21869)

except ImportError:
    pass
nums_x = {'a': 1, 'b': 2, 'cc': {'c': 3}}
_l_(21870)
_c_(21873, _n_(21871, "print", lambda: print), 'Original dictionary: ', _n_(21872, "nums_x", lambda: nums_x))
_l_(21874)
nums_y = _c_(21878, _a_(21876, _n_(21875, "copy", lambda: copy), "deepcopy"), _n_(21877, "nums_x", lambda: nums_x))
_l_(21879)
_c_(21881, _n_(21880, "print", lambda: print), '\nDeep copy of the said list:')
_l_(21882)
_c_(21885, _n_(21883, "print", lambda: print), _n_(21884, "nums_y", lambda: nums_y))
_l_(21886)
_c_(21888, _n_(21887, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(21889)
_n_(21890, "nums_x", lambda: nums_x)['cc']['c'] = 10
_l_(21891)
_c_(21894, _n_(21892, "print", lambda: print), _n_(21893, "nums_x", lambda: nums_x))
_l_(21895)
_c_(21897, _n_(21896, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(21898)
_c_(21901, _n_(21899, "print", lambda: print), _n_(21900, "nums_y", lambda: nums_y))
_l_(21902)
nums = {'x': 1, 'y': 2, 'zz': {'z': 3}}
_l_(21903)
_c_(21905, _n_(21904, "print", lambda: print), '\nOriginal dictionary :')
_l_(21906)
_c_(21909, _n_(21907, "print", lambda: print), _n_(21908, "nums", lambda: nums))
_l_(21910)
_c_(21912, _n_(21911, "print", lambda: print), '\nDeep copy of the said list:')
_l_(21913)
_c_(21916, _n_(21914, "print", lambda: print), _n_(21915, "nums_copy", lambda: nums_copy))
_l_(21917)
_c_(21919, _n_(21918, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(21920)
_n_(21921, "nums", lambda: nums)['zz']['z'] = 10
_l_(21922)
_c_(21924, _n_(21923, "print", lambda: print), '\nFirst dictionary:')
_l_(21925)
_c_(21928, _n_(21926, "print", lambda: print), _n_(21927, "nums", lambda: nums))
_l_(21929)
_c_(21931, _n_(21930, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(21932)
_c_(21935, _n_(21933, "print", lambda: print), _n_(21934, "nums_copy", lambda: nums_copy))
_l_(21936)