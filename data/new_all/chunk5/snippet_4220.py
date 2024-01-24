# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61497467/attributeerror-module-numpy-has-no-attribute-asarray
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(700501)

except ImportError:
    pass
try:
    import numpy as np
    _l_(700503)

except ImportError:
    pass
im = _c_(700506, _a_(700505, _n_(700504, "Image", lambda: Image), "open"), "photo.jpg", "r")
_l_(700507)
data = _c_(700511, _a_(700509, _n_(700508, "np", lambda: np), "asarray"), _n_(700510, "im", lambda: im))
_l_(700512)
_c_(700515, _n_(700513, "print", lambda: print), _n_(700514, "data", lambda: data))
_l_(700516)