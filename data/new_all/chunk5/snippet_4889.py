# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41782239/typeerror-module-object-is-not-callable-selectivesearch
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import skimage.data
    _l_(702259)

except ImportError:
    pass
try:
    import selectivesearch
    _l_(702261)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(702263)

except ImportError:
    pass
img = _c_(702266, _a_(702265, _a_(702264, skimage, "data"), "astronaut"))
_l_(702267)
img_lbl, regions= _c_(702271, _a_(702269, _n_(702268, "selectivesearch", lambda: selectivesearch), "selectivesearch"), _n_(702270, "img", lambda: img), scale=500, sigma=0.9, min_size=10)
_l_(702272)
_n_(702273, "regions", lambda: regions)[:10]
_l_(702274)
[{'labels': [0.0], 'rect': (0, 0, 15, 24), 'size': 260},
{'labels': [1.0], 'rect': (13, 0, 1, 12), 'size': 23}]
_l_(702275)