# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54011487/typeerror-unsupported-operand-types-for-image-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(379003)

except ImportError:
    pass

image = _c_(379007, _a_(379005, _n_(379004, "Image", lambda: Image), "open"), _n_(379006, "image_path", lambda: image_path))
_l_(379008)
image = _c_(379012, _a_(379010, _n_(379009, "np", lambda: np), "asarray"), _n_(379011, "image", lambda: image)) / 255
_l_(379013)