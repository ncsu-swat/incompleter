# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60870654/attributeerror-module-bezier-has-no-attribute-curve-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(653765)

except ImportError:
    pass
try:
    import bezier
    _l_(653767)

except ImportError:
    pass

nodes1 = _c_(653770, _a_(653769, _n_(653768, "np", lambda: np), "asfortranarray"), [
[0.0, 0.5, 1.0],
[0.0, 1.0, 0.0]])
_l_(653771)

curve1 = _c_(653775, _a_(653773, _n_(653772, "bezier", lambda: bezier), "Curve"), _n_(653774, "nodes1", lambda: nodes1), degree=2)
_l_(653776)