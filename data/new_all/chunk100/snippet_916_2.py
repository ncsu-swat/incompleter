# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(92767)
_c_(92769, _n_(92768, "print", lambda: print), 'original List:')
_l_(92770)
_c_(92773, _n_(92771, "print", lambda: print), _n_(92772, "nums1", lambda: nums1))
_l_(92774)
_c_(92776, _n_(92775, "print", lambda: print), '\nRotate the said list in left direction by 4:')
_l_(92777)
result = _n_(92778, "nums1", lambda: nums1)[3:] + _n_(92779, "nums1", lambda: nums1)[:4]
_l_(92780)
_c_(92783, _n_(92781, "print", lambda: print), _n_(92782, "result", lambda: result))
_l_(92784)
_c_(92786, _n_(92785, "print", lambda: print), '\nRotate the said list in left direction by 2:')
_l_(92787)
result = _n_(92788, "nums1", lambda: nums1)[2:] + _n_(92789, "nums1", lambda: nums1)[:2]
_l_(92790)
_c_(92793, _n_(92791, "print", lambda: print), _n_(92792, "result", lambda: result))
_l_(92794)
_c_(92796, _n_(92795, "print", lambda: print), '\nRotate the said list in Right direction by 4:')
_l_(92797)
result = _n_(92798, "nums1", lambda: nums1)[-3:] + _n_(92799, "nums1", lambda: nums1)[:-4]
_l_(92800)
_c_(92803, _n_(92801, "print", lambda: print), _n_(92802, "result", lambda: result))
_l_(92804)
_c_(92806, _n_(92805, "print", lambda: print), '\nRotate the said list in Right direction by 2:')
_l_(92807)
_c_(92810, _n_(92808, "print", lambda: print), _n_(92809, "result", lambda: result))
_l_(92811)