# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53073447/attributeerror-module-has-no-attribute-while-avoiding-cyclic-reference-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import model
    _l_(573312)

except ImportError:
    pass
class ViewController:
    _l_(573317)

    def initialize(self, mod):
        _l_(573316)

        _n_(573313, "self", lambda: self).model = _n_(573314, "mod", lambda: mod)
        _l_(573315)