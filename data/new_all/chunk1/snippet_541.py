# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49416273/attributeerror-nonetype-object-has-no-attribute-when-creating-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def Foo():
    _l_(392438)

    a = 0
    _l_(392433)
    def bar(self):
        _l_(392437)

        aux = _a_(392435, _n_(392434, "self", lambda: self), "a")
        _l_(392436)
        return aux

f = _c_(392440, _n_(392439, "Foo", lambda: Foo))
_l_(392441)
_c_(392444, _a_(392443, _n_(392442, "f", lambda: f), "bar")) # error
_l_(392445) # error