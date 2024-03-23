# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import copy
    _l_(59963)

except ImportError:
    pass
nums_x = [1, [2, 3, 4]]
_l_(59964)
_c_(59967, _n_(59965, "print", lambda: print), 'Original list: ', _n_(59966, "nums_x", lambda: nums_x))
_l_(59968)
nums_y = _c_(59972, _a_(59970, _n_(59969, "copy", lambda: copy), "deepcopy"), _n_(59971, "nums_x", lambda: nums_x))
_l_(59973)
_c_(59975, _n_(59974, "print", lambda: print), '\nDeep copy of the said list:')
_l_(59976)
_c_(59979, _n_(59977, "print", lambda: print), _n_(59978, "nums_y", lambda: nums_y))
_l_(59980)
_c_(59982, _n_(59981, "print", lambda: print), '\nChange the value of an element of the original list:')
_l_(59983)
_n_(59984, "nums_x", lambda: nums_x)[1][1] = 10
_l_(59985)
_c_(59988, _n_(59986, "print", lambda: print), _n_(59987, "nums_x", lambda: nums_x))
_l_(59989)
_c_(59991, _n_(59990, "print", lambda: print), '\nCopy of the second list (Deep copy):')
_l_(59992)
_c_(59995, _n_(59993, "print", lambda: print), _n_(59994, "nums_y", lambda: nums_y))
_l_(59996)
deep_copy = _c_(60000, _a_(59998, _n_(59997, "copy", lambda: copy), "deepcopy"), _n_(59999, "nums", lambda: nums))
_l_(60001)
_c_(60003, _n_(60002, "print", lambda: print), '\nOriginal list:')
_l_(60004)
_c_(60007, _n_(60005, "print", lambda: print), _n_(60006, "nums", lambda: nums))
_l_(60008)
_c_(60010, _n_(60009, "print", lambda: print), '\nDeep copy of the said list:')
_l_(60011)
_c_(60014, _n_(60012, "print", lambda: print), _n_(60013, "deep_copy", lambda: deep_copy))
_l_(60015)
_c_(60017, _n_(60016, "print", lambda: print), '\nChange the value of some elements of the original list:')
_l_(60018)
_n_(60019, "nums", lambda: nums)[0][2] = 55
_l_(60020)
_n_(60021, "nums", lambda: nums)[1][1] = 77
_l_(60022)
_c_(60024, _n_(60023, "print", lambda: print), '\nOriginal list:')
_l_(60025)
_c_(60028, _n_(60026, "print", lambda: print), _n_(60027, "nums", lambda: nums))
_l_(60029)
_c_(60031, _n_(60030, "print", lambda: print), '\nSecond list (Deep copy):')
_l_(60032)
_c_(60035, _n_(60033, "print", lambda: print), _n_(60034, "deep_copy", lambda: deep_copy))
_l_(60036)