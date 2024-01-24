# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48026466/typeerror-unsupported-operand-types-for-int-and-nonetype-while-adding
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(366388)

except ImportError:
    pass
try:
    import numpy as np
    _l_(366390)

except ImportError:
    pass

img1=_c_(366393, _a_(366392, _n_(366391, "cv2", lambda: cv2), "imread"), '3.jpg')
_l_(366394)
img2=_c_(366397, _a_(366396, _n_(366395, "cv2", lambda: cv2), "imread"), '4.jpg')
_l_(366398)

add = _n_(366399, "img1", lambda: img1) + _n_(366400, "img2", lambda: img2)
_l_(366401)

_c_(366405, _a_(366403, _n_(366402, "cv2", lambda: cv2), "imshow"), 'add', _n_(366404, "add", lambda: add))
_l_(366406)
_c_(366409, _a_(366408, _n_(366407, "cv2", lambda: cv2), "waitKey"), 0)
_l_(366410)
_a_(366412, _n_(366411, "cv2", lambda: cv2), "destroyAllWindows")
_l_(366413)