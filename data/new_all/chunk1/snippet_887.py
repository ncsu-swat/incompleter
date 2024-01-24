# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75463626/typeerror-only-integer-tensors-of-a-single-element-can-be-converted-to-an-index
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
n_inc = _c_(394223, _a_(394222, _n_(394221, "torch", lambda: torch), "tensor"), 1)
_l_(394224)
theta = _c_(394227, _a_(394226, _n_(394225, "torch", lambda: torch), "tensor"), 0.6109)
_l_(394228)
phi = _c_(394231, _a_(394230, _n_(394229, "torch", lambda: torch), "tensor"), 0)
_l_(394232)
k0 = _c_(394235, _a_(394234, _n_(394233, "torch", lambda: torch), "tensor"), 6.2832)
_l_(394236)


kinc = _n_(394237, "k0", lambda: k0)*_n_(394238, "n_inc", lambda: n_inc)*[_c_(394242, _a_(394240, _n_(394239, "torch", lambda: torch), "sin"), _n_(394241, "theta", lambda: theta))*_c_(394246, _a_(394244, _n_(394243, "torch", lambda: torch), "cos"), _n_(394245, "phi", lambda: phi)),
                 _c_(394250, _a_(394248, _n_(394247, "torch", lambda: torch), "sin"), _n_(394249, "theta", lambda: theta))*_c_(394254, _a_(394252, _n_(394251, "torch", lambda: torch), "sin"), _n_(394253, "phi", lambda: phi)), 
                 _c_(394258, _a_(394256, _n_(394255, "torch", lambda: torch), "cos"), _n_(394257, "theta", lambda: theta))]
_l_(394259)
_c_(394262, _n_(394260, "print", lambda: print), _n_(394261, "kinc", lambda: kinc))
_l_(394263)