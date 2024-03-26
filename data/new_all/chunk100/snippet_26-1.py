# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import copy
    _l_(107324)

except ImportError:
    pass
nums_x = {'a': 1, 'b': 2, 'cc': {'c': 3}}
_l_(107325)
_c_(107328, _n_(107326, "print", lambda: print), 'Original dictionary: ', _n_(107327, "nums_x", lambda: nums_x))
_l_(107329)
_c_(107331, _n_(107330, "print", lambda: print), '\nDeep copy of the said list:')
_l_(107332)
_c_(107335, _n_(107333, "print", lambda: print), _n_(107334, "nums_y", lambda: nums_y))
_l_(107336)
_c_(107338, _n_(107337, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(107339)
_n_(107340, "nums_x", lambda: nums_x)['cc']['c'] = 10
_l_(107341)
_c_(107344, _n_(107342, "print", lambda: print), _n_(107343, "nums_x", lambda: nums_x))
_l_(107345)
_c_(107347, _n_(107346, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(107348)
_c_(107351, _n_(107349, "print", lambda: print), _n_(107350, "nums_y", lambda: nums_y))
_l_(107352)
nums = {'x': 1, 'y': 2, 'zz': {'z': 3}}
_l_(107353)
nums_copy = _c_(107357, _a_(107355, _n_(107354, "copy", lambda: copy), "deepcopy"), _n_(107356, "nums", lambda: nums))
_l_(107358)
_c_(107360, _n_(107359, "print", lambda: print), '\nOriginal dictionary :')
_l_(107361)
_c_(107364, _n_(107362, "print", lambda: print), _n_(107363, "nums", lambda: nums))
_l_(107365)
_c_(107367, _n_(107366, "print", lambda: print), '\nDeep copy of the said list:')
_l_(107368)
_c_(107371, _n_(107369, "print", lambda: print), _n_(107370, "nums_copy", lambda: nums_copy))
_l_(107372)
_c_(107374, _n_(107373, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(107375)
_n_(107376, "nums", lambda: nums)['zz']['z'] = 10
_l_(107377)
_c_(107379, _n_(107378, "print", lambda: print), '\nFirst dictionary:')
_l_(107380)
_c_(107383, _n_(107381, "print", lambda: print), _n_(107382, "nums", lambda: nums))
_l_(107384)
_c_(107386, _n_(107385, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(107387)
_c_(107390, _n_(107388, "print", lambda: print), _n_(107389, "nums_copy", lambda: nums_copy))
_l_(107391)