# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(74388)

except ImportError:
    pass
try:
    import numpy as np
    _l_(74390)

except ImportError:
    pass
a = _c_(74395, _a_(74392, _n_(74391, "np", lambda: np), "full"), (512, 256, 3), 255, dtype=_a_(74394, _n_(74393, "np", lambda: np), "uint8"))
_l_(74396)
_c_(74399, _a_(74398, _n_(74397, "image", lambda: image), "save"), 'white.png', 'PNG')
_l_(74400)