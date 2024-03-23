# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(92857)
_c_(92859, _n_(92858, "print", lambda: print), 'original List:')
_l_(92860)
_c_(92863, _n_(92861, "print", lambda: print), _n_(92862, "nums1", lambda: nums1))
_l_(92864)
_c_(92866, _n_(92865, "print", lambda: print), '\nRotate the said list in left direction by 4:')
_l_(92867)
result = _n_(92868, "nums1", lambda: nums1)[3:] + _n_(92869, "nums1", lambda: nums1)[:4]
_l_(92870)
_c_(92873, _n_(92871, "print", lambda: print), _n_(92872, "result", lambda: result))
_l_(92874)
_c_(92876, _n_(92875, "print", lambda: print), '\nRotate the said list in left direction by 2:')
_l_(92877)
_c_(92880, _n_(92878, "print", lambda: print), _n_(92879, "result", lambda: result))
_l_(92881)
_c_(92883, _n_(92882, "print", lambda: print), '\nRotate the said list in Right direction by 4:')
_l_(92884)
result = _n_(92885, "nums1", lambda: nums1)[-3:] + _n_(92886, "nums1", lambda: nums1)[:-4]
_l_(92887)
_c_(92890, _n_(92888, "print", lambda: print), _n_(92889, "result", lambda: result))
_l_(92891)
_c_(92893, _n_(92892, "print", lambda: print), '\nRotate the said list in Right direction by 2:')
_l_(92894)
result = _n_(92895, "nums1", lambda: nums1)[-2:] + _n_(92896, "nums1", lambda: nums1)[:-2]
_l_(92897)
_c_(92900, _n_(92898, "print", lambda: print), _n_(92899, "result", lambda: result))
_l_(92901)