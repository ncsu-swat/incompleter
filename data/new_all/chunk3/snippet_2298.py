# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53073447/attributeerror-module-has-no-attribute-while-avoiding-cyclic-reference-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import model
    _l_(567147)

except ImportError:
    pass
class ViewController:
    _l_(567154)

    def initialize(self, mod:_a_(567149, _n_(567148, "model", lambda: model), "Model")):
        _l_(567153)

        _n_(567150, "self", lambda: self).model = _n_(567151, "mod", lambda: mod)
        _l_(567152)