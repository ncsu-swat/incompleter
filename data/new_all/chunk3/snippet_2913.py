# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58572142/typeerror-argument-of-type-windowspath-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(548690)

except ImportError:
    pass
try:
    import os
    _l_(548692)

except ImportError:
    pass
try:
    import cv2
    _l_(548694)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(548696)

except ImportError:
    pass
try:
    from os import listdir
    _l_(548698)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(548700)

except ImportError:
    pass

all_images = _c_(548706, _n_(548701, "list", lambda: list), _c_(548705, _a_(548704, _c_(548703, _n_(548702, "Path", lambda: Path), r'D:/face/train'), "glob"), '**/*.jpg'))
_l_(548707)
_c_(548722, _a_(548709, _n_(548708, "np", lambda: np), "array"), [_c_(548720, _a_(548719, _c_(548718, _a_(548711, _n_(548710, "np", lambda: np), "array"), _c_(548717, _a_(548713, _n_(548712, "cv2", lambda: cv2), "imread"), _c_(548716, _n_(548714, "str", lambda: str), _n_(548715, "file", lambda: file)))), "flatten")) for file in _n_(548721, "all_images", lambda: all_images)])
_l_(548723)
Path = r'D:\face\train'
_l_(548724)
_c_(548727, _n_(548725, "print", lambda: print), _n_(548726, "all_images", lambda: all_images)[0])
_l_(548728)