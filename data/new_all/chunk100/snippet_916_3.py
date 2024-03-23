# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(92812)
_c_(92814, _n_(92813, "print", lambda: print), 'original List:')
_l_(92815)
_c_(92818, _n_(92816, "print", lambda: print), _n_(92817, "nums1", lambda: nums1))
_l_(92819)
_c_(92821, _n_(92820, "print", lambda: print), '\nRotate the said list in left direction by 4:')
_l_(92822)
result = _n_(92823, "nums1", lambda: nums1)[3:] + _n_(92824, "nums1", lambda: nums1)[:4]
_l_(92825)
_c_(92828, _n_(92826, "print", lambda: print), _n_(92827, "result", lambda: result))
_l_(92829)
_c_(92831, _n_(92830, "print", lambda: print), '\nRotate the said list in left direction by 2:')
_l_(92832)
result = _n_(92833, "nums1", lambda: nums1)[2:] + _n_(92834, "nums1", lambda: nums1)[:2]
_l_(92835)
_c_(92838, _n_(92836, "print", lambda: print), _n_(92837, "result", lambda: result))
_l_(92839)
_c_(92841, _n_(92840, "print", lambda: print), '\nRotate the said list in Right direction by 4:')
_l_(92842)
_c_(92845, _n_(92843, "print", lambda: print), _n_(92844, "result", lambda: result))
_l_(92846)
_c_(92848, _n_(92847, "print", lambda: print), '\nRotate the said list in Right direction by 2:')
_l_(92849)
result = _n_(92850, "nums1", lambda: nums1)[-2:] + _n_(92851, "nums1", lambda: nums1)[:-2]
_l_(92852)
_c_(92855, _n_(92853, "print", lambda: print), _n_(92854, "result", lambda: result))
_l_(92856)