# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50763584/code-works-in-python-2-but-not-python3-typeerror-a-bytes-like-object-is-require
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(432627)

except ImportError:
    pass
try:
    import pickle
    _l_(432629)

except ImportError:
    pass

modelpath = "models/"
_l_(432630)

gmm_files = [_c_(432636, _a_(432633, _a_(432632, _n_(432631, "os", lambda: os), "path"), "join"), _n_(432634, "modelpath", lambda: modelpath),_n_(432635, "fname", lambda: fname)) for fname in 
          _c_(432640, _a_(432638, _n_(432637, "os", lambda: os), "listdir"), _n_(432639, "modelpath", lambda: modelpath)) if _c_(432643, _a_(432642, _n_(432641, "fname", lambda: fname), "endswith"), '.gmm')]
_l_(432644)

models    = [_c_(432650, _a_(432646, _n_(432645, "pickle", lambda: pickle), "load"), _c_(432649, _n_(432647, "open", lambda: open), _n_(432648, "fname", lambda: fname),'r')) for fname in _n_(432651, "gmm_files", lambda: gmm_files)]
_l_(432652)