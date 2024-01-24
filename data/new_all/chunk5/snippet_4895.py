# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41782239/typeerror-module-object-is-not-callable-selectivesearch
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import skimage.data
    _l_(671029)

except ImportError:
    pass
try:
    import selectivesearch
    _l_(671031)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(671033)

except ImportError:
    pass
img = _c_(671036, _a_(671035, _a_(671034, skimage, "data"), "astronaut"))
_l_(671037)
img_lbl, regions= _c_(671041, _a_(671039, _n_(671038, "selectivesearch", lambda: selectivesearch), "selectivesearch"), _n_(671040, "img", lambda: img), scale=500, sigma=0.9, min_size=10)
_l_(671042)
_n_(671043, "regions", lambda: regions)[:10]
_l_(671044)
[{'labels': [0.0], 'rect': (0, 0, 15, 24), 'size': 260},
{'labels': [1.0], 'rect': (13, 0, 1, 12), 'size': 23}]
_l_(671045)