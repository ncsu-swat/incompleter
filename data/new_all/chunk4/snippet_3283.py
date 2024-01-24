# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76069846/register-function-raising-a-nameerror-when-referencing-the-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Quantity:
    _l_(618116)


    _CONVERT_FUNCS = []
    _l_(618098)

    def __register_conversion(func):
        _l_(618107)

        _c_(618103, _a_(618101, _a_(618100, _n_(618099, "Quantity", lambda: Quantity), "_CONVERT_FUNCS"), "append"), _n_(618102, "func", lambda: func))
        _l_(618104)
        aux = _n_(618105, "func", lambda: func)
        _l_(618106)
        return aux

    @__register_conversion
    def function1(a, b):
        _l_(618111)

        aux = _n_(618108, "a", lambda: a) + _n_(618109, "b", lambda: b)
        _l_(618110)
        return aux

    @__register_conversion
    def function2(a, b):
        _l_(618115)

        aux = _n_(618112, "a", lambda: a) * _n_(618113, "b", lambda: b)
        _l_(618114)
        return aux