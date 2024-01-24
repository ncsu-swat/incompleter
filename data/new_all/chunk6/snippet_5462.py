# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43809513/getting-attributeerror-module-matplotlib-image-has-no-attribute-frombyte-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(345613)

except ImportError:
    pass
image = _c_(345618, _a_(345616, _a_(345615, _n_(345614, "caffe", lambda: caffe), "io"), "load_image"), _n_(345617, "root", lambda: root) + 'images/cat.jpg')
_l_(345619)
transformed_image = _c_(345623, _a_(345621, _n_(345620, "transformer", lambda: transformer), "preprocess"), 'data', _n_(345622, "image", lambda: image))
_l_(345624)
_c_(345628, _a_(345626, _n_(345625, "plt", lambda: plt), "imshow"), _n_(345627, "image", lambda: image))
_l_(345629)