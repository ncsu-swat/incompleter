# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53073447/attributeerror-module-has-no-attribute-while-avoiding-cyclic-reference-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import model
    _l_(551307)

except ImportError:
    pass
try:
    import viewController
    _l_(551309)

except ImportError:
    pass
mModel = _c_(551312, _a_(551311, _n_(551310, "model", lambda: model), "Model"))
_l_(551313)
mVC = _c_(551316, _a_(551315, _n_(551314, "viewController", lambda: viewController), "ViewController"))
_l_(551317)
_c_(551321, _a_(551319, _n_(551318, "mModel", lambda: mModel), "initializeApp"), _n_(551320, "mVC", lambda: mVC))
_l_(551322)