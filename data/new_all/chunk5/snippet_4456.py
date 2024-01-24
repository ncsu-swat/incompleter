# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57422230/receiving-a-typeerror-when-using-scipy-integrate-quad-cant-convert-complex-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def H(G):
    _l_(670983)

    aux = _c_(670981, _a_(670971, _n_(670970, "integrate", lambda: integrate), "quad"), lambda x: (_a_(670973, _n_(670972, "np", lambda: np), "pi")*_c_(670977, _a_(670975, _n_(670974, "np", lambda: np), "exp"), -_n_(670976, "x", lambda: x)))/(1+1j*_n_(670978, "G", lambda: G)),0,_a_(670980, _n_(670979, "np", lambda: np), "inf"))
    _l_(670982)
    return aux
_c_(670990, _a_(670986, _a_(670985, _n_(670984, "scipy", lambda: scipy), "optimize"), "fsolve"), lambda G: _c_(670989, _n_(670987, "f", lambda: f), _n_(670988, "G", lambda: G)),x0 = 1)
_l_(670991)