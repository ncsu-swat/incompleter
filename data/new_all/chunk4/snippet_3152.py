# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37363764/python3-abstract-class-typeerror-not-raised
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from abc import ABCMeta, abstractmethod
    _l_(621940)

except ImportError:
    pass

class Base(_n_(621941, "object", lambda: object)):
    _l_(621947)

    __metaclass__ = _n_(621942, "ABCMeta", lambda: ABCMeta)
    _l_(621943)

    @_n_(621944, "abstractmethod", lambda: abstractmethod)
    def bar(self):
        _l_(621946)

        pass
        _l_(621945)


class Concrete(_n_(621948, "Base", lambda: Base)):
    _l_(621950)

    pass
    _l_(621949)


confused = _c_(621952, _n_(621951, "Concrete", lambda: Concrete))
_l_(621953)