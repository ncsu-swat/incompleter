# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import copy
    _l_(59888)

except ImportError:
    pass
_c_(59891, _n_(59889, "print", lambda: print), 'Original list: ', _n_(59890, "nums_x", lambda: nums_x))
_l_(59892)
nums_y = _c_(59896, _a_(59894, _n_(59893, "copy", lambda: copy), "deepcopy"), _n_(59895, "nums_x", lambda: nums_x))
_l_(59897)
_c_(59899, _n_(59898, "print", lambda: print), '\nDeep copy of the said list:')
_l_(59900)
_c_(59903, _n_(59901, "print", lambda: print), _n_(59902, "nums_y", lambda: nums_y))
_l_(59904)
_c_(59906, _n_(59905, "print", lambda: print), '\nChange the value of an element of the original list:')
_l_(59907)
_n_(59908, "nums_x", lambda: nums_x)[1][1] = 10
_l_(59909)
_c_(59912, _n_(59910, "print", lambda: print), _n_(59911, "nums_x", lambda: nums_x))
_l_(59913)
_c_(59915, _n_(59914, "print", lambda: print), '\nCopy of the second list (Deep copy):')
_l_(59916)
_c_(59919, _n_(59917, "print", lambda: print), _n_(59918, "nums_y", lambda: nums_y))
_l_(59920)
nums = [[1, 2, 3], [4, 5, 6]]
_l_(59921)
deep_copy = _c_(59925, _a_(59923, _n_(59922, "copy", lambda: copy), "deepcopy"), _n_(59924, "nums", lambda: nums))
_l_(59926)
_c_(59928, _n_(59927, "print", lambda: print), '\nOriginal list:')
_l_(59929)
_c_(59932, _n_(59930, "print", lambda: print), _n_(59931, "nums", lambda: nums))
_l_(59933)
_c_(59935, _n_(59934, "print", lambda: print), '\nDeep copy of the said list:')
_l_(59936)
_c_(59939, _n_(59937, "print", lambda: print), _n_(59938, "deep_copy", lambda: deep_copy))
_l_(59940)
_c_(59942, _n_(59941, "print", lambda: print), '\nChange the value of some elements of the original list:')
_l_(59943)
_n_(59944, "nums", lambda: nums)[0][2] = 55
_l_(59945)
_n_(59946, "nums", lambda: nums)[1][1] = 77
_l_(59947)
_c_(59949, _n_(59948, "print", lambda: print), '\nOriginal list:')
_l_(59950)
_c_(59953, _n_(59951, "print", lambda: print), _n_(59952, "nums", lambda: nums))
_l_(59954)
_c_(59956, _n_(59955, "print", lambda: print), '\nSecond list (Deep copy):')
_l_(59957)
_c_(59960, _n_(59958, "print", lambda: print), _n_(59959, "deep_copy", lambda: deep_copy))
_l_(59961)