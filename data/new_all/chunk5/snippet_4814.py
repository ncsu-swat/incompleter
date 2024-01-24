# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47221143/open-cv-3-python-3-attributeerror-module-cv2-has-no-attribute-videocapture
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(685547)

except ImportError:
    pass
try:
    import cv2
    _l_(685549)

except ImportError:
    pass
cap = _c_(685552, _a_(685551, _n_(685550, "cv2", lambda: cv2), "VideoCapture"), 0)
_l_(685553)
while(True):
    _l_(685577)

    ret, frame = _c_(685556, _a_(685555, _n_(685554, "cap", lambda: cap), "read"))
    _l_(685557)
    gray = _c_(685563, _a_(685559, _n_(685558, "cv2", lambda: cv2), "cvtColor"), _n_(685560, "frame", lambda: frame), _a_(685562, _n_(685561, "cv2", lambda: cv2), "COLOR_BGR2GRAY"))
    _l_(685564)
    _c_(685568, _a_(685566, _n_(685565, "cv2", lambda: cv2), "imshow"), 'frame',_n_(685567, "gray", lambda: gray))
    _l_(685569)
    if _c_(685572, _a_(685571, _n_(685570, "cv2", lambda: cv2), "waitKey"), 1) & 0xFF == _c_(685574, _n_(685573, "ord", lambda: ord), 'q'):
        _l_(685576)

        break
        _l_(685575)
_c_(685580, _a_(685579, _n_(685578, "cap", lambda: cap), "release"))
_l_(685581)
_c_(685584, _a_(685583, _n_(685582, "cv2", lambda: cv2), "destroyAllWindows"))
_l_(685585)