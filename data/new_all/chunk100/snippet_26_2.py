# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import copy
    _l_(21796)

except ImportError:
    pass
nums_x = {'a': 1, 'b': 2, 'cc': {'c': 3}}
_l_(21797)
_c_(21800, _n_(21798, "print", lambda: print), 'Original dictionary: ', _n_(21799, "nums_x", lambda: nums_x))
_l_(21801)
nums_y = _c_(21805, _a_(21803, _n_(21802, "copy", lambda: copy), "deepcopy"), _n_(21804, "nums_x", lambda: nums_x))
_l_(21806)
_c_(21808, _n_(21807, "print", lambda: print), '\nDeep copy of the said list:')
_l_(21809)
_c_(21812, _n_(21810, "print", lambda: print), _n_(21811, "nums_y", lambda: nums_y))
_l_(21813)
_c_(21815, _n_(21814, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(21816)
_n_(21817, "nums_x", lambda: nums_x)['cc']['c'] = 10
_l_(21818)
_c_(21821, _n_(21819, "print", lambda: print), _n_(21820, "nums_x", lambda: nums_x))
_l_(21822)
_c_(21824, _n_(21823, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(21825)
_c_(21828, _n_(21826, "print", lambda: print), _n_(21827, "nums_y", lambda: nums_y))
_l_(21829)
nums_copy = _c_(21833, _a_(21831, _n_(21830, "copy", lambda: copy), "deepcopy"), _n_(21832, "nums", lambda: nums))
_l_(21834)
_c_(21836, _n_(21835, "print", lambda: print), '\nOriginal dictionary :')
_l_(21837)
_c_(21840, _n_(21838, "print", lambda: print), _n_(21839, "nums", lambda: nums))
_l_(21841)
_c_(21843, _n_(21842, "print", lambda: print), '\nDeep copy of the said list:')
_l_(21844)
_c_(21847, _n_(21845, "print", lambda: print), _n_(21846, "nums_copy", lambda: nums_copy))
_l_(21848)
_c_(21850, _n_(21849, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(21851)
_n_(21852, "nums", lambda: nums)['zz']['z'] = 10
_l_(21853)
_c_(21855, _n_(21854, "print", lambda: print), '\nFirst dictionary:')
_l_(21856)
_c_(21859, _n_(21857, "print", lambda: print), _n_(21858, "nums", lambda: nums))
_l_(21860)
_c_(21862, _n_(21861, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(21863)
_c_(21866, _n_(21864, "print", lambda: print), _n_(21865, "nums_copy", lambda: nums_copy))
_l_(21867)