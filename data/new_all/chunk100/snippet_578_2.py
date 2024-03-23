# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import copy
    _l_(60038)

except ImportError:
    pass
nums_x = [1, [2, 3, 4]]
_l_(60039)
_c_(60042, _n_(60040, "print", lambda: print), 'Original list: ', _n_(60041, "nums_x", lambda: nums_x))
_l_(60043)
_c_(60045, _n_(60044, "print", lambda: print), '\nDeep copy of the said list:')
_l_(60046)
_c_(60049, _n_(60047, "print", lambda: print), _n_(60048, "nums_y", lambda: nums_y))
_l_(60050)
_c_(60052, _n_(60051, "print", lambda: print), '\nChange the value of an element of the original list:')
_l_(60053)
_n_(60054, "nums_x", lambda: nums_x)[1][1] = 10
_l_(60055)
_c_(60058, _n_(60056, "print", lambda: print), _n_(60057, "nums_x", lambda: nums_x))
_l_(60059)
_c_(60061, _n_(60060, "print", lambda: print), '\nCopy of the second list (Deep copy):')
_l_(60062)
_c_(60065, _n_(60063, "print", lambda: print), _n_(60064, "nums_y", lambda: nums_y))
_l_(60066)
nums = [[1, 2, 3], [4, 5, 6]]
_l_(60067)
deep_copy = _c_(60071, _a_(60069, _n_(60068, "copy", lambda: copy), "deepcopy"), _n_(60070, "nums", lambda: nums))
_l_(60072)
_c_(60074, _n_(60073, "print", lambda: print), '\nOriginal list:')
_l_(60075)
_c_(60078, _n_(60076, "print", lambda: print), _n_(60077, "nums", lambda: nums))
_l_(60079)
_c_(60081, _n_(60080, "print", lambda: print), '\nDeep copy of the said list:')
_l_(60082)
_c_(60085, _n_(60083, "print", lambda: print), _n_(60084, "deep_copy", lambda: deep_copy))
_l_(60086)
_c_(60088, _n_(60087, "print", lambda: print), '\nChange the value of some elements of the original list:')
_l_(60089)
_n_(60090, "nums", lambda: nums)[0][2] = 55
_l_(60091)
_n_(60092, "nums", lambda: nums)[1][1] = 77
_l_(60093)
_c_(60095, _n_(60094, "print", lambda: print), '\nOriginal list:')
_l_(60096)
_c_(60099, _n_(60097, "print", lambda: print), _n_(60098, "nums", lambda: nums))
_l_(60100)
_c_(60102, _n_(60101, "print", lambda: print), '\nSecond list (Deep copy):')
_l_(60103)
_c_(60106, _n_(60104, "print", lambda: print), _n_(60105, "deep_copy", lambda: deep_copy))
_l_(60107)