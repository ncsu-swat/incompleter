# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44714626/how-to-solve-the-typeerror-nonetype-object-is-not-subscriptable-in-opencv-cv
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(413261)

except ImportError:
    pass
try:
    import cv2
    _l_(413263)

except ImportError:
    pass
img = _c_(413268, _a_(413265, _n_(413264, "cv2", lambda: cv2), "imread"), 'freelancer.jpg',_a_(413267, _n_(413266, "cv2", lambda: cv2), "IMREAD_COLOR"))
_l_(413269)
px  = _n_(413270, "img", lambda: img)[55,55]
_l_(413271)
_c_(413274, _n_(413272, "print", lambda: print), _n_(413273, "px", lambda: px))
_l_(413275)