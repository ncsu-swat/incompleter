# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65637744/attributeerror-module-skimage-has-no-attribute-filters
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cv2
    _l_(383658)

except ImportError:
    pass
try:
    import numpy as np
    _l_(383660)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(383662)

except ImportError:
    pass
try:
    import skimage
    _l_(383664)

except ImportError:
    pass

my_image = _c_(383667, _a_(383666, _n_(383665, "cv2", lambda: cv2), "imread"), 'my_image.jpeg', 1)
_l_(383668)

gray = _c_(383674, _a_(383670, _n_(383669, "cv2", lambda: cv2), "cvtColor"), _n_(383671, "my_image", lambda: my_image), _a_(383673, _n_(383672, "cv2", lambda: cv2), "COLOR_BGR2GRAY"))
_l_(383675)
b = _c_(383680, _a_(383678, _a_(383677, _n_(383676, "skimage", lambda: skimage), "filters"), "threshold_local"), _n_(383679, "gray", lambda: gray),19,offset=10)
_l_(383681)
b = _c_(383685, _a_(383683, _n_(383682, "Image", lambda: Image), "fromarray"), _n_(383684, "b", lambda: b))
_l_(383686)
b = _c_(383689, _a_(383688, _n_(383687, "b", lambda: b), "convert"), "L")
_l_(383690)
_c_(383693, _a_(383692, _n_(383691, "b", lambda: b), "save"), 'adaptive_output.png')
_l_(383694)