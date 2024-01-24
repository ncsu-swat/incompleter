# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51126531/resizing-to-bigger-resolution-with-skimage-causes-shape-typeerror-in-keras
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from  skimage import transform
    _l_(434983)

except ImportError:
    pass
new_shape = (48,88,3)
_l_(434984)
x_train = _c_(434993, _a_(434986, _n_(434985, "np", lambda: np), "asarray"), [_c_(434991, _a_(434988, _n_(434987, "transform", lambda: transform), "resize"), _n_(434989, "image", lambda: image), _n_(434990, "new_shape", lambda: new_shape)) for image in _n_(434992, "x_train", lambda: x_train)])
_l_(434994)