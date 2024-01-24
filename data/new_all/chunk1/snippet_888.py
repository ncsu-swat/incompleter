# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75463626/typeerror-only-integer-tensors-of-a-single-element-can-be-converted-to-an-index
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(378194)

except ImportError:
    pass
try:
    import torch
    _l_(378196)

except ImportError:
    pass

theta = 0.6109
_l_(378197)
phi = 0.0
_l_(378198)
k0 = 6.2832
_l_(378199)
n_inc = 1.0
_l_(378200)

kinc = _n_(378201, "k0", lambda: k0)*_n_(378202, "n_inc", lambda: n_inc)*_c_(378225, _a_(378204, _n_(378203, "np", lambda: np), "array"), [_c_(378208, _a_(378206, _n_(378205, "np", lambda: np), "sin"), _n_(378207, "theta", lambda: theta))*_c_(378212, _a_(378210, _n_(378209, "np", lambda: np), "cos"), _n_(378211, "phi", lambda: phi)), 
                          _c_(378216, _a_(378214, _n_(378213, "np", lambda: np), "sin"), _n_(378215, "theta", lambda: theta))*_c_(378220, _a_(378218, _n_(378217, "np", lambda: np), "sin"), _n_(378219, "phi", lambda: phi)), 
                          _c_(378224, _a_(378222, _n_(378221, "np", lambda: np), "cos"), _n_(378223, "theta", lambda: theta))])
_l_(378226)
kinc = _c_(378230, _a_(378228, _n_(378227, "torch", lambda: torch), "tensor"), _n_(378229, "kinc", lambda: kinc))
_l_(378231)
_c_(378234, _n_(378232, "print", lambda: print), _n_(378233, "kinc", lambda: kinc))
_l_(378235)