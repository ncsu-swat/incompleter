# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63417844/attributeerror-module-test-has-no-attribute-myfunc
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import test
    _l_(585940)

except ImportError:
    pass
class myclass:
    _l_(585948)

    ...
    _l_(585941)
    def mainfunc(self):
        _l_(585946)

        _c_(585944, _a_(585943, _n_(585942, "test", lambda: test), "myfunc"))
        _l_(585945)
    ...
    _l_(585947)
start = _c_(585950, _n_(585949, "myclass", lambda: myclass))
_l_(585951)
_c_(585954, _a_(585953, _n_(585952, "start", lambda: start), "mainfunc"))
_l_(585955)