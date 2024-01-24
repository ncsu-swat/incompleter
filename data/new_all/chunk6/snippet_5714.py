# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48026466/typeerror-unsupported-operand-types-for-int-and-nonetype-while-adding
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(342064)

except ImportError:
    pass
try:
    import numpy as np
    _l_(342066)

except ImportError:
    pass

img1=_c_(342069, _a_(342068, _n_(342067, "cv2", lambda: cv2), "imread"), '3.jpg')
_l_(342070)
img2=_c_(342073, _a_(342072, _n_(342071, "cv2", lambda: cv2), "imread"), '4.jpg')
_l_(342074)

add = _n_(342075, "img1", lambda: img1) + _n_(342076, "img2", lambda: img2)
_l_(342077)

_c_(342081, _a_(342079, _n_(342078, "cv2", lambda: cv2), "imshow"), 'add', _n_(342080, "add", lambda: add))
_l_(342082)
_c_(342085, _a_(342084, _n_(342083, "cv2", lambda: cv2), "waitKey"), 0)
_l_(342086)
_a_(342088, _n_(342087, "cv2", lambda: cv2), "destroyAllWindows")
_l_(342089)