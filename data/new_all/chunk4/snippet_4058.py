# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63417844/attributeerror-module-test-has-no-attribute-myfunc
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import test
    _l_(620312)

except ImportError:
    pass
class myclass:
    _l_(620320)

    ...
    _l_(620313)
    def mainfunc(self):
        _l_(620318)

        _c_(620316, _a_(620315, _n_(620314, "test", lambda: test), "myfunc"))
        _l_(620317)
    ...
    _l_(620319)
start = _c_(620322, _n_(620321, "myclass", lambda: myclass))
_l_(620323)
_c_(620326, _a_(620325, _n_(620324, "start", lambda: start), "mainfunc"))
_l_(620327)