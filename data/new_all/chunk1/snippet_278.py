# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64627848/attributeerror-numpy-ndarray-object-has-no-attribute-imwrite
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(405977)

except ImportError:
    pass
img = _c_(405980, _a_(405979, _n_(405978, "cv2", lambda: cv2), "imread"), "input.jpg")
_l_(405981)
_c_(405984, _a_(405983, _n_(405982, "img", lambda: img), "imwrite"), "output.jpg")
_l_(405985)