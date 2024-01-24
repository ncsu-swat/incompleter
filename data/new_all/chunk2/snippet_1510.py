# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48830707/attributeerror-while-accessing-instance-variables
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Test():
    _l_(460752)


    __class_secret_number = 100
    _l_(460708)

    def __secret_func(self):
        _l_(460716)

        _n_(460709, "self", lambda: self).number1 = 1
        _l_(460710)
        _n_(460711, "self", lambda: self).__secret_number1 = 11
        _l_(460712)
        _c_(460714, _n_(460713, "print", lambda: print), 'You cannot see this unless accessing from the Class itself')
        _l_(460715)

    def test_func(self):
        _l_(460721)

        _n_(460717, "self", lambda: self).number2 = 2
        _l_(460718)
        _n_(460719, "self", lambda: self).__secret_number2 = 22
        _l_(460720)

    def my_func(self):
        _l_(460751)

        _c_(460724, _a_(460723, _n_(460722, "self", lambda: self), "__secret_func"))
        _l_(460725)
        _c_(460729, _n_(460726, "print", lambda: print), 'Secret no. from class: ', _a_(460728, _n_(460727, "self", lambda: self), "__class_secret_number"))
        _l_(460730)

        _c_(460734, _n_(460731, "print", lambda: print), 'non secret no. from secret func: ', _a_(460733, _n_(460732, "self", lambda: self), "number1"))
        _l_(460735)
        _c_(460739, _n_(460736, "print", lambda: print), 'Secret no. from secret func: ', _a_(460738, _n_(460737, "self", lambda: self), "__secret_number1"))
        _l_(460740)

        # These two prints raise an exception.
        _c_(460744, _n_(460741, "print", lambda: print), 'non secret no. from test_func: ', _a_(460743, _n_(460742, "self", lambda: self), "number2"))
        _l_(460745)
        _c_(460749, _n_(460746, "print", lambda: print), 'Secret no. from test_func: ', _a_(460748, _n_(460747, "self", lambda: self), "__secret_number2"))
        _l_(460750)

test = _c_(460754, _n_(460753, "Test", lambda: Test))
_l_(460755)
_c_(460758, _a_(460757, _n_(460756, "test", lambda: test), "my_func"))
_l_(460759)