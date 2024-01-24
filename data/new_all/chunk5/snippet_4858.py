# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45154163/attributeerror-second-object-has-no-attribute-funct
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Second(_n_(655817, "QDialog", lambda: QDialog)):
    _l_(655852)

    def __init__(self, parent=None):
        _l_(655851)

        _c_(655823, _a_(655821, _n_(655818, "super", lambda: super)(_n_(655819, "Second", lambda: Second), _n_(655820, "self", lambda: self)), "__init__"), _n_(655822, "parent", lambda: parent))
        _l_(655824)
        def funct():
            _l_(655828)

            _c_(655826, _n_(655825, "print", lambda: print), "This is a test")
            _l_(655827)
        buttonBox = _c_(655835, _n_(655829, "QDialogButtonBox", lambda: QDialogButtonBox), _a_(655831, _n_(655830, "QDialogButtonBox", lambda: QDialogButtonBox), "Ok")|_a_(655833, _n_(655832, "QDialogButtonBox", lambda: QDialogButtonBox), "Cancel"), _n_(655834, "self", lambda: self))
        _l_(655836)
        _c_(655842, _a_(655839, _a_(655838, _n_(655837, "buttonBox", lambda: buttonBox), "rejected"), "connect"), _a_(655841, _n_(655840, "self", lambda: self), "reject"))
        _l_(655843)
        _c_(655849, _a_(655846, _a_(655845, _n_(655844, "buttonBox", lambda: buttonBox), "accepted"), "connect"), _a_(655848, _n_(655847, "self", lambda: self), "funct"))
        _l_(655850)