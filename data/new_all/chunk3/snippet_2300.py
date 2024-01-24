# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53073447/attributeerror-module-has-no-attribute-while-avoiding-cyclic-reference-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import viewController
    _l_(572012)

except ImportError:
    pass
class Model():
    _l_(572025)

    def initializeApp(self, viewContr: _a_(572014, _n_(572013, "viewController", lambda: viewController), "ViewController")):
        _l_(572024)

        _n_(572015, "self", lambda: self).vc = _n_(572016, "viewContr", lambda: viewContr)
        _l_(572017)
        _c_(572022, _a_(572020, _a_(572019, _n_(572018, "self", lambda: self), "vc"), "initialize"), _n_(572021, "self", lambda: self))
        _l_(572023)