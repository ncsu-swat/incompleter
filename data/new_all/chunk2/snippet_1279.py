# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56731528/python-threading-typeerror-testmethod-takes-2-positional-arguments-but-12-w
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from threading import Thread
    _l_(432326)

except ImportError:
    pass

class TestClass:
    _l_(432345)

    def _testmethod(self, argument):
        _l_(432331)

        _c_(432329, _n_(432327, "print", lambda: print), _n_(432328, "argument", lambda: argument))
        _l_(432330)

    def __init__(self, arg):
        _l_(432344)

        _n_(432332, "self", lambda: self).T = _c_(432337, _n_(432333, "Thread", lambda: Thread), target=_a_(432335, _n_(432334, "self", lambda: self), "_testmethod"), args=(_n_(432336, "arg", lambda: arg),))
        _l_(432338)
        _c_(432342, _a_(432341, _a_(432340, _n_(432339, "self", lambda: self), "T"), "start"))        
        _l_(432343)        

C = _c_(432347, _n_(432346, "TestClass", lambda: TestClass), "hello world")
_l_(432348)