# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48026466/typeerror-unsupported-operand-types-for-int-and-nonetype-while-adding
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(338325)

except ImportError:
    pass
try:
    import numpy as np
    _l_(338327)

except ImportError:
    pass

img1=_c_(338330, _a_(338329, _n_(338328, "cv2", lambda: cv2), "imread"), '3.jpg')
_l_(338331)
img2=_c_(338334, _a_(338333, _n_(338332, "cv2", lambda: cv2), "imread"), '4.jpg')
_l_(338335)

add = _n_(338336, "img1", lambda: img1) + _n_(338337, "img2", lambda: img2)
_l_(338338)

_c_(338342, _a_(338340, _n_(338339, "cv2", lambda: cv2), "imshow"), 'add', _n_(338341, "add", lambda: add))
_l_(338343)
_c_(338346, _a_(338345, _n_(338344, "cv2", lambda: cv2), "waitKey"), 0)
_l_(338347)
_a_(338349, _n_(338348, "cv2", lambda: cv2), "destroyAllWindows")
_l_(338350)