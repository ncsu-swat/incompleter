# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70562802/inheritance-from-parent-class-return-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MathParent:
    _l_(633100)

    def multiply(self, number1, number2):
        _l_(633097)

        _n_(633090, "self", lambda: self).answer = _n_(633091, "number1", lambda: number1) * _n_(633092, "number2", lambda: number2)
        _l_(633093)
        aux = _a_(633095, _n_(633094, "self", lambda: self), "answer")
        _l_(633096)
        return aux
    def happy(self):
        _l_(633099)

        aux = "Nice Mark!"
        _l_(633098)
        return aux

class MathChild(_n_(633101, "MathParent", lambda: MathParent)):
    _l_(633107)

    def plus_x(self, x) :
        _l_(633106)

        aux = _a_(633103, _n_(633102, "self", lambda: self), "answer") + _n_(633104, "x", lambda: x)
        _l_(633105)
        return aux

p_out = _c_(633109, _n_(633108, "MathParent", lambda: MathParent))
_l_(633110)
_c_(633115, _n_(633111, "print", lambda: print), _c_(633114, _a_(633113, _n_(633112, "p_out", lambda: p_out), "multiply"), 5, 2))
_l_(633116)
_c_(633121, _n_(633117, "print", lambda: print), _c_(633120, _a_(633119, _n_(633118, "p_out", lambda: p_out), "happy")))
_l_(633122)

c_out = _c_(633124, _n_(633123, "MathChild", lambda: MathChild))
_l_(633125)
_c_(633130, _n_(633126, "print", lambda: print), _c_(633129, _a_(633128, _n_(633127, "c_out", lambda: c_out), "happy")))
_l_(633131)
_c_(633136, _n_(633132, "print", lambda: print), _c_(633135, _a_(633134, _n_(633133, "c_out", lambda: c_out), "plus_x"), 5))
_l_(633137)