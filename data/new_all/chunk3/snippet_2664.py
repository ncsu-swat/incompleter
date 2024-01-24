# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67415057/python-add-a-method-with-parameters-with-class-decorator-results-in-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyInp(_n_(535272, "int", lambda: int)):
    _l_(535274)

    pass
    _l_(535273)

def add_bar(cls, input_type):
    _l_(535288)

    def bar(self, inp :_n_(535275, "input_type", lambda: input_type)):
        _l_(535280)

        _c_(535278, _n_(535276, "print", lambda: print), f"bar: {_n_(535277, 'inp', lambda: inp)}")
        _l_(535279)

    _c_(535284, _n_(535281, "setattr", lambda: setattr), _n_(535282, "cls", lambda: cls), 'bar', _n_(535283, "bar", lambda: bar))
    _l_(535285)
    aux = _n_(535286, "cls", lambda: cls)
    _l_(535287)
    return aux

@_c_(535291, _n_(535289, "add_bar", lambda: add_bar), input_type=_n_(535290, "MyInp", lambda: MyInp))
class Foo():
    _l_(535293)

    pass
    _l_(535292)

f = _c_(535295, _n_(535294, "Foo", lambda: Foo))
_l_(535296)
_c_(535299, _a_(535298, _n_(535297, "f", lambda: f), "bar"), 3)
_l_(535300)