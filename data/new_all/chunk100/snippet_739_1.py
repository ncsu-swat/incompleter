# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(74402)

except ImportError:
    pass
try:
    import numpy as np
    _l_(74404)

except ImportError:
    pass
image = _c_(74408, _a_(74406, _n_(74405, "Image", lambda: Image), "fromarray"), _n_(74407, "a", lambda: a), 'RGB')
_l_(74409)
_c_(74412, _a_(74411, _n_(74410, "image", lambda: image), "save"), 'white.png', 'PNG')
_l_(74413)