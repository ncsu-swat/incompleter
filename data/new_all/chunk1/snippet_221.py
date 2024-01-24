# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54011487/typeerror-unsupported-operand-types-for-image-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(381078)

except ImportError:
    pass

image = _c_(381082, _a_(381080, _n_(381079, "Image", lambda: Image), "open"), _n_(381081, "image_path", lambda: image_path))
_l_(381083)
image = _c_(381087, _a_(381085, _n_(381084, "np", lambda: np), "array"), _n_(381086, "image", lambda: image)) / 255
_l_(381088)