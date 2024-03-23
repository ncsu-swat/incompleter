# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import copy
    _l_(21723)

except ImportError:
    pass
_c_(21726, _n_(21724, "print", lambda: print), 'Original dictionary: ', _n_(21725, "nums_x", lambda: nums_x))
_l_(21727)
nums_y = _c_(21731, _a_(21729, _n_(21728, "copy", lambda: copy), "deepcopy"), _n_(21730, "nums_x", lambda: nums_x))
_l_(21732)
_c_(21734, _n_(21733, "print", lambda: print), '\nDeep copy of the said list:')
_l_(21735)
_c_(21738, _n_(21736, "print", lambda: print), _n_(21737, "nums_y", lambda: nums_y))
_l_(21739)
_c_(21741, _n_(21740, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(21742)
_n_(21743, "nums_x", lambda: nums_x)['cc']['c'] = 10
_l_(21744)
_c_(21747, _n_(21745, "print", lambda: print), _n_(21746, "nums_x", lambda: nums_x))
_l_(21748)
_c_(21750, _n_(21749, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(21751)
_c_(21754, _n_(21752, "print", lambda: print), _n_(21753, "nums_y", lambda: nums_y))
_l_(21755)
nums = {'x': 1, 'y': 2, 'zz': {'z': 3}}
_l_(21756)
nums_copy = _c_(21760, _a_(21758, _n_(21757, "copy", lambda: copy), "deepcopy"), _n_(21759, "nums", lambda: nums))
_l_(21761)
_c_(21763, _n_(21762, "print", lambda: print), '\nOriginal dictionary :')
_l_(21764)
_c_(21767, _n_(21765, "print", lambda: print), _n_(21766, "nums", lambda: nums))
_l_(21768)
_c_(21770, _n_(21769, "print", lambda: print), '\nDeep copy of the said list:')
_l_(21771)
_c_(21774, _n_(21772, "print", lambda: print), _n_(21773, "nums_copy", lambda: nums_copy))
_l_(21775)
_c_(21777, _n_(21776, "print", lambda: print), '\nChange the value of an element of the original dictionary:')
_l_(21778)
_n_(21779, "nums", lambda: nums)['zz']['z'] = 10
_l_(21780)
_c_(21782, _n_(21781, "print", lambda: print), '\nFirst dictionary:')
_l_(21783)
_c_(21786, _n_(21784, "print", lambda: print), _n_(21785, "nums", lambda: nums))
_l_(21787)
_c_(21789, _n_(21788, "print", lambda: print), '\nSecond dictionary (Deep copy):')
_l_(21790)
_c_(21793, _n_(21791, "print", lambda: print), _n_(21792, "nums_copy", lambda: nums_copy))
_l_(21794)