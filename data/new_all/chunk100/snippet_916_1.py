# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(92722)
_c_(92724, _n_(92723, "print", lambda: print), 'original List:')
_l_(92725)
_c_(92728, _n_(92726, "print", lambda: print), _n_(92727, "nums1", lambda: nums1))
_l_(92729)
_c_(92731, _n_(92730, "print", lambda: print), '\nRotate the said list in left direction by 4:')
_l_(92732)
_c_(92735, _n_(92733, "print", lambda: print), _n_(92734, "result", lambda: result))
_l_(92736)
_c_(92738, _n_(92737, "print", lambda: print), '\nRotate the said list in left direction by 2:')
_l_(92739)
result = _n_(92740, "nums1", lambda: nums1)[2:] + _n_(92741, "nums1", lambda: nums1)[:2]
_l_(92742)
_c_(92745, _n_(92743, "print", lambda: print), _n_(92744, "result", lambda: result))
_l_(92746)
_c_(92748, _n_(92747, "print", lambda: print), '\nRotate the said list in Right direction by 4:')
_l_(92749)
result = _n_(92750, "nums1", lambda: nums1)[-3:] + _n_(92751, "nums1", lambda: nums1)[:-4]
_l_(92752)
_c_(92755, _n_(92753, "print", lambda: print), _n_(92754, "result", lambda: result))
_l_(92756)
_c_(92758, _n_(92757, "print", lambda: print), '\nRotate the said list in Right direction by 2:')
_l_(92759)
result = _n_(92760, "nums1", lambda: nums1)[-2:] + _n_(92761, "nums1", lambda: nums1)[:-2]
_l_(92762)
_c_(92765, _n_(92763, "print", lambda: print), _n_(92764, "result", lambda: result))
_l_(92766)