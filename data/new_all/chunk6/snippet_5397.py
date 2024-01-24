# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55852727/typeerror-when-adding-cuda-device
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import torch
    _l_(359503)

except ImportError:
    pass
try:
    from torch import cuda
    _l_(359505)

except ImportError:
    pass
if _c_(359508, _a_(359507, _n_(359506, "cuda", lambda: cuda), "is_available")):
    _l_(359517)

    devic=_c_(359511, _a_(359510, _n_(359509, "cuda", lambda: cuda), "device"), 0)
    _l_(359512)
    layer=_c_(359515, _a_(359514, _n_(359513, "torch", lambda: torch), "rand"), [5,3,2],requires_grad=True)
    _l_(359516)