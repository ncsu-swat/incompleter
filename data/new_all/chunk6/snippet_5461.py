# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43809513/getting-attributeerror-module-matplotlib-image-has-no-attribute-frombyte-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(370185)

except ImportError:
    pass
image = _c_(370190, _a_(370188, _a_(370187, _n_(370186, "caffe", lambda: caffe), "io"), "load_image"), _n_(370189, "root", lambda: root) + 'images/cat.jpg')
_l_(370191)
transformed_image = _c_(370195, _a_(370193, _n_(370192, "transformer", lambda: transformer), "preprocess"), 'data', _n_(370194, "image", lambda: image))
_l_(370196)
_c_(370200, _a_(370198, _n_(370197, "plt", lambda: plt), "imshow"), _n_(370199, "image", lambda: image))
_l_(370201)