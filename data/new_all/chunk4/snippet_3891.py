# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65844779/typeerror-init-takes-from-1-to-6-positional-arguments-but-7-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ThreadWithReturnValue(_n_(583230, "Thread", lambda: Thread)):
    _l_(583267)

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        _l_(583244)

        _c_(583240, _a_(583232, _n_(583231, "Thread", lambda: Thread), "__init__"), _n_(583233, "self", lambda: self), _n_(583234, "group", lambda: group), _n_(583235, "target", lambda: target), _n_(583236, "name", lambda: name), _n_(583237, "args", lambda: args), _n_(583238, "kwargs", lambda: kwargs), _n_(583239, "Verbose", lambda: Verbose))
        _l_(583241)
        _n_(583242, "self", lambda: self)._return = None
        _l_(583243)
    def run(self):
        _l_(583257)

        if _a_(583246, _n_(583245, "self", lambda: self), "_Thread__target") is not None:
            _l_(583256)

            _n_(583247, "self", lambda: self)._return = _c_(583254, _a_(583249, _n_(583248, "self", lambda: self), "_Thread__target"), *_a_(583251, _n_(583250, "self", lambda: self), "_Thread__args"),
                                                **_a_(583253, _n_(583252, "self", lambda: self), "_Thread__kwargs"))
            _l_(583255)
    def join(self):
        _l_(583266)

        _c_(583261, _a_(583259, _n_(583258, "Thread", lambda: Thread), "join"), _n_(583260, "self", lambda: self))
        _l_(583262)
        aux = _a_(583264, _n_(583263, "self", lambda: self), "_return")
        _l_(583265)
        return aux