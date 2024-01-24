# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47221143/open-cv-3-python-3-attributeerror-module-cv2-has-no-attribute-videocapture
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(653307)

except ImportError:
    pass
try:
    import cv2
    _l_(653309)

except ImportError:
    pass
cap = _c_(653312, _a_(653311, _n_(653310, "cv2", lambda: cv2), "VideoCapture"), 0)
_l_(653313)
while(True):
    _l_(653337)

    ret, frame = _c_(653316, _a_(653315, _n_(653314, "cap", lambda: cap), "read"))
    _l_(653317)
    gray = _c_(653323, _a_(653319, _n_(653318, "cv2", lambda: cv2), "cvtColor"), _n_(653320, "frame", lambda: frame), _a_(653322, _n_(653321, "cv2", lambda: cv2), "COLOR_BGR2GRAY"))
    _l_(653324)
    _c_(653328, _a_(653326, _n_(653325, "cv2", lambda: cv2), "imshow"), 'frame',_n_(653327, "gray", lambda: gray))
    _l_(653329)
    if _c_(653332, _a_(653331, _n_(653330, "cv2", lambda: cv2), "waitKey"), 1) & 0xFF == _c_(653334, _n_(653333, "ord", lambda: ord), 'q'):
        _l_(653336)

        break
        _l_(653335)
_c_(653340, _a_(653339, _n_(653338, "cap", lambda: cap), "release"))
_l_(653341)
_c_(653344, _a_(653343, _n_(653342, "cv2", lambda: cv2), "destroyAllWindows"))
_l_(653345)