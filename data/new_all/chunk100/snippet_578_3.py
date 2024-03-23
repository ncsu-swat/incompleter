# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import copy
    _l_(60109)

except ImportError:
    pass
nums_x = [1, [2, 3, 4]]
_l_(60110)
_c_(60113, _n_(60111, "print", lambda: print), 'Original list: ', _n_(60112, "nums_x", lambda: nums_x))
_l_(60114)
nums_y = _c_(60118, _a_(60116, _n_(60115, "copy", lambda: copy), "deepcopy"), _n_(60117, "nums_x", lambda: nums_x))
_l_(60119)
_c_(60121, _n_(60120, "print", lambda: print), '\nDeep copy of the said list:')
_l_(60122)
_c_(60125, _n_(60123, "print", lambda: print), _n_(60124, "nums_y", lambda: nums_y))
_l_(60126)
_c_(60128, _n_(60127, "print", lambda: print), '\nChange the value of an element of the original list:')
_l_(60129)
_n_(60130, "nums_x", lambda: nums_x)[1][1] = 10
_l_(60131)
_c_(60134, _n_(60132, "print", lambda: print), _n_(60133, "nums_x", lambda: nums_x))
_l_(60135)
_c_(60137, _n_(60136, "print", lambda: print), '\nCopy of the second list (Deep copy):')
_l_(60138)
_c_(60141, _n_(60139, "print", lambda: print), _n_(60140, "nums_y", lambda: nums_y))
_l_(60142)
nums = [[1, 2, 3], [4, 5, 6]]
_l_(60143)
_c_(60145, _n_(60144, "print", lambda: print), '\nOriginal list:')
_l_(60146)
_c_(60149, _n_(60147, "print", lambda: print), _n_(60148, "nums", lambda: nums))
_l_(60150)
_c_(60152, _n_(60151, "print", lambda: print), '\nDeep copy of the said list:')
_l_(60153)
_c_(60156, _n_(60154, "print", lambda: print), _n_(60155, "deep_copy", lambda: deep_copy))
_l_(60157)
_c_(60159, _n_(60158, "print", lambda: print), '\nChange the value of some elements of the original list:')
_l_(60160)
_n_(60161, "nums", lambda: nums)[0][2] = 55
_l_(60162)
_n_(60163, "nums", lambda: nums)[1][1] = 77
_l_(60164)
_c_(60166, _n_(60165, "print", lambda: print), '\nOriginal list:')
_l_(60167)
_c_(60170, _n_(60168, "print", lambda: print), _n_(60169, "nums", lambda: nums))
_l_(60171)
_c_(60173, _n_(60172, "print", lambda: print), '\nSecond list (Deep copy):')
_l_(60174)
_c_(60177, _n_(60175, "print", lambda: print), _n_(60176, "deep_copy", lambda: deep_copy))
_l_(60178)