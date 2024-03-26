# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import copy
    _l_(107255)

except ImportError:
    pass
nums_x = {'a': 1, 'b': 2, 'cc': {'c': 3}}
_l_(107256)
_c_(107259, _n_(107257, "print", lambda: print), 'Original dictionary: ', _n_(107258, "nums_x", lambda: nums_x))
_l_(107260)
nums_y = _c_(107264, _a_(107262, _n_(107261, "copy", lambda: copy), "deepcopy"), _n_(107263, "nums_x", lambda: nums_x))
_l_(107265)
_c_(107267, _n_(107266, "print", lambda: print), '\nDeep copy of the said list:')
_l_(107268)
_c_(107271, _n_(107269, "print", lambda: print), _n_(107270, "nums_y", lambda: nums_y))
_l_(107272)
_c_(107274, _n_(107273, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(107275)
_n_(107276, "nums_x", lambda: nums_x)['cc']['c'] = 10
_l_(107277)
_c_(107280, _n_(107278, "print", lambda: print), _n_(107279, "nums_x", lambda: nums_x))
_l_(107281)
_c_(107283, _n_(107282, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(107284)
_c_(107287, _n_(107285, "print", lambda: print), _n_(107286, "nums_y", lambda: nums_y))
_l_(107288)
nums = {'x': 1, 'y': 2, 'zz': {'z': 3}}
_l_(107289)
_c_(107291, _n_(107290, "print", lambda: print), '\nOriginal dictionary :')
_l_(107292)
_c_(107295, _n_(107293, "print", lambda: print), _n_(107294, "nums", lambda: nums))
_l_(107296)
_c_(107298, _n_(107297, "print", lambda: print), '\nDeep copy of the said list:')
_l_(107299)
_c_(107302, _n_(107300, "print", lambda: print), _n_(107301, "nums_copy", lambda: nums_copy))
_l_(107303)
_c_(107305, _n_(107304, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(107306)
_n_(107307, "nums", lambda: nums)['zz']['z'] = 10
_l_(107308)
_c_(107310, _n_(107309, "print", lambda: print), '\nFirst dictionary:')
_l_(107311)
_c_(107314, _n_(107312, "print", lambda: print), _n_(107313, "nums", lambda: nums))
_l_(107315)
_c_(107317, _n_(107316, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(107318)
_c_(107321, _n_(107319, "print", lambda: print), _n_(107320, "nums_copy", lambda: nums_copy))
_l_(107322)